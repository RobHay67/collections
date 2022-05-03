

import streamlit as st

from dvds.model.load import load_dvd_covers_for_series


def set_dvd_series(scope, widget_key):
	# dvds_file is the master list of dvds
	selected_series = (scope[widget_key])

	scope.dvd_series_selected = selected_series
	
	create_dvds_df(scope)
	


def create_dvds_df(scope):

	dvd_df = scope.dvds_file
	
	selected_series = scope.dvd_series_selected
	
	scope.dvd_df = dvd_df[dvd_df['series'] == selected_series]

	load_dvd_covers_for_series(scope)






def dvd_series_selector(scope):

	widget_key = 'widget_dvd_series'
	previous_selection = scope.dvd_series_selected
	pos_for_previous = scope.dvd_series_list.index(previous_selection)	

	st.selectbox(
					label='Choose DVD Series',
					options=scope.dvd_series_list,
					index=pos_for_previous,
					on_change=set_dvd_series,
					args=(scope, widget_key),
					key=widget_key,
					)


	