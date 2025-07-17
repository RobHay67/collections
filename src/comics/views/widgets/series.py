import logging
import streamlit as st
from comics.model import Comic


def selectbox_series(scope):
	logging.trace("selectbox_series")
	widget_key = 'widget_selectbox_series'
	
	previous_selection = Comic.selected_series
	if previous_selection is not None:
		pos_for_previous = Comic.series_list.index(previous_selection)	
	else: 
		pos_for_previous = None

	st.selectbox(
					label		= 'Choose Comic Series',
					options		= Comic.series_list,
					index		= pos_for_previous,
					on_change	= change_comic_series,
					args		= (scope, widget_key),
					key			= widget_key,
					)
	

def change_comic_series(scope, widget_key):
	logging.warning(f"change_comic_series {widget_key=}")
	Comic.selected_series = (scope[widget_key])
	Comic.create_page_comics()
