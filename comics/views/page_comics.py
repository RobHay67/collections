import logging
import streamlit as st
from comics.views.header import page_header_comics
from comics.views.render_comic import render_comic


# Page Configuration
scope = st.session_state
page = 'comics'
scope.display_page = page
logging.render(f"NAVIGATE {page=}")

st.title('Comic Collection')

page_header_comics(scope)

if scope.comics_selected_series != None:
	# sort the comics_df by issue_no
	scope.comics_page_df.sort_values(by='issue_no')
	no_of_comics = len(scope.comics_page_df)
	comic_index_list = list(scope.comics_page_df.index.values)

	for count in range(0, no_of_comics, 4):
		col1,col2,col3,col4=st.columns([2,2,2,2])
		with col1: render_comic(scope, comic_index_list, count+0)
		with col2: render_comic(scope, comic_index_list, count+1)
		with col3: render_comic(scope, comic_index_list, count+2)
		with col4: render_comic(scope, comic_index_list, count+3)

	st.write(scope.comics_page_df)






