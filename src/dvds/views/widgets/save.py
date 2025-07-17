import logging
import streamlit as st
from dvds.model import Dvd


def button_save_dvds():
	logging.trace("dvd_save_button")
	st.button(
		label				='Save Changes to DVDs File', 
		key					='widget_save_dvds',
		use_container_width	=True,
		on_click			=clicked_save_dvd_file,
		)


def clicked_save_dvd_file():
	logging.warning("dvd_save_file")
	Dvd.save_dvds()