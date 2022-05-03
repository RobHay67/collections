

from config.streamlit import set_streamlit_page_config
from files.config import scope_file_locations
from pages.config import scope_pages
from comics.config import scope_comics
from dvds.config import scope_dvds

from pages.home import render_home_page


def set_scope(scope):
	
	set_streamlit_page_config()								# should only run onetime

	if 'initial_load' not in scope:					
		scope.initial_load = True				# set the initial load state 
												# prevents this section from runnning again and
												# allows the ticker index to load next
		scope_file_locations(scope)					# Required before we can attempt to load any data
		
		scope_comics(scope)
		scope_dvds(scope)

		scope_pages(scope)					# This contains all the page Specific settings

		render_home_page(scope)				# Render the home page

	if scope.initial_load:					# This will only run one time after the initial load has occured
		scope.initial_load = False			# Prevent session_state from re-running during its use


	return scope