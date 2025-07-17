# ------------------------------------------------- Application
# activate .venv		> source .venv/bin/activate
# run application		> uv run streamlit run src/streamlit_app.py
# test object creation	> uv run src/comics/objects.py
# --------------------------------------------------------------------- 
# streamlit name		> robhay67-collections-home-3ou9ku
# git repo				> https://robhay67-collections-home-ge86ye.streamlit.app/dvds
# --------------------------------------------------------------------- 


import streamlit as st
from config.system.logger import set_logging_config
from config.system.log_instructions import log_instructions
from config.system.package_info import terminal_out_package_info
from config.system.re_render import app_is_re_rendering
from config.scope.scope_set_scope import set_scope
from page.navigation import sidebar_navigation
from config.system.scope_keys import terminal_out_scope_keys


scope=st.session_state
if 'config' not in scope:
	# This needs to be the first code to run
	set_logging_config()
	log_instructions()
	terminal_out_package_info()
	

if __name__ == "__main__":
	# optional debugging info
	app_is_re_rendering()
	
	if 'display_page' not in scope:
		set_scope(scope)

	page_navigation = sidebar_navigation(scope)
	page_navigation.run()

	terminal_out_scope_keys('streamlit_app')

