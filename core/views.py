from django.shortcuts import render
from django.db.models import Count

from applications.models import *

##
##	/
##
def home(request):
	context = {
		'postingCounts': JobPosting.objects.count(),
		'activePostings': JobPosting.objects.filter(status='active'),
		'declinedPostings': JobPosting.objects.filter(status='declined', initial_screen=False),
		'sorryPassPostings': JobPosting.objects.filter(status='declined', initial_screen=True),
		'noContactPostings': JobPosting.objects.exclude(status='declined'),
		'dates': JobPosting.activeAppsCountByDate()[0],
		'counts': JobPosting.activeAppsCountByDate()[1],
	}
	return render(request, 'core/home.html', context)
	
	