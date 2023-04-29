
import streamlit as st

from pages.widgets.dvd_series import dvd_series_selectbox
from pages.widgets.dvd_season import dvd_season_selectbox
from pages.widgets.dvd_doctor import dvd_doctor_selectbox
from pages.widgets.save_dvd import dvd_save_button
from pages.widgets.dvd_missing_eps import missing_dvd_eps_button


def render_dvd_header(scope):

	col1,col2,col3=st.columns([5,3,3])

	with col1: 
		dvd_series_selectbox(scope)
	
		subcol1, subcol2 = col1.columns(2)

		with subcol2:
			if scope.dvd_selected_doctor == 'All Doctors': # this is the default
				dvd_season_selectbox(scope)
			else:
				st.write('Showing All seasons for ' + scope.dvd_selected_doctor)
	
		with subcol1:
			if scope.dvd_selected_series == 'Doctor Who':
				dvd_doctor_selectbox(scope)

	with col3:
		dvd_save_button(scope)
		no_collected = scope.dvd_df['collected'].sum()
		available_to_collect = len(scope.dvd_df)
		
		st.write('Available to collect = ', available_to_collect)
		st.write('Number Collected = ', no_collected)

		missing_dvd_eps_button(scope)