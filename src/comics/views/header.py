import logging
import streamlit as st
from comics.views.widgets.series import selectbox_series
from comics.views.widgets.missing_eps import button_missing_comics_only
from comics.views.widgets.save import button_save_comics

from comics.model import Comic

def page_header_comics(scope):
	logging.trace("page_header_comics")

	no_collected 			= Comic.page_qty_collected 
	available_to_collect 	= Comic.page_qty 
	number_missing 			= Comic.page_qty_missing

	col1,col2,col3=st.columns([5,3,3])
	with col1: 
		selectbox_series(scope)
	with col2:
		st.write('Available = ', available_to_collect)
		st.write('Collected = ', no_collected)
		st.write('Missing... = ', number_missing)
	with col3:
		if Comic.selected_series is not None:
			button_missing_comics_only(scope)
		button_save_comics(scope)

	
