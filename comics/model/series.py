

import streamlit as st

from comics.model.load import load_comic_covers


def set_comic_series(scope, widget_key):
	# comics_file is the master list of comics
	selected_series = (scope[widget_key])

	scope.comics_selected_series = selected_series
	
	# this currently defaults to vol 1
	# scope.comics_selected_volume = 

	create_comic_df(scope)
	


def create_comic_df(scope):

	comic_df = scope.comics_file
	
	selected_series = scope.comics_selected_series
	
	scope.comic_df = comic_df[comic_df['series'] == selected_series]

	load_comic_covers(scope)






def series_selector(scope):

	widget_key = 'widget_comic_series'
	previous_selection = scope.comics_selected_series
	pos_for_previous = scope.comic_series_list.index(previous_selection)	

	st.selectbox(
					label='Choose Comic Series',
					options=scope.comic_series_list,
					index=pos_for_previous,
					on_change=set_comic_series,
					args=(scope, widget_key),
					key=widget_key,
					)


	