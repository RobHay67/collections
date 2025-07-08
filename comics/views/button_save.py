import logging
import streamlit as st

from comics.model.save import save_comic_file


def button_save_comics(scope):
	logging.trace("button_save_comics")

	st.button(
		label='Save Changes to Comics File', 
		key='widget_save_comics',
		use_container_width=True,
		on_click=clicked_save_comics_button,
		args=(scope, ),
		)


def clicked_save_comics_button(scope):
	logging.warning("clicked_save_button")
	save_comic_file(scope)
