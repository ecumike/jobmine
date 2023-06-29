import pandas as pd

from django.db import models
from django.db.models import Avg, Q
from django.utils import timezone


def getToday():
	return timezone.now().date()

class Company(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	name = models.CharField(max_length=100, unique=True)
	url = models.URLField(max_length=255, null=True, blank=True)
	
	class Meta:
		ordering = ['name']
		verbose_name_plural = 'Companies'
		
	def __str__(self):
		return self.name

class JobPosting(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	
	applied_date = models.DateField(default=getToday)
	initial_contact_date = models.DateField(null=True, blank=True)
	declined_date = models.DateField(null=True, blank=True)
	# Auto-calc'd
	initial_contact_days = models.PositiveIntegerField(null=True, blank=True, editable=False)
	declined_days = models.PositiveIntegerField(null=True, blank=True, editable=False)
	# Info
	company = models.ForeignKey(Company, related_name='job_posting_company', on_delete=models.PROTECT)
	title = models.CharField(max_length=100)
	url = models.URLField(max_length=255, null=True, blank=True)
	contact_names = models.TextField(blank=True)
	contact_emails = models.TextField(blank=True)
	# Statuses
	status = models.CharField(choices=[
		('active','Active'),
		('declined','Declined')
	], max_length=10, default='', blank=True)
	initial_screen = models.BooleanField(default=False)
	round_1 = models.BooleanField(default=False)
	round_2 = models.BooleanField(default=False)
	round_3 = models.BooleanField(default=False)
	round_4 = models.BooleanField(default=False)
	round_5 = models.BooleanField(default=False)
	
	class Meta:
		ordering = ['company', 'title']
		
	def __str__(self):
		return f'{self.company} - {self.title}'
	
	def save(self, *args, **kwargs):
		if self.initial_contact_date:
			self.initial_contact_days = (self.initial_contact_date - self.applied_date).days
		
		if self.declined_date:
			self.declined_days = (self.declined_date - self.applied_date).days
		
		super(JobPosting, self).save(*args, **kwargs) 
		
		
	@staticmethod
	def activeAppsCountByDate():
		counts = []
		dates = []
		for date in pd.date_range(start='6/1/2023', end=pd.Timestamp.today()):
			dateAware = timezone.make_aware(date)
			activeCount = JobPosting.objects.filter(applied_date__lte=dateAware).exclude(status='declined', declined_date__lte=dateAware).count()
			dates.append(dateAware.strftime('%Y-%m-%d'))
			counts.append(activeCount)
			
		return (dates,counts)
	
	
	@staticmethod
	def getAverageInitialContactDays():
		return round(JobPosting.objects.filter(initial_contact_days__gt=0).aggregate(Avg('initial_contact_days'))['initial_contact_days__avg'],1)
	
	
	@staticmethod
	def getAverageDeclinedDays():
		return round(JobPosting.objects.filter(declined_days__gt=0).aggregate(Avg('declined_days'))['declined_days__avg'],1)
			
		
			
		