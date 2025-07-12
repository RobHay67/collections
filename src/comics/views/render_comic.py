import logging
import streamlit as st
from comics.views.collected import collected_comic_checkbox


def render_comic(scope, comic_index_list, count):
	logging.trace(f"render_comic {count=}")

	if count < len(comic_index_list):
		index_no = comic_index_list[count]

		issue_no = str(scope.comics_page_df._get_value(index_no, 'issue_no'))
		title = str(scope.comics_page_df._get_value(index_no, 'title'))
		note = str(scope.comics_page_df._get_value(index_no, 'notes'))
		collected = scope.comics_page_df._get_value(index_no, 'collected')
		if title == 'nan': title = 'Missing Title for this Issue'
		comic_cover = scope.comics_page_covers[index_no]

		st.header(issue_no)
		collected_comic_checkbox(scope, index_no, collected)
		st.image(comic_cover, caption=title)
		if note != 'nan':st.caption(note)



