import logging
import streamlit as st


def collected_comic_checkbox(scope, index_no, collected):
	logging.partial(f"collected_comic_checkbox {index_no=} {collected=}")
	widget_key = 'widget_comic_collected_' + str(index_no)

	st.checkbox(
				label='Collected',
				value=collected,
				key=widget_key,
				on_change=update_collected,
				args=(scope, index_no, widget_key)
				)


def update_collected(scope, index_no, widget_key):
	logging.warning(f"update_collected {index_no=} {widget_key=}")
	changed_value = scope[widget_key]
	scope.comics_file.at[index_no, 'collected'] = changed_value



