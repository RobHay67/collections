# ------------------------------------------------- Application
# activate venv			> source venv/bin/activate
# run application		> streamlit run streamlit_app.py
# --------------------------------------------------------------------- 
# streamlit name		> robhay67-collections-home-3ou9ku
# --------------------------------------------------------------------- 
# https://robhay67-collections-home-ge86ye.streamlit.app/dvds

import streamlit as st
from config.system.logger import set_logging_config
from config.system.re_render import app_is_re_rendering
from config.system.package_info import print_package_info
from config.system.instructions import log_instructions
from config.system.scope_keys import print_scope_keys
from config.scope.scope_set_scope import set_scope
from page.navigation.page_navigation import sidebar_navigation


scope=st.session_state
if 'config' not in scope:
	# This needs to be the first code to run
	set_logging_config()	
	

if __name__ == "__main__":
	# optional debugging info
	app_is_re_rendering()
	# print_package_info()
	log_instructions()
	# print_scope_keys('streamlit_app')
	
	if 'config' not in scope:set_scope(scope)
	page_navigation = sidebar_navigation(scope)
	page_navigation.run()

	# print_scope_keys('streamlit_app')


