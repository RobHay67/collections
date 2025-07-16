import logging
import streamlit as st

from comics.model import Comic

def collected_comic_checkbox(comic, index_no):
	logging.trace("collected_comic_checkbox")
	widget_key 	= 'widget_comic_collected_' + str(index_no)
	
	# comic 		= Comic.get_by_index(index_no)

	st.checkbox(
				label		= "Collected",
				value		= comic.collected,
				key			= widget_key,
				on_change	= update_collected,
				args		= (comic, widget_key)
				)


def update_collected(comic, widget_key):
	logging.warning(f"update_collected {widget_key=}")
	comic.collected = st.session_state[widget_key]
	Comic.count_page_objects()



