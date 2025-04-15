import logging
import streamlit as st


# ignore_keys = ['comic_file', 'comic_df', 'comic_covers', 'dvd_file', 'dvd_df', 'dvd_covers']


def print_scope_keys(location=' unspecified location',hide_widgets=True):
	logging.debug("print_scope_keys")
	print('\033[92m')
	print('='*66)
	print('Called From    > ', location)
	print('Hiding Widgets > ', hide_widgets)
	print('-'*66)
	counter = 0; widgets = 0
	for key in sorted(st.session_state):
		if key[:6] == 'widget':
			widgets+=1
			if hide_widgets==False:print(widgets, key)
		else:
			counter+=1
			print(counter, key)
	print('-'*66)
	print('Total Scope Keys   = ', counter)
	print('Total Widgets Keys = ', widgets)
	print('='*66)
	print('\033[0m')




