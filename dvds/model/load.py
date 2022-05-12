
import os
import pandas as pd
from PIL import Image

from dvds.model.schema import schema
from dvds.model.schema import csv_dates
from dvds.model.schema import csv_dtypes

from dvds.model.save import save_dvds_file
from files.config import path_dvd_cover



def load_dvds_file(scope):

	if os.path.exists( scope.path_dvds_file ):

		dvds_file = pd.read_csv(  scope.path_dvds_file, 
									index_col='index',
									dtype=csv_dtypes(schema),
									parse_dates=csv_dates(schema),
									)

	else: 
		dataframe_columns = []
		for column_name in schema: 
			dataframe_columns.append(column_name)
			
		dvds_file = pd.DataFrame(columns=dataframe_columns)

		save_dvds_file(scope)
		
	scope.dvds_file = dvds_file
		
		


def load_dvd_covers_for_series(scope):

	print('load all the dvd covers and store them for later usage')

	series = scope.dvd_selected_series

	# Filter to selected series
	# load_df = scope.dvd_df[scope.dvd_df['series']==series].copy()
	load_df = scope.dvds_file[scope.dvds_file['series']==series].copy()

	dvd_covers = {}
	missing_cover_image = image = Image.open(scope.path_to_missing_dvd_cover)

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
