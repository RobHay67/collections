
import os
import pandas as pd
from PIL import Image

from comics.model.schema import schema
from comics.model.schema import csv_dates
from comics.model.schema import csv_dtypes

from comics.model.save import save_comics_file
from files.config import path_comic_cover


def load_comics_file(scope):

	if os.path.exists( scope.path_comics_file ):

		comics_file = pd.read_csv(  scope.path_comics_file, 
									dtype=csv_dtypes(schema),
									parse_dates=csv_dates(schema),
									)

		comics_file['cover_date'] = pd.to_datetime( comics_file['cover_date'].dt.date  )

		scope.comics_file = comics_file
	else: 
		dataframe_columns = []
		for column_name in schema: 
			dataframe_columns.append(column_name)
			
		comics_file = pd.DataFrame(columns=dataframe_columns)
		
		scope.comics_file = comics_file
		
		save_comics_file(scope)


def load_comic_covers(scope):

	print('load all the comic covers and storee them for later usage')

	series = scope.comics_selected_series

	volume = scope.comics_selected_volume
	issue_list = list(scope.comic_df['issue_no'])

	comic_covers = {}

	for issue in issue_list:
		path_to_comic_cover = path_comic_cover(scope, series, volume, issue)
		image = Image.open(path_to_comic_cover)

		comic_covers[issue] = image


	scope.comic_covers = comic_covers
