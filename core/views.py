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
		# "declined" is declined applications, no matter how far along they got, call or no calls.
		'declinedPostings': JobPosting.objects.filter(status='declined', initial_screen=False),
		# "pass" is declined applications that had at least an initial phone screen call.
		'sorryPassPostings': JobPosting.objects.filter(status='declined', initial_screen=True),
		'noContactPostings': JobPosting.objects.exclude(status='declined').exclude(initial_screen=True),
		'dates': JobPosting.activeAppsCountByDate()[0],
		'counts': JobPosting.activeAppsCountByDate()[1],
		'avgInitialContactDays': JobPosting.getAverageInitialContactDays(),
		'avgDeclinedDays': JobPosting.getAverageDeclinedDays(),
	}
	return render(request, 'core/home.html', context)
	
	