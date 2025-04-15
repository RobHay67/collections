import logging
import os
import pandas as pd
from comics.scope.schema import schema
from comics.scope.schema import csv_dates
from comics.scope.schema import csv_dtypes


def load_comic_file(scope):
	logging.warning("load_comic_file")
	if os.path.exists( scope.file_path_comics ):
		comic_file = pd.read_csv(  scope.file_path_comics, 
						   			index_col='index',
									dtype=csv_dtypes(schema),
									parse_dates=csv_dates(schema),
									)

		comic_file['cover_date'] = pd.to_datetime( comic_file['cover_date'].dt.date  )
	else: 
		dataframe_columns = []
		for column_name in schema: 
			dataframe_columns.append(column_name)
		comic_file = pd.DataFrame(columns=dataframe_columns)
	return comic_file



