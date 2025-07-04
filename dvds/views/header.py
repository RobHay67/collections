import logging
import streamlit as st
from dvds.views.selectors.dvd_series import selectbox_series
from dvds.views.selectors.season import selectbox_dvd_season
from dvds.views.selectors.doctor import selectbox_which_doctor
from dvds.views.button_save_dvds import button_save_dvds
from dvds.views.selectors.missing_eps import button_missing_dvd_eps_only


def page_header_dvds(scope):
	logging.partial(f"render_dvd_header")
	
	# The Numbers
	total_to_collect = len(scope.dvds_page_df)
	available_to_collect = scope.dvds_page_df['available'].sum()
	missing_episodes = total_to_collect - available_to_collect
	collected = scope.dvds_page_df['collected'].sum()
	still_to_collect = available_to_collect - collected
	
	col1,col2,col3,col4=st.columns([5,1.5,1.5,3])
	with col1: 
		selectbox_series(scope)
	
		subcol1, subcol2 = col1.columns(2)
		with subcol2:selectbox_dvd_season(scope)
		with subcol1:
			if scope.dvds_selected_series == 'Doctor Who':
				selectbox_which_doctor(scope)
	with col2:
		st.caption('Total Episodes = ' + str(total_to_collect))
		st.caption('Missing Episodes = ' + str(missing_episodes))
		st.write('Able to Collect = ', available_to_collect)
	with col3:
		st.write('Collected so far = ', collected)
		st.write('To Collect... = ', still_to_collect)
	with col4:
		button_save_dvds(scope)
		button_missing_dvd_eps_only(scope)