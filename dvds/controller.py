import streamlit as st

from dvds.model.series import dvd_series_selector


def render_dvd_details(scope, i):
	
	story_no = str(scope.dvd_story_list[i])
	title = str(scope.dvd_title_list[i])
	# note = str(scope.comic_notes_list[i])

	if title == 'nan': title = 'Missing Title for this Issue'
	# if note == 'nan': title = ''

	dvd_cover = scope.dvd_covers[story_no]

	st.header(story_no)

	# widget_collected(scope, i)



	st.image(dvd_cover, caption=title)
	# if note != 'nan':
	# 	st.caption(note)






def render_dvds_page(scope):

	st.title('DVD Collection')

	col1,col2,col3,col4=st.columns([4,3,3,4])

	with col1: dvd_series_selector(scope)
	with col2: st.write('Doctor Selector')
	with col3: st.write('Season Selector')

	scope.dvd_df.sort_values(by='story')
	no_of_dvds = len(scope.dvd_df)
	
	scope.dvd_story_list = list(scope.dvd_df['story'])
	scope.dvd_title_list = list(scope.dvd_df['title'])
	# scope.dvd_notes_list = list(scope.comic_df['notes'])


	# for i in range(0, no_of_dvds, 8):
	# 	col1,col2,col3,col4,col5,col6,col7,col8=st.columns([2,2,2,2,2,2,2,2])
	# 	with col1: render_dvd_details(scope, i+0)
	# 	with col2: render_dvd_details(scope, i+1)
	# 	with col3: render_dvd_details(scope, i+2)
	# 	with col4: render_dvd_details(scope, i+3)
	# 	with col5: render_dvd_details(scope, i+4)
	# 	with col6: render_dvd_details(scope, i+5)
	# 	with col7: render_dvd_details(scope, i+6)
	# 	with col8: render_dvd_details(scope, i+7)





