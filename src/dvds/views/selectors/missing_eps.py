import logging
import streamlit as st
from dvds.model import Dvd


def button_missing_dvd_eps_only():
	logging.trace("button_missing_dvd_eps_only")
	widget_label = 'dvd_missing_eps_button'

	if Dvd.selected_missing_only:
		button_type = "primary"
		button_label = "Show All Episodes"
	else :
		button_type = "secondary"
		button_label = "Show Episodes not yet Collected"

	st.button(
				label 				= button_label,
				use_container_width	= True,
				type				= button_type,
				on_click			= change_show_missing_episodes,
				key					= widget_label,
				)


def change_show_missing_episodes():
	logging.warning("change_show_missing_episodes")	
	if Dvd.selected_missing_only:
		new_vale = False
	else:
		new_vale = True
	Dvd.selected_missing_only = new_vale
	Dvd.create_page_dvds()
