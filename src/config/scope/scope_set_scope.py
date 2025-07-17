import logging
from config.scope.scope_streamlit import set_streamlit_page_config

from comics.model import Comic
from dvds.model import Dvd

def set_scope(scope):
	logging.warning("set_scope")
	set_streamlit_page_config()					# should only run onetime

	if 'folder_project' not in scope:
		scope.display_page = 'home'
		Comic.load_comics()
		Dvd.load_dvds()
	return scope


