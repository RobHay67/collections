
from comics.model.load import load_comic_file

from comics.model.series import create_comic_df

def scope_comics(scope):


	load_comic_file(scope)


	scope.comic_series_list = list(scope.comic_file['series'].unique())
	scope.comic_selected_series = scope.comic_series_list[0]
	scope.comic_selected_volume = 1
	scope.comic_df = {}
	scope.comic_covers = {}
	create_comic_df(scope)

	# scope.loaded_comics = False				# set default status as have not loaded the data at this stage
