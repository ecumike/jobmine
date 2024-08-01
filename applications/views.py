from django.shortcuts import render
from django.db.models.functions import Lower

from .models import JobPosting

##
##	/
##
def applications_home(request):
	staleApplications = JobPosting.get_stale_application()
	noContactPostings = JobPosting.objects.all_active().exclude(status='declined').exclude(initial_screen=True).only('title', 'url', 'company__name').select_related('company').order_by(Lower('company__name'))

	for ncp in noContactPostings:
		ncp.isOld = ncp in staleApplications

	appCountByDate = JobPosting.active_apps_count_by_date()
	declinedPostings = JobPosting.objects.all_active().filter(status='declined').only('title', 'url', 'company__name').select_related('company').order_by(Lower('company__name'))
	activePostings = JobPosting.objects.all_active().filter(status='active').only('title', 'url', 'company__name').select_related('company').order_by(Lower('company__name'))

	context = {
		'postingCounts': JobPosting.objects.all_active().count(),
		'activePostings': activePostings,
		'activePostingsCount': activePostings.count(),
		# "declined" is declined applications, no matter how far along they got, call or no calls.
		'declinedPostings': declinedPostings.filter(initial_screen=False),
		# "pass" is declined applications that had at least an initial phone screen call.
		'sorryPassPostings': declinedPostings.filter(initial_screen=True),
		'noContactPostings': noContactPostings,
		'dates': appCountByDate[0],
		'counts': appCountByDate[1],
		'newAppsCounts': JobPosting.new_apps_by_date(),
		'avgInitialContactDays': JobPosting.get_average_initial_contact_days(),
		'avgDeclinedDays': JobPosting.get_average_declined_days(),
	}
	return render(request, 'applications/home.html', context)

