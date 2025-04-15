import logging
import streamlit as st
from dvds.views.selectors.dvd_series import selectbox_series
from dvds.views.selectors.season import selectbox_dvd_season
from dvds.views.selectors.doctor import selectbox_which_doctor
from dvds.views.button_save_dvds import button_save_dvds
from dvds.views.selectors.missing_eps import button_missing_dvd_eps_only


def page_header_dvds(scope):
	logging.partial(f"render_dvd_header")
	
	no_collected = scope.dvds_page_df['collected'].sum()
	available_to_collect = len(scope.dvds_page_df)
	number_missing = available_to_collect - no_collected
	
	col1,col2,col3=st.columns([5,3,3])
	with col1: 
		selectbox_series(scope)
	
		subcol1, subcol2 = col1.columns(2)
		with subcol2:selectbox_dvd_season(scope)
		with subcol1:
			if scope.dvds_selected_series == 'Doctor Who':
				selectbox_which_doctor(scope)
	with col2:
		st.write('Available = ', available_to_collect)
		st.write('Collected = ', no_collected)
		st.write('Missing... = ', number_missing)
	with col3:
		button_save_dvds(scope)
		button_missing_dvd_eps_only(scope)