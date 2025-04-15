import logging
import streamlit as st
from dvds.scope.scope_page_df import scope_dvds_to_display
from dvds.scope.scope_page_covers import scope_dvd_covers_for_page


def button_missing_dvd_eps_only(scope):
	logging.partial(f"button_missing_dvd_eps_only")
	widget_label = 'dvd_missing_eps_button'

	if scope.dvds_selected_missing_eps_only == True:
		button_type = "primary"
		button_label = "Show All Episodes"
	else :
		button_type = "secondary"
		button_label = "Show Missing Episodes"

	st.button(
				label = button_label,
				use_container_width=True,
				type=button_type,
				on_click=change_show_missing_episodes,
				args=(scope, widget_label),
				key=widget_label,
				)


def change_show_missing_episodes(scope, widget_label):
	logging.warning(f"change_show_missing_episodes {widget_label=}")
	if scope.dvds_selected_missing_eps_only == True:
		scope.dvds_selected_missing_eps_only = False
	else:
		scope.dvds_selected_missing_eps_only = True

	# Update Page Data
	scope.dvds_page_df = scope_dvds_to_display(scope)
	scope.dvds_page_covers = scope_dvd_covers_for_page(scope)