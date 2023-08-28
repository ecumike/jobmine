from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import Lower

from applications.models import *

##
##	/
##
def home(request):
	staleApplications = JobPosting.getStaleApplications()
	noContactPostings = JobPosting.objects.exclude(status='declined').exclude(initial_screen=True).only('title', 'url', 'company__name').select_related('company').order_by(Lower('company__name'))
	
	for ncp in noContactPostings:
		ncp.isOld = ncp in staleApplications
		
	appCountByDate = JobPosting.activeAppsCountByDate()
	declinedPostings = JobPosting.objects.filter(status='declined').only('title', 'url', 'company__name').select_related('company').order_by(Lower('company__name'))
	activePostings = JobPosting.objects.filter(status='active').only('title', 'url', 'company__name').select_related('company').order_by(Lower('company__name'))
	
	context = {
		'postingCounts': JobPosting.objects.count(),
		'activePostings': activePostings,
		'activePostingsCount': activePostings.count(),
		# "declined" is declined applications, no matter how far along they got, call or no calls.
		'declinedPostings': declinedPostings.filter(initial_screen=False),
		# "pass" is declined applications that had at least an initial phone screen call.
		'sorryPassPostings': declinedPostings.filter(initial_screen=True),
		'noContactPostings': noContactPostings,
		'dates': appCountByDate[0],
		'counts': appCountByDate[1],
		'newAppsCounts': JobPosting.newAppsByDate(),
		'avgInitialContactDays': JobPosting.getAverageInitialContactDays(),
		'avgDeclinedDays': JobPosting.getAverageDeclinedDays(),
	}
	return render(request, 'core/home.html', context)
	
	