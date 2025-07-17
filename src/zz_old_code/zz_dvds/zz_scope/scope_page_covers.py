import logging
import os
from PIL import Image
from files.scope_files_and_folders import path_dvd_cover

from dvds.model import Dvd


def scope_dvd_covers_for_page(scope):
	logging.warning("scope_dvd_covers_for_page")
	dvd_covers = {}
	missing_cover_image = image = Image.open(Dvd._path_dvds_covers_missing)

	for index, row in scope.dvds_page_df.iterrows():
		cover_number = row['cover']
		path_to_dvd_cover = path_dvd_cover(scope, cover_number)
		# logging.debug(f"{index=} {cover_number=} {path_to_dvd_cover=}")	
		image = Image.open(path_to_dvd_cover) if os.path.isfile(path_to_dvd_cover) else missing_cover_image
		dvd_covers[index] = image

	return dvd_covers