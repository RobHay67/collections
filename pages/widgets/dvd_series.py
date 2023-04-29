import streamlit as st


from dvds.config import set_dvds_to_display
from dvds.load import load_dvd_covers_for_series



def dvd_series_selectbox(scope):

	widget_key = 'widget_dvd_series'
	previous_selection = scope.dvd_selected_series
	pos_for_previous = scope.dvd_series_list.index(previous_selection)	

	st.selectbox(
					label='Choose DVD Series',
					options=scope.dvd_series_list,
					index=pos_for_previous,
					on_change=set_dvd_series,
					args=(scope, widget_key),
					key=widget_key,
					)
	

def set_dvd_series(scope, widget_key):
	selected_series = (scope[widget_key])
	scope.dvd_selected_series = selected_series

	load_dvd_covers_for_series(scope)
	set_dvds_to_display(scope)