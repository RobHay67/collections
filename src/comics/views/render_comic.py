import logging
import streamlit as st

from comics.model import Comic
from comics.views.collected import collected_comic_checkbox


def render_comic(scope, list_pos):
	logging.trace(f"render_comic {list_pos=}")
	
	if list_pos < Comic.page_qty:
		comic		= Comic.page_comics[list_pos]
		comic_cover = Comic.page_covers[list_pos]
		index_no	= comic.index

		st.header(comic.issue_no)
		collected_comic_checkbox(comic, index_no)
		st.image(comic_cover, caption=comic.title)
		if comic.notes is not None:
			st.caption(comic.notes)
