



from dvds.model.load import load_dvds_file
from dvds.model.series import create_dvds_df




def scope_dvds(scope):



	load_dvds_file(scope)

	scope.dvd_series_list = list(scope.dvds_file['series'].unique())
	scope.dvd_series_selected = scope.dvd_series_list[0]

	scope.dvd_df = {}
	scope.dvd_covers = {}
	create_dvds_df(scope)
