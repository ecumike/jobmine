from django.contrib import admin

from .models import Company, JobPosting


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_at', 'updated_at', 'name', 'url')
	list_filter = ('created_at', 'updated_at')
	search_fields = ('name',)
	date_hierarchy = 'created_at'


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'applied_date',
		'initial_contact_date',
		'declined_date',
		'company',
		'title',
		'url',
		'status',
		'contact_names',
		'contact_emails',
		'initial_screen',
		'round_1',
		'round_2',
		'round_3',
		'round_4',
		'round_5',
	)
	list_filter = (
		'company__name',
		'applied_date',
		'initial_contact_date',
		'declined_date',
		'initial_screen',

	)
	date_hierarchy = 'created_at'

	search_fields = ('company__name',)
