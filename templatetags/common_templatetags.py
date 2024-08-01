from django import template

register = template.Library()

##
## Global template HTML helpers for site consistency and easy redesigns.
##
@register.simple_tag(takes_context=True)
def get_template_helpers(context):
	horizontal_space = 'ph3 ph4-ns'
	rounded = 'br2'

	common_button = 'bw0 dib pointer ph3 pv2 custom-animate-all border-box lh-copy custom-standard-button ' + rounded
	small_button = 'bw0 dib pointer ph3 pv2 custom-animate-all border-box ' + rounded

	return {
		'classes': {
			'button': common_button,
			'small_button': small_button,
			'bluePriButton': 'bg-blue-70 hover-bg-dark-blue white hover-white',
			'blueSecButton': 'bg-near-white hover-bg-dark-blue dark-blue hover-white',
			'blueTertiaryButton': 'bg-white hover-bg-dark-blue blue-70 hover-white nounderline',
			'greenPriButton': 'bg-green hover-bg-dark-green white hover-white',
			'redPriButton': 'bg-red hover-bg-dark-red white hover-white',
			'redSecButton': 'bg-near-white hover-bg-red dark-red hover-white',
			'disabledButton': 'bg-black-10 black-40',
			'bulletlist': 'bo-bullet-list',
			'grid': horizontal_space,
			'horizontal_space': horizontal_space,
			'hasIconFlexCenter': 'inline-flex items-center underline-hover',
			'link': 'custom-animate-all link linkcolor',
			'navItem': 'custom-animate-all underline-hover pa3 link f6 f5-ns db relative hover-dark-blue textcolor',
			'pageTitleSecondary': 'fw4',
			'rounded': rounded,
			'tableListCell': 'pv3 pr3 bb b--black-20',
			'tableListCellSmall': 'pv2 pr2 bb b--black-20 f6',
			'tableListCell_bt': 'pv2 bt b--black-20',
			'yellowMessage': 'ph2 bg-light-yellow bo-fadeout br2',
		},
		'html': {
			'hr': '<div class="' + horizontal_space + ' w-100 mv5"><div class="bb b--silver"></div></div>',
			'icons': {
				'old': '<svg class="icon" style="" width="18px" height="18px" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><title>>30 days since applied</title><g id="Layer_2" data-name="Layer 2"><g id="invisible_box" data-name="invisible box"><rect width="48" height="48" fill="none"/></g><g id="Q3_icons" data-name="Q3 icons"><g><path d="M14.2,31.9h0a2,2,0,0,0-.9-2.9A11.8,11.8,0,0,1,6.1,16.8,12,12,0,0,1,16.9,6a12.1,12.1,0,0,1,11.2,5.6,2.3,2.3,0,0,0,2.3.9h0a2,2,0,0,0,1.1-3,15.8,15.8,0,0,0-15-7.4,16,16,0,0,0-4.8,30.6A2,2,0,0,0,14.2,31.9Z"/><path d="M16.5,11.5v5h-5a2,2,0,0,0,0,4h9v-9a2,2,0,0,0-4,0Z"/><path d="M45.7,43l-15-26a2,2,0,0,0-3.4,0l-15,26A2,2,0,0,0,14,46H44A2,2,0,0,0,45.7,43ZM29,42a2,2,0,1,1,2-2A2,2,0,0,1,29,42Zm2-8a2,2,0,0,1-4,0V26a2,2,0,0,1,4,0Z"/></g></g></g></svg>',
				'edit': '<svg class="icon" style="" width="18px" height="18px" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path><title>Edit</title></svg>'
			},
			'tableWidget': {
				'sortOnly': 'data-widget="datatable" data-fixed-header="true" data-paging="false" data-searching="false" data-info="false" class="w-100 hover stripe collapse display" width="100%"',
				'fullFeatures': 'data-widget="datatable" data-fixed-header="true" data-length-change="false" data-page-length="100" class="w-100 hover stripe collapse display" width="100%" data-buttons=\'["excel"]\' data-dom="lBifrtip"',
			},
		},
	}

