import logging
import streamlit as st
from comics.views.header import page_header_comics
from comics.views.render_comic import render_comic

from comics.model import Comic


# Page Configuration
scope = st.session_state
page = 'comics'
scope.display_page = page
logging.success(f"NAVIGATE {page=}")

st.title('Comic Collection')

page_header_comics(scope)

if Comic.selected_series is not None:
	for list_pos in range(0, Comic.page_qty, 4):
		col1,col2,col3,col4=st.columns([2,2,2,2])
		with col1: 
			render_comic(scope, list_pos+0)
		with col2: 
			render_comic(scope, list_pos+1)
		with col3: 
			render_comic(scope, list_pos+2)
		with col4: 
			render_comic(scope, list_pos+3)

	# st.write(Comic.page_comics)




