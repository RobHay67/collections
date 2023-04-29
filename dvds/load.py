
import os
import pandas as pd
from PIL import Image

from dvds.schema import schema
from dvds.schema import csv_dates
from dvds.schema import csv_dtypes

from dvds.save import save_dvd_file
from files.config import path_dvd_cover



def load_dvd_file(scope):

	if os.path.exists( scope.dvd_file_path ):

		dvd_file = pd.read_csv(  scope.dvd_file_path, 
									index_col='index',
									dtype=csv_dtypes(schema),
									parse_dates=csv_dates(schema),
									)

	else: 
		dataframe_columns = []
		for column_name in schema: 
			dataframe_columns.append(column_name)
			
		dvd_file = pd.DataFrame(columns=dataframe_columns)

		save_dvd_file(scope)
		
	scope.dvd_file = dvd_file
		
		


def load_dvd_covers_for_series(scope):

	print('load all the dvd covers and store them for later usage')

	series = scope.dvd_selected_series

	# Filter to selected series
	# load_df = scope.dvd_df[scope.dvd_df['series']==series].copy()
	load_df = scope.dvd_file[scope.dvd_file['series']==series].copy()

	dvd_covers = {}
	missing_cover_image = image = Image.open(scope.dvd_file_path_missing_cover)

	# for story in story_list:
	for idx, row in load_df.iterrows():		
		image_exists = row['image']
		# for future - this should really reference the index for each 
		# series as other dvd collectons will also start at ep1
		path_to_dvd_cover = path_dvd_cover(scope, idx)

		if os.path.isfile(path_to_dvd_cover):
			image = Image.open(path_to_dvd_cover)
		else:
			image = missing_cover_image

		dvd_covers[idx] = image

	scope.dvd_covers = dvd_covers
