from django.core.management.base import BaseCommand
from applications.models import Company, JobPosting


def clear_sample_data():
	JobPosting.objects.all().delete()
	Company.objects.all().delete()


class Command(BaseCommand):
	help = "Deletes all companies and job posting."

	def handle(self, *args, **options):
		clear_sample_data()
		self.stdout.write(
			self.style.SUCCESS('Successfully removed all sample data.')
		)
