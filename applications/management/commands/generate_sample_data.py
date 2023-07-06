import random 

from datetime import timedelta
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from applications.models import Company, JobPosting


fakeCompanies = ['Addtech X', 'Adelicatek', 'Arzo Tek', 'Binq', 'Capy Tech', 'Cela Tek', 'Client Tech', 'Cloud Sys', 'Compute Link', 'Cortex Fizzle', 'Creative Cog', 'Dash Gear', 'Digi Dust', 'Digital Flip', 'Digiznix', 'Doctor Tech', 'Dudtechx', 'Elytech Lab', 'Evertechix', 'Exo Pak', 'Flow Techy', 'Folksy Fix', 'Gadget Go', 'Gadgetrix', 'Geeky Stream', 'Genius Genius', 'Giga Tek', 'Gizmo Labs', 'Hard Tek', 'Humtech', 'Iding Tech', 'Imtech Pro', 'Infotec X', 'Inteli Desk', 'Internacionaltec', 'keywords', 'Limitless Techs', 'Logic Drip', 'Material Labs', 'Metricon', 'Neotechie', 'Nuevo Tec', 'Option Techs', 'Osso Tech', 'Other Technologies', 'Phone Streimel', 'Qilltech', 'Quantum Brinegar', 'Quest Tek', 'Robi Tech', 'Rocket Bright', 'Sci Tech Patter', 'Science Quest', 'Silcotech', 'Silly Technik', 'Silva Teknol', 'Skillful Stuff', 'slytechlab', 'Solu Tech', 'Spanner Hive', 'Syntechia', 'Takal', 'Tec Toad', 'Tech Traunch', 'Tech Trusty', 'Tech Zuleta', 'Techie Bits', 'Techkoz', 'Technicott', 'Technikum', 'Techno Spike', 'Technolog X', 'Tempo Fab', 'Terminologyx', 'Think Technik', 'Tinker Mindset', 'Torus360', 'Tronixia', 'Typical Tech', 'Zee Worx',]


fakeTitles = ['Software Engineer', 'Staff Software Engineer', 'Software UI Engineer', 'Software Engineer I', 'Software Engineer II', 'Senior Software Engineer', 'Senior Software Engineer I']


def createCompanies():
	for company in fakeCompanies:
		newCo = Company.objects.get_or_create(
			name = company,
			url = f'https://{company.lower()}.com'
		)
	return list(Company.objects.all())


def randomDate():
	'''
	Return a random datetime.
	'''
	start = timezone.now() - timedelta(days=60)
	end = timezone.now()
	
	return start + timedelta(
		seconds = random.randint(0, int((end - start).total_seconds()))
	)
	
	
def clearSampleData():
	JobPosting.objects.all().delete()
	Company.objects.all().delete()


def createSampleDataSet(num):
	'''
	Create companies
	Create (inbound #) random applications with all random data
	Minimum is 20, so we can randomly set declines and passes
	'''
	companyList = createCompanies()
	
	if num < 20:
		num = 20
		
	# Create job postings
	for i in range(num):
		company = random.choice(companyList)
		
		JobPosting.objects.create(
			applied_date = randomDate(),
			company = company,
			title = random.choice(fakeTitles),
			url = f'https://jobs.{company}/posting/1234567/',
		)
	
	jobPostingList = JobPosting.objects.all()
	
	# Randomly set initial screen for a few
	for i in range(8):
		posting = random.choice(jobPostingList)
		posting.initial_contact_date = posting.applied_date + timedelta(days = random.randint(3, 16))
		posting.initial_screen = True
		posting.save()
		
	# Randomly decline a few (no screen)
	for i in range(14):
		posting = random.choice(JobPosting.objects.exclude(initial_screen=True))
		posting.declined_date = posting.applied_date + timedelta(days = random.randint(3, 16))
		posting.save()
	
	# Randomly pass on a few (after at least initial screen)
	for i in range(4):
		posting = random.choice(JobPosting.objects.filter(status='active'))
		posting.declined_date = posting.applied_date + timedelta(days = random.randint(3, 16))
		posting.save()


class Command(BaseCommand):
	help = "Generates a random sample data set for display purposes for the given # of job postings"
	
	def add_arguments(self, parser):
		parser.add_argument('number', nargs='+', type=int)
	
	def handle(self, *args, **options):
		try:
			num = int(options['number'][0])
		except Poll.DoesNotExist:
			raise CommandError('Number of postings to create must be an int.')
		
		createSampleDataSet(num)
		self.stdout.write(
			self.style.SUCCESS('Successfully created all sample data, open the app in your browser to view.')
		)

