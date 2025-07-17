import logging
import streamlit as st
from dvds.model import Dvd


def selectbox_series():
	logging.trace("dvd_series_selectbox")
	widget_key = 'widget_dvd_series'
	
	previous_selection = Dvd.selected_series
	if previous_selection is not None:
		pos_for_previous = Dvd.series_list.index(previous_selection)	
	else: 
		pos_for_previous = None

	st.selectbox(
			label			= 'Choose DVD Series',
			options			= Dvd.series_list,
			index			= pos_for_previous,
			on_change		= change_series,
			args			= (widget_key, ),
			key				= widget_key,
			label_visibility= 'collapsed',
			)
	

def change_series(widget_key):
	logging.warning(f"change_series {widget_key=}")
	Dvd.selected_series = st.session_state[widget_key]
	Dvd.create_season_list()
	Dvd.create_page_dvds()
