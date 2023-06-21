from django.db import models
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
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	applied_date = models.DateField(default=getToday)
	company = models.ForeignKey(Company, related_name='job_posting_company', on_delete=models.PROTECT)
	title = models.CharField(max_length=100)
	url = models.URLField(max_length=255, null=True, blank=True)
	status = models.CharField(choices=[
		('active','Active'),
		('declined','Declined')
	], max_length=10, default='', blank=True)
	contact_names = models.TextField(blank=True)
	contact_emails = models.TextField(blank=True)
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
		
		