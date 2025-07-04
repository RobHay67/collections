import logging
import os
from PIL import Image
from files.scope_files_and_folders import path_dvd_cover


def scope_dvd_covers_for_page(scope):
	logging.warning(f"scope_dvd_covers_for_page")
	dvd_covers = {}
	missing_cover_image = image = Image.open(scope.file_path_dvds_missing_cover)

	for index, row in scope.dvds_page_df.iterrows():
		cover_number = row['cover']
		path_to_dvd_cover = path_dvd_cover(scope, cover_number)
		logging.debug(f"{index=} {cover_number=} {path_to_dvd_cover=}")	
		image = Image.open(path_to_dvd_cover) if os.path.isfile(path_to_dvd_cover) else missing_cover_image
		dvd_covers[index] = image

	return dvd_covers