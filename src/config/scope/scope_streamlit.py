import logging
import streamlit as st



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Streamlit CONFIG  (TODO not sure this belongs in this spot - but its convenient for the moment)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_streamlit_page_config():
	logging.warning("set_streamlit_page_config")
	# Set the Browser Tab Name for the App
	
	st.set_page_config( 
			page_title='Robs Hobbies - Collection Databases', 
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



