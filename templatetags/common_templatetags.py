from django import template

register = template.Library()

##
## Global template HTML helpers for site consistency and easy redesigns.
##
@register.simple_tag(takes_context=True)
def getTemplateHelpers(context):
	horizontalSpace = 'ph3 ph4-ns'
	rounded = 'br2'
	
	commonButton = 'bw0 dib pointer ph3 pv2 custom-animate-all border-box lh-copy custom-standard-button ' + rounded
	smallButton = 'bw0 dib pointer ph3 pv2 custom-animate-all border-box ' + rounded
	
	tab = rounded + ' custom-tab relative w-auto bg-animate db pointer ph4 pv3 mb0 bw0 fw5 bg-near-white hover-bg-light-gray'
	
	icons = {}
	
	return {
		'classes': {
			'button': commonButton,
			'smallButton': smallButton,
			'bluePriButton': 'bg-blue-70 hover-bg-dark-blue white hover-white',
			'blueSecButton': 'bg-near-white hover-bg-dark-blue dark-blue hover-white',
			'blueTertiaryButton': 'bg-white hover-bg-dark-blue blue-70 hover-white nounderline',
			'greenPriButton': 'bg-green hover-bg-dark-green white hover-white',
			'redPriButton': 'bg-red hover-bg-dark-red white hover-white',
			'redSecButton': 'bg-near-white hover-bg-red dark-red hover-white',
			'disabledButton': 'bg-black-10 black-40',
			'bulletlist': 'bo-bullet-list',
			'grid': horizontalSpace,
			'horizontalSpace': horizontalSpace,
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
			'hr': '<div class="' + horizontalSpace + ' w-100 mv5"><div class="bb b--silver"></div></div>',
			'icons': icons,
			'tableWidget': {
				'sortOnly': 'data-widget="datatable" data-fixed-header="true" data-paging="false" data-searching="false" data-info="false" class="w-100 hover stripe collapse display" width="100%"',
				'fullFeatures': 'data-widget="datatable" data-fixed-header="true" data-length-change="false" data-page-length="100" class="w-100 hover stripe collapse display" width="100%" data-buttons=\'["excel"]\' data-dom="lBifrtip"',
			},
		},
		'icons': {
			'add': '<svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path><title>Add</title></svg>',
			'edit': '<svg preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path><title>Edit</title></svg>'
		}
	}

