



def set_dvds_to_display(scope):

	dvd_df = scope.dvd_file.copy()

	# Filter to selected series
	dvd_df = dvd_df[dvd_df['series'] == scope.dvd_selected_series]


	if scope.dvd_selected_missing_eps_only == True:
		# Show only DVDs that I am yet to collected (missing episodes)
		dvd_df = dvd_df[dvd_df['collected'] == False]

	else:
		# Filter to the Selected Season
		if scope.dvd_selected_doctor == 'All Doctors':
			dvd_df = dvd_df[dvd_df['season'] == scope.dvd_selected_season]
		
		if scope.dvd_selected_doctor != 'All Doctors':
			# Special Selector for Doctor Who -  Select by doctor instead of Season
			dvd_df = dvd_df[dvd_df['doctor'] == scope.dvd_selected_doctor]

	# print(len(dvd_df))
	# Store DVDs re

	scope.dvd_df = dvd_df
	scope.dvd_df.sort_values(by=['season','story'], inplace=True)
	
	scope.dvd_index_list = list(scope.dvd_df.index.values)
	scope.dvd_seasons_list = list(scope.dvd_df['season'])
	scope.dvd_story_list = list(scope.dvd_df['story'])
	scope.dvd_title_list = list(scope.dvd_df['title'])
	scope.dvd_url_list = list(scope.dvd_df['url'])
	scope.dvd_collected_list = list(scope.dvd_df['collected'])