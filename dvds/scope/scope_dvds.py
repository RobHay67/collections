import logging
from dvds.model.load_file import load_dvd_file
from dvds.scope.scope_list_of_doctors import scope_list_of_doctors
from dvds.scope.scope_list_of_seasons import scope_list_of_seasons
from dvds.scope.scope_page_df import scope_dvds_to_display
from dvds.scope.scope_page_covers import scope_dvd_covers_for_page




def scope_dvds(scope):
	logging.warning(f"scope_dvds")
	
	scope.dvds_file = load_dvd_file(scope)
	scope.dvds_list_of_series = list(scope.dvds_file['series'].unique())
	
	# These are defaulted to Doctor Who as that is the only series that is
	# currently being collected. We can change this to None later if we
	# decide to collect additional series
	scope.dvds_selected_series = 'Doctor Who'
	scope.dvds_selected_season = 'All Seasons'
	scope.dvds_selected_doctor = 'All Doctors'
	scope.dvds_selected_missing_eps_only = False
	
	scope.dvds_page_df = {}							# DvDs to display
	scope.dvds_page_covers = {}						# store the images for the selected DvDs

	# Special for Doctor Who
	scope.dvds_list_of_doctors_for_who = scope_list_of_doctors(scope)

	# Special as we have already selected the series to display
	# remove this later if there are multiple series
	scope.dvds_list_of_seasons = scope_list_of_seasons(scope)
	
	# Store data to display (as above, because we set defaults)
	scope.dvds_page_df = scope_dvds_to_display(scope)
	scope.dvds_page_covers = scope_dvd_covers_for_page(scope)




