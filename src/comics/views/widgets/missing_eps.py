import logging
import streamlit as st
from comics.model import Comic


def button_missing_comics_only(scope):
	logging.trace("button_missing_comics_only")
	widget_label = 'comics_missing_eps_button'

	if Comic.selected_missing_only:
	# if scope.comics_selected_missing_only == True:
		button_type = "primary"
		button_label = "Show All Comics"
	else :
		button_type = "secondary"
		button_label = "Show Missing Comics"

	st.button(
				label = button_label,
				use_container_width=True,
				type=button_type,
				on_click=change_show_missing_comics,
				args=(scope, widget_label),
				key=widget_label,
				)


def change_show_missing_comics(scope, widget_label):
	logging.warning(f"change_show_missing_comics {widget_label=}")
	if Comic.selected_missing_only:
		Comic.selected_missing_only = False
	else:
		Comic.selected_missing_only = True

	# Update Page Data
	Comic.create_page_comics()
