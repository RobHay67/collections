import logging
import streamlit as st
from dvds.scope.scope_list_of_seasons import scope_list_of_seasons
from dvds.scope.scope_page_df import scope_dvds_to_display
from dvds.scope.scope_page_covers import scope_dvd_covers_for_page


def selectbox_series(scope):
	logging.partial(f"dvd_series_selectbox")
	widget_key = 'widget_dvd_series'
	previous_selection = scope.dvds_selected_series


	pos_for_previous = scope.dvds_list_of_series.index(previous_selection)	

	st.selectbox(
					label='Choose DVD Series',
					options=scope.dvds_list_of_series,
					index=pos_for_previous,
					on_change=change_series,
					args=(scope, widget_key),
					key=widget_key,
					label_visibility='collapsed',
					)
	

def change_series(scope, widget_key):
	logging.warning(f"change_series {widget_key=}")
	selected_series = (scope[widget_key])
	scope.dvds_selected_series = selected_series
	scope.dvds_list_of_seasons = scope_list_of_seasons(scope)
	# Update Page Data
	scope.dvds_page_df = scope_dvds_to_display(scope)
	scope.dvds_page_covers = scope_dvd_covers_for_page(scope)