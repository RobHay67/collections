import logging
import streamlit as st
from comics.scope.scope_page_df import scope_comic_df_for_page
from comics.scope.scope_page_covers import scope_comic_covers_for_page

def selectbox_series(scope):
	logging.partial(f"selectbox_series")
	widget_key = 'widget_selectbox_series'
	previous_selection = scope.comics_selected_series
	
	if previous_selection != None:
		pos_for_previous = scope.comics_list_of_series.index(previous_selection)	
	else: 
		pos_for_previous = None

	st.selectbox(
					label='Choose Comic Series',
					options=scope.comics_list_of_series,
					index=pos_for_previous,
					on_change=change_comic_series,
					args=(scope, widget_key),
					key=widget_key,
					)
	

def change_comic_series(scope, widget_key):
	logging.warning(f"change_comic_series {widget_key=}")
	selected_series = (scope[widget_key])
	scope.comics_selected_series = selected_series
	# Update Page Data
	scope.comics_page_df = scope_comic_df_for_page(scope)
	scope.comics_page_covers = scope_comic_covers_for_page(scope)
