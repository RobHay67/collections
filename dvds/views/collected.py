import logging
import streamlit as st


def checkbox_collected(scope, index_no, previous_selection):
	logging.partial(f"checkbox_collected {index_no=} {previous_selection=}")
	widget_key = 'widget_checkbox_collected_' + str(index_no)

	st.checkbox(
				label='Collected',
				value=previous_selection,
				key=widget_key,
				on_change=clicked_collected,
				args=(scope, index_no, widget_key)
				)


def clicked_collected(scope, index_no, widget_key):
	logging.warning(f"clicked_collected {index_no=} {widget_key=}")
	changed_value = scope[widget_key]
	scope.dvds_file.at[index_no, 'collected'] = changed_value