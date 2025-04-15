import logging
from PIL import Image
from files.scope_files_and_folders import path_comic_cover


def scope_comic_covers_for_page(scope):
	logging.warning("scope_comic_covers_for_page")
	comics_covers = {}

	for index, row in scope.comics_page_df.iterrows():
		series = row['series']
		volume = row['volume']
		issue_no = row['issue_no']
		path_to_comic_cover = path_comic_cover(scope, series, volume, issue_no)
		image = Image.open(path_to_comic_cover)
		comics_covers[index] = image

	return comics_covers


