import streamlit as st

from dvds.model.save import save_dvds_file
from dvds.model.selectors import dvd_selector_series
from dvds.model.selectors import dvd_selector_season
from dvds.model.selectors import dvd_selector_doctor
from dvds.model.selectors import dvd_selector_missing_episodes

def render_dvds_page(scope):
	col1,col2=st.columns([8,2])
	with col1:
		st.title('DVD Collection')
	with col2:
		save_dvd_file = st.button('Save DVDs File')

	if save_dvd_file: save_dvds_file(scope)

	render_selectors(scope)

	no_of_dvds = len(scope.dvd_story_list)

	for i in range(0, no_of_dvds, 8):
		col1,col2,col3,col4,col5,col6,col7,col8=st.columns([2,2,2,2,2,2,2,2])
		with col1: render_dvd_details(scope, no_of_dvds, i+0)
		with col2: render_dvd_details(scope, no_of_dvds, i+1)
		with col3: render_dvd_details(scope, no_of_dvds, i+2)
		with col4: render_dvd_details(scope, no_of_dvds, i+3)
		with col5: render_dvd_details(scope, no_of_dvds, i+4)
		with col6: render_dvd_details(scope, no_of_dvds, i+5)
		with col7: render_dvd_details(scope, no_of_dvds, i+6)
		with col8: render_dvd_details(scope, no_of_dvds, i+7)



def render_selectors(scope):
	col1,col2,col3,col4=st.columns([4,3,3,4])

	with col1: 
		dvd_selector_series(scope)
	
	# with col2:
		if scope.dvd_selected_doctor == 'All Doctors': # this is the default
			print(scope.dvd_selected_doctor)
			dvd_selector_season(scope)
		else:
			st.write('Showing All seasons for ' + scope.dvd_selected_doctor)
	
		if scope.dvd_selected_series == 'Doctor Who':
		# with col3: 
			dvd_selector_doctor(scope)

	with col4:
		no_collected = scope.dvd_df['collected'].sum()
		available_to_collect = len(scope.dvd_df)
		
		st.write('Available to collect = ', available_to_collect)
		st.write('Number Collected = ', no_collected)

		dvd_selector_missing_episodes(scope)


def render_dvd_details(scope, no_of_dvds, i):

	if i < no_of_dvds:
		
		index_no = scope.dvd_index_list[i]
		season_no = str(scope.dvd_seasons_list[i])
		story_no = str(scope.dvd_story_list[i])
		title = str(scope.dvd_title_list[i])
		url = scope.dvd_url_list[i]
		collected = scope.dvd_collected_list[i]

		if title == 'nan': title = 'Missing Title for this Issue'

		widget_collected(scope, index_no, collected)

		if scope.dvd_show_only_missing_eps:
			st.caption('Season ' + season_no)

		# Render the DVD Cover - if we have one
		if index_no in scope.dvd_covers.keys():
			dvd_cover = scope.dvd_covers[index_no]
			st.image(dvd_cover, caption=title)
		
		st.write(title)

		st.caption('Story ' + story_no + ' - index ' + str(index_no))
		# st.write(url)


def widget_collected(scope, index_no, previous_selection):

	widget_key = 'widget_collected_' + str(index_no)

	st.checkbox(
				label='Collected',
				value=previous_selection,
				key=widget_key,
				on_change=update_collected,
				args=(scope, index_no, widget_key)
				)


def update_collected(scope, index_no, widget_key):

	# index_no = int(index_no)
	changed_value = scope[widget_key]
	
	# store the selection
	scope.dvds_file.at[index_no, 'collected'] = changed_value
