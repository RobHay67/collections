import logging
import streamlit as st
from dvds.model import Dvd


def selectbox_dvd_season():
	logging.trace("selectbox_dvd_season")
	widget_key = 'widget_dvd_season'

	previous_selection = Dvd.selected_season
	if previous_selection is not None:
		pos_for_previous = Dvd.seasons_list.index(previous_selection)	
	else: 
		pos_for_previous = None

	st.selectbox(
					label		= 'Select Seasons for Doctor Who',
					options		= Dvd.seasons_list,
					index		= pos_for_previous,
					on_change	= change_season,
					args		= (widget_key, ),
					key			= widget_key,
					)


def change_season(widget_key):
	logging.warning(f"change_season {widget_key=}")
	Dvd.selected_season = st.session_state[widget_key]
	Dvd.create_page_dvds()
	



