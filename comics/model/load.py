
import os
import pandas as pd

from comics.model.schema import schema
from comics.model.schema import csv_dates
from comics.model.schema import csv_dtypes

from comics.model.save import save_comics_file


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


