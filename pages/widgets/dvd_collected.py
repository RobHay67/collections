
import streamlit as st


def collected_dvd_checkbox(scope, index_no, previous_selection):

	widget_key = 'widget_dvd_collected_' + str(index_no)

	st.checkbox(
				label='Collected',
				value=previous_selection,
				key=widget_key,
				on_change=update_collected,
				args=(scope, index_no, widget_key)
				)
	


def update_collected(scope, index_no, widget_key):

	# index_no = int(index_no)
	changed_value = scope[widget_key]
	
	# store the selection
	scope.dvd_file.at[index_no, 'collected'] = changed_value