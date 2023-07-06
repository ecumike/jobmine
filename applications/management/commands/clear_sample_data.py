from django.core.management.base import BaseCommand, CommandError
from applications.models import Company, JobPosting


def clearSampleData():
	JobPosting.objects.all().delete()
	Company.objects.all().delete()


class Command(BaseCommand):
	help = "Deletes all companies and job posting."
	
	def handle(self, *args, **options):
		clearSampleData()
		self.stdout.write(
			self.style.SUCCESS('Successfully removed all sample data.')
		)
