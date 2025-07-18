import logging
import streamlit as st
from dvds.views.header import page_header_dvds
from dvds.views.render_dvd import render_dvd
from dvds.model import Dvd

# page allows for the selection of either
# a) a season
# b) a doctor

# Page Configuration
scope = st.session_state
page = 'dvds'
scope.display_page = page
logging.success(f"NAVIGATE {page=}")

st.title('DVD Collection')

page_header_dvds()

for list_pos in range(0, Dvd.page_qty, 8):
	col1,col2,col3,col4,col5,col6,col7,col8=st.columns([2,2,2,2,2,2,2,2])
	st.divider()
	with col1: 
		render_dvd(scope, list_pos+0)
	with col2:
		render_dvd(scope, list_pos+1)
	with col3:
		render_dvd(scope, list_pos+2)
	with col4:
		render_dvd(scope, list_pos+3)
	with col5:
		render_dvd(scope, list_pos+4)
	with col6:
		render_dvd(scope, list_pos+5)
	with col7:
		render_dvd(scope, list_pos+6)
	with col8: 
		render_dvd(scope, list_pos+7)
