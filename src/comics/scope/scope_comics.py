import logging
from comics.model.load_file import load_comic_file


def scope_comics(scope):
	logging.warning("scope_comics")

	scope.comics_file = load_comic_file(scope)
	scope.comics_list_of_series = list(scope.comics_file['series'].unique())
	scope.comics_selected_series = None					# Comic Series to display
	scope.comics_selected_missing_only = False
	scope.comics_page_df = {}							# Comics to display
	scope.comics_page_covers = {}						# store the images for the selected comics

