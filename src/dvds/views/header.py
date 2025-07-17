import logging
import streamlit as st
from dvds.views.selectors.series import selectbox_series
from dvds.views.selectors.season import selectbox_dvd_season
from dvds.views.selectors.doctor import selectbox_which_doctor
from dvds.views.widgets.save import button_save_dvds
from dvds.views.selectors.missing_eps import button_missing_dvd_eps_only

from dvds.model import Dvd


def page_header_dvds():
	logging.trace("render_dvd_header")
	
	# The Numbers
	total_to_collect 		= Dvd.page_qty
	available_to_collect 	= Dvd.page_qty_available
	missing_episodes 		= total_to_collect - available_to_collect
	collected 				= Dvd.page_qty_collected
	still_to_collect 		= available_to_collect - collected
	
	col1,col2,col3,col4=st.columns([5,1.5,1.5,3])
	with col1: 
		selectbox_series()
	
		subcol1, subcol2 = col1.columns(2)
		with subcol2:
			selectbox_dvd_season()
		with subcol1:
			if Dvd.selected_series == "Doctor Who":
				selectbox_which_doctor()
	with col2:
		st.caption('Total Episodes = ' + str(total_to_collect))
		st.caption('Missing Episodes = ' + str(missing_episodes))
		st.write('Able to Collect = ', available_to_collect)
	with col3:
		st.write('Collected so far = ', collected)
		st.write('To Collect... = ', still_to_collect)
	with col4:
		button_save_dvds()
		button_missing_dvd_eps_only()