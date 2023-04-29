
import streamlit as st

from pages.widgets.dvd_collected import collected_dvd_checkbox


def render_dvd(scope, no_of_dvds, i):

	if i < no_of_dvds:
		
		index_no = scope.dvd_index_list[i]
		season_no = str(scope.dvd_seasons_list[i])
		story_no = str(scope.dvd_story_list[i])
		title = str(scope.dvd_title_list[i])
		url = scope.dvd_url_list[i]
		collected = scope.dvd_collected_list[i]

		if title == 'nan': title = 'Missing Title for this Issue'

		collected_dvd_checkbox(scope, index_no, collected)

		if scope.dvd_selected_missing_eps_only:
			st.caption('Season ' + season_no)

		# Render the DVD Cover - if we have one
		if index_no in scope.dvd_covers.keys():
			dvd_cover = scope.dvd_covers[index_no]
			st.image(dvd_cover, caption=title, use_column_width=True)
		
		st.write(title)

		st.caption('Story ' + story_no + ' - index ' + str(index_no))
		st.write(url)




	

