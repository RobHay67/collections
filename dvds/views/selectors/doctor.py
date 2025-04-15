import logging
import streamlit as st
from dvds.scope.scope_list_of_seasons import scope_list_of_seasons
from dvds.scope.scope_dvds import scope_dvds_to_display
from dvds.scope.scope_page_covers import scope_dvd_covers_for_page


def selectbox_which_doctor(scope):
	logging.partial(f"selectbox_which_doctor")
	widget_key = 'widget_which_doctor'
	
	previous_selection = scope.dvds_selected_doctor
	pos_for_previous = scope.dvds_list_of_doctors_for_who.index(previous_selection)	

	st.selectbox(
					label='Select by Doctor',
					options=scope.dvds_list_of_doctors_for_who,
					index=pos_for_previous,
					on_change=change_doctor,
					args=(scope, widget_key),
					key=widget_key,
					)


def change_doctor(scope, widget_key):
	logging.warning(f"change_doctor {widget_key=}")
	selected_doctor = (scope[widget_key])
	scope.dvds_selected_doctor = selected_doctor
	scope.dvds_list_of_seasons = scope_list_of_seasons(scope)
	# Update Page Data
	scope.dvds_page_df = scope_dvds_to_display(scope)
	scope.dvds_page_covers = scope_dvd_covers_for_page(scope)

