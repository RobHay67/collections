import logging
import streamlit as st
from comics.scope.scope_page_df import scope_comic_df_for_page
from comics.scope.scope_page_covers import scope_comic_covers_for_page


def button_missing_comics_only(scope):
	logging.trace(f"button_missing_comics_only")
	widget_label = 'comics_missing_eps_button'

	if scope.comics_selected_missing_only == True:
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
	if scope.comics_selected_missing_only == True:
		scope.comics_selected_missing_only = False
	else:
		scope.comics_selected_missing_only = True

	# Update Page Data
	scope.comics_page_df = scope_comic_df_for_page(scope)
	scope.comics_page_covers = scope_comic_covers_for_page(scope)
