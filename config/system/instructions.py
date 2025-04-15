import logging


def log_instructions():
	logging.render("log_instructions")
	# for i in range(2):print('')
	print(  '\033[95m' + 'partial  <05> Streamlit > components (buttons / dropdowns / uploader)' + '\033[0m')
	print(  '\033[95m' + 'debug    <10> Python    > minor/repetitive functions (helpers)' + '\033[0m')
	print(  '\033[95m' + 'common   <15> Python    > commonly run code - key' + '\033[0m')
	# print(  '\033[94m' + 'Info      <20> not used' + '\033[0m')
	print(  '\033[95m' + 'render   <25> Streamlit > render main pages (Controllers / Routers)' + '\033[0m')
	print(  '\033[95m' + 'warning  <30> Python    > Scope / config has been changed' + '\033[0m')
	print(  '\033[95m' + 'core     <35> Python    > Core Functions (Controllers)' + '\033[0m')
	print(  '\033[95m' + 'errors   <40> Python    > Actual Errors or unexpected results (look into these)' + '\033[0m')
	print(  '\033[95m' + 'critical <50> Python    > TODOs or placeholders notes that are currently being worked upon' + '\033[0m')

	for i in range(5):print('')
