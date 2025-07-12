import logging
import streamlit as st
from dvds.scope.scope_page_df import scope_dvds_to_display
from dvds.scope.scope_page_covers import scope_dvd_covers_for_page


def selectbox_dvd_season(scope):
	logging.trace(f"selectbox_dvd_season")
	widget_key = 'widget_dvd_season'
	previous_selection = scope.dvds_selected_season

	pos_for_previous = scope.dvds_list_of_seasons.index(previous_selection)	

	st.selectbox(
					label='Select Seasons for Doctor Who',
					options=scope.dvds_list_of_seasons,
					index=pos_for_previous,
					on_change=change_season,
					args=(scope, widget_key),
					key=widget_key,
					)


def change_season(scope, widget_key):
	logging.warning(f"change_season {widget_key=}")
	selected_season = (scope[widget_key])
	scope.dvds_selected_season = selected_season
	# Update Page Data
	scope.dvds_page_df = scope_dvds_to_display(scope)
	scope.dvds_page_covers = scope_dvd_covers_for_page(scope)
	



