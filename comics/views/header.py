import logging
import streamlit as st
from comics.views.selectors.series import selectbox_series
from comics.views.selectors.missing_eps import button_missing_comics_only
from comics.views.button_save import button_save_comics

def page_header_comics(scope):
	logging.partial(f"page_header_comics")

	no_collected = scope.comics_page_df['collected'].sum()
	available_to_collect = len(scope.comics_page_df)
	number_missing = available_to_collect - no_collected

	col1,col2,col3=st.columns([5,3,3])
	with col1: selectbox_series(scope)
	with col2:
		st.write('Available = ', available_to_collect)
		st.write('Collected = ', no_collected)
		st.write('Missing... = ', number_missing)
	with col3:
		if scope.comics_selected_series != None:
			button_missing_comics_only(scope)
		button_save_comics(scope)

	
