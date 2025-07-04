import logging
import streamlit as st
from dvds.views.collected import checkbox_collected
from dvds.views.watched import checkbox_watched


def render_dvd(scope, dvd_index_list, count):
	logging.partial(f"render_dvd {count=}")

	if count < len(dvd_index_list):
		index_no = dvd_index_list[count]
		logging.debug(f"{index_no=}")
		season_no = str(scope.dvds_page_df._get_value(index_no, 'season'))
		story_no = str(scope.dvds_page_df._get_value(index_no, 'story'))
		title = str(scope.dvds_page_df._get_value(index_no, 'title'))
		url = str(scope.dvds_page_df._get_value(index_no, 'url'))
		collected = scope.dvds_page_df._get_value(index_no, 'collected')
		watched = scope.dvds_page_df._get_value(index_no, 'watched')
		if title == 'nan': title = 'Missing Title for this Issue'

		checkbox_collected(scope, index_no, collected)
		checkbox_watched(scope, index_no, watched)
		if scope.dvds_selected_missing_eps_only:
			st.caption('Season ' + season_no)
		
		# Render the DVD Cover - if we have one
		if index_no in scope.dvds_page_covers.keys():
			dvd_cover = scope.dvds_page_covers[index_no]
			st.image(dvd_cover, caption=title, use_container_width=True)
		st.write(title)
		st.caption('Story ' + story_no + ' - index ' + str(index_no))
		st.write(url)




	

