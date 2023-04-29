
import streamlit as st

from dvds.config import set_dvds_to_display
from dvds.config import scope_dvd_season_list



def dvd_doctor_selectbox(scope):
	widget_key = 'widget_dvd_doctor'
	previous_selection = scope.dvd_selected_doctor
	pos_for_previous = scope.dvd_doctor_list.index(previous_selection)	

	st.selectbox(
					label='Available Doctors for ' + scope.dvd_selected_series,
					options=scope.dvd_doctor_list,
					index=pos_for_previous,
					on_change=set_dvd_doctor,
					args=(scope, widget_key),
					key=widget_key,
					)

	scope_dvd_season_list(scope)


def set_dvd_doctor(scope, widget_key):
	selected_doctor = (scope[widget_key])
	scope.dvd_selected_doctor = selected_doctor
	set_dvds_to_display(scope)




