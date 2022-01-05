


from pages.view.welcome import view_project_welcome
from config.model.folders import scope_folders


def set_scope(scope):
	
	# set_streamlit_page_config()								# should only run onetime

	if 'initial_load' not in scope:					
		scope.initial_load = True				# set the initial load state 
												# prevents this section from runnning again and
												# allows the ticker index to load next

		scope.loaded_comics = False				# set default status as have not loaded the data at this stage

		# scope_app(scope)					# This contains all the application settings
		# scope_pages(scope)					# This contains all the page Specific settings
		scope_folders(scope)					# Required before we can attempt to load any data
		# scope_download(scope)
		# scope_strategy(scope)
		# scope_chart(scope)
		# scope_results(scope)
		# scope_screener(scope)
		# scope_tickers(scope)
		scope.page_to_display = 'home_page'		# The homepage to display on first load

		view_project_welcome(scope)				# Render the home page

	if scope.initial_load:					# This will only run one time after the initial load has occured
	# 	scope_index(scope)
		scope.initial_load = False			# Prevent session_state from re-running during its use


	return scope