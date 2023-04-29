import streamlit as st

from files.config import scope_file_locations
from comics.config import scope_comics
from dvds.config import scope_dvds



def set_scope(scope):
	
	set_streamlit_page_config()					# should only run onetime

	if 'initial_load' not in scope:					
		scope.initial_load = True				# set the initial load state 
												# prevents this section from runnning again and
												# allows the ticker index to load next
		scope_file_locations(scope)				# Required before we can attempt to load any data
		scope_comics(scope)
		scope_dvds(scope)

	if scope.initial_load:						# This will only run one time after the initial load has occured
		scope.initial_load = False				# Prevent session_state from re-running during its use


	return scope


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Streamlit CONFIG  (TODO not sure this belongs in this spot - but its convenient for the moment)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_streamlit_page_config():
	
	# Set the Browser Tab Name for the App
	
	st.set_page_config( 
			page_title='Hobbies and Collections', 
			page_icon='🧩',
			layout="wide",
			)
	
	# Padding Between Controls
	padding = 1.0
	st.markdown(f""" <style>
		.reportview-container .main .block-container{{
			padding-top: {padding}rem;
			padding-right: {padding}rem;
			padding-left: {padding}rem;
			padding-bottom: {padding}rem;
		}} </style> """, unsafe_allow_html=True)

	# Remove whitespace from the top of the page and sidebar
	st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True) # this is heaps better

