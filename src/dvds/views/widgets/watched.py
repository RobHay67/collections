import logging
import streamlit as st

# from dvds.model import Dvd

def checkbox_watched(dvd, index_no):
	logging.trace(f"checkbox_watched {index_no=}")
	widget_key = 'widget_checkbox_watched_' + str(index_no)

	st.checkbox(
				label		= 'Watched',
				value		= dvd.watched,
				key			= widget_key,
				on_change	= clicked_watched,
				args		= (dvd, widget_key)
				)


def clicked_watched(dvd, widget_key):
	logging.warning(f"clicked_watched {widget_key=}")
	dvd.watched = st.session_state[widget_key]
	# Dvd.count_page_objects()
