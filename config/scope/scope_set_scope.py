import logging
from config.scope.scope_streamlit import set_streamlit_page_config
from files.scope_files_and_folders import scope_file_locations
from comics.scope.scope_comics import scope_comics
from dvds.scope.scope_dvds import scope_dvds


def set_scope(scope):
	logging.warning(f"set_scope")
	set_streamlit_page_config()					# should only run onetime

	if 'folder_project' not in scope:
		scope_file_locations(scope)				# Required before we can attempt to load any data
		scope_comics(scope)
		scope_dvds(scope)
		scope.display_page = 'home'

	return scope


