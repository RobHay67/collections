import logging
import streamlit as st
from dvds.model import Dvd


def selectbox_which_doctor():
	logging.trace("selectbox_which_doctor")
	widget_key = 'widget_which_doctor'

	previous_selection = Dvd.selected_doctor
	if previous_selection is not None:
		pos_for_previous = Dvd.doctors_list.index(previous_selection)	
	else: 
		pos_for_previous = None

	st.selectbox(
					label		= 'Select by Doctor',
					options		= Dvd.doctors_list,
					index		= pos_for_previous,
					on_change	= change_doctor,
					args		= (widget_key, ),
					key			= widget_key,
					)


def change_doctor(widget_key):
	logging.warning(f"change_doctor {widget_key=}")
	Dvd.selected_doctor = st.session_state[widget_key]
	Dvd.create_season_list()
	Dvd.create_page_dvds()

