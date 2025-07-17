import logging


def scope_list_of_seasons(scope):
	series = scope.dvds_selected_series
	logging.warning(f"scope_list_of_seasons {series=}")
	
	# filter dvds to the selected series
	dvd_df = scope.dvds_file[scope.dvds_file['series'] == series]

	# list of unique seasons in the dvd series
	season_list = list(dvd_df['season'].unique())
	season_list.insert(0, 'All Seasons')
	
	return season_list

		