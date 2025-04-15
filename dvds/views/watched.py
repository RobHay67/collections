import logging
import streamlit as st


def checkbox_watched(scope, index_no, previous_selection):
	logging.partial(f"checkbox_watched {index_no=} {previous_selection=}")
	widget_key = 'widget_checkbox_watched_' + str(index_no)

	st.checkbox(
				label='Watched',
				value=previous_selection,
				key=widget_key,
				on_change=clicked_watched,
				args=(scope, index_no, widget_key)
				)


def clicked_watched(scope, index_no, widget_key):
	logging.warning(f"clicked_watched {index_no=} {widget_key=}")
	changed_value = scope[widget_key]
	scope.dvds_file.at[index_no, 'watched'] = changed_value