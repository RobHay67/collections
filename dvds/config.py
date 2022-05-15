

# index,series,season,story,title,doctor,image,url

from dvds.model.load import load_dvds_file
from dvds.model.selectors import refresh_dvd_covers
from dvds.model.selectors import scope_dvd_season_list
from dvds.model.load import load_dvd_covers_for_series




def scope_dvds(scope):

	load_dvds_file(scope)

	scope.dvd_series_list = list(scope.dvds_file['series'].unique())
	scope.dvd_selected_series = 'Doctor Who'
	scope.dvd_selected_season = 1
	
	scope_dvd_season_list(scope)

	scope.dvd_selected_doctor = 'All Doctors'
	scope.dvd_show_only_missing_eps = False
	scope.dvd_df = {}
	scope.dvd_covers = {}
	load_dvd_covers_for_series(scope)
	refresh_dvd_covers(scope)




