
import streamlit as st

from dvds.config import scope_dvd_season_list
from dvds.config import set_dvds_to_display



def dvd_season_selectbox(scope):

	widget_key = 'widget_dvd_season'
	previous_selection = scope.dvd_selected_season

	pos_for_previous = scope.dvd_season_list.index(previous_selection)	

	st.selectbox(
					label='Available Seasons for ' + scope.dvd_selected_series,
					options=scope.dvd_season_list,
					index=pos_for_previous,
					on_change=set_dvd_season,
					args=(scope, widget_key),
					key=widget_key,
					)

	scope_dvd_season_list(scope)



def set_dvd_season(scope, widget_key):
	selected_season = (scope[widget_key])
	scope.dvd_selected_season = selected_season
	set_dvds_to_display(scope)



