
import streamlit as st

from dvds.display import set_dvds_to_display


def missing_dvd_eps_button(scope):

	widget_label = 'dvd_missing_eps_button'

	if scope.dvd_selected_missing_eps_only == True:
		button_type = "primary"
		button_label = "Show All Episodes"
	else :
		button_type = "secondary"
		button_label = "Show All Episodes yet to be collected"


	st.button(
				label = button_label,
				use_container_width=True,
				type=button_type,
				on_click=set_missing_eps,
				args=(scope, widget_label),
				key=widget_label,
				)


def set_missing_eps(scope, widget_label):

	if scope.dvd_selected_missing_eps_only == True:
		scope.dvd_selected_missing_eps_only = False
	else:
		scope.dvd_selected_missing_eps_only = True

	set_dvds_to_display(scope)
