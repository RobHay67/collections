

import streamlit as st

from dvds.model.load import load_dvd_covers_for_series
# from dvds.config import scope_dvd_season_list


# index,series,season,story,title,doctor,image,url


# ---------------------------------------------------
# DVD - Series
# ---------------------------------------------------
def dvd_selector_series(scope):

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
	refresh_dvd_covers(scope)


# ---------------------------------------------------
# DVD - Season
# ---------------------------------------------------
def dvd_selector_season(scope):

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
	refresh_dvd_covers(scope)


def scope_dvd_season_list(scope):

	series = scope.dvd_selected_series
	dvd_df = scope.dvds_file[scope.dvds_file['series'] == series]
	scope.dvd_season_list = list(dvd_df['season'].unique())

	# Add special selector for Doctor Who
	
	default_doctor = 'All Doctors'
	scope.dvd_doctor_list = []
	
	if series == 'Doctor Who':		
		dvd_doctor_list = list(dvd_df['doctor'].unique())
		dvd_doctor_list.insert(0, default_doctor)
		scope.dvd_doctor_list = dvd_doctor_list
# ---------------------------------------------------
# DVD - Select by Doctor for Doctor Who Series
# ---------------------------------------------------
def dvd_selector_doctor(scope):
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
	print(selected_doctor)
	scope.dvd_selected_doctor = selected_doctor
	refresh_dvd_covers(scope)



# ---------------------------------------------------
# DVD - Create a dataframe of the seasons for this series
# ---------------------------------------------------

def refresh_dvd_covers(scope):

	dvd_df = scope.dvds_file

	# Filter to series
	dvd_df = dvd_df[dvd_df['series'] == scope.dvd_selected_series]

	# Special filter for Doctor Who
	if scope.dvd_selected_doctor == 'All Doctors': # this is the default
		dvd_df = dvd_df[dvd_df['season'] == scope.dvd_selected_season]
	else:
		# select by doctor
		dvd_df = dvd_df[dvd_df['doctor'] == scope.dvd_selected_doctor]

	scope.dvd_df = dvd_df
	scope.dvd_df.sort_values(by='story', inplace=True)
	
	scope.dvd_index_list = list(scope.dvd_df.index.values)
	scope.dvd_story_list = list(scope.dvd_df['story'])
	scope.dvd_title_list = list(scope.dvd_df['title'])
	scope.dvd_url_list = list(scope.dvd_df['url'])
	scope.dvd_collected_list = list(scope.dvd_df['collected'])
	


# ---------------------------------------------------
# DVD - Season List
# ---------------------------------------------------


	
		

