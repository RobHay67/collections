import logging
import streamlit as st

# from dvds.model import Dvd

def checkbox_available(dvd, index_no):
	logging.trace(f"checkbox_available {index_no=}")
	widget_key = 'widget_checkbox_available_' + str(index_no)

	st.checkbox(
				label		= 'Available',
				value		= dvd.available,
				key			= widget_key,
				# on_change	= clicked_available,
				# args		= (dvd, widget_key)
				)


# def clicked_available(dvd, widget_key):
# 	logging.warning(f"clicked_watched {widget_key=}")
# 	dvd.watched = st.session_state[widget_key]
