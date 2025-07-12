import logging


def scope_dvds_to_display(scope):
	series = scope.dvds_selected_series
	season = scope.dvds_selected_season
	doctor = scope.dvds_selected_doctor
	missing_only = scope.dvds_selected_missing_eps_only
	logging.warning(f"scope_dvds_to_display {series=} {season=} {doctor=}")
	
	# Filet to selected series
	dvds_page_df = scope.dvds_file.copy()
	dvds_page_df = dvds_page_df[dvds_page_df['series'] == series]

	# Filter to selected season
	if season != 'All Seasons':
		dvds_page_df = dvds_page_df[dvds_page_df['season'] == season]

	# Filter to a selected Doctor
	if doctor != 'All Doctors':
		dvds_page_df = dvds_page_df[dvds_page_df['doctor'] == doctor]

	# Filter to missing eps only if requested
	if missing_only == True:
		# Show only DVDs that HAVE NOT been collected (missing episodes)
		dvds_page_df = dvds_page_df[dvds_page_df['collected'] == False]

	# Sort
	# dvds_page_df.sort_values(by=['season','story'], inplace=True)
	dvds_page_df.sort_index(inplace=True)

	return dvds_page_df