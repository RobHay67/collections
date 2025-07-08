import logging
import streamlit as st


from dvds.model.save import save_dvd_file



def button_save_dvds(scope):
	logging.trace(f"dvd_save_button")
	st.button(
		label='Save Changes to DVDs File', 
		key='widget_save_dvds',
		use_container_width=True,
		on_click=clicked_save_dvd_file,
		args=(scope, ),
		)


def clicked_save_dvd_file(scope):
	logging.warning(f"dvd_save_file")
	save_dvd_file(scope)