

# index,series,season,story,title,doctor,image,url

from dvds.load import load_dvd_file
from dvds.load import load_dvd_covers_for_series
from dvds.display import set_dvds_to_display



def scope_dvds(scope):

	load_dvd_file(scope)

	scope.dvd_series_list = list(scope.dvd_file['series'].unique())
	scope.dvd_selected_series = 'Doctor Who'
	scope.dvd_selected_season = 1
	
	scope_dvd_season_list(scope)

	scope.dvd_selected_doctor = 'All Doctors'
	scope.dvd_selected_missing_eps_only = False
	scope.dvd_df = {}
	scope.dvd_covers = {}
	load_dvd_covers_for_series(scope)
	set_dvds_to_display(scope)


def scope_dvd_season_list(scope):

	series = scope.dvd_selected_series

	# filter dvds to the selected series
	dvd_df = scope.dvd_file[scope.dvd_file['series'] == series]

	# list of unique seasons in the dvd series
	season_list = list(dvd_df['season'].unique())    
	scope.dvd_season_list = season_list

	# Add special selector for Doctor Who	
	default_doctor = 'All Doctors'
	scope.dvd_doctor_list = []
	
	if series == 'Doctor Who':		
		dvd_doctor_list = list(dvd_df['doctor'].unique())
		dvd_doctor_list.insert(0, default_doctor)
		scope.dvd_doctor_list = dvd_doctor_list


