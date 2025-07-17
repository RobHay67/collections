import logging
import streamlit as st

from dvds.model import Dvd

def checkbox_collected(dvd, index_no):
	logging.trace(f"checkbox_collected {index_no=}")
	widget_key = 'widget_checkbox_collected_' + str(index_no)

	st.checkbox(
				label		= 'Collected',
				value		= dvd.collected,
				key			= widget_key,
				on_change	= clicked_collected,
				args		= (dvd, widget_key)
				)


def clicked_collected(dvd, widget_key):
	logging.warning(f"clicked_collected {widget_key=}")
	print(st.session_state[widget_key])
	dvd.collected = st.session_state[widget_key]
	Dvd.count_page_objects()
