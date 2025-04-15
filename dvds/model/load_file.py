import logging
import os
import pandas as pd
from dvds.scope.schema import schema
from dvds.scope.schema import csv_dates
from dvds.scope.schema import csv_dtypes


def load_dvd_file(scope):
	logging.warning(f"load_dvd_file")
	if os.path.exists( scope.file_path_dvds ):
		dvd_file = pd.read_csv(  scope.file_path_dvds, 
									index_col='index',
									dtype=csv_dtypes(schema),
									parse_dates=csv_dates(schema),
									)
	else: 
		dataframe_columns = []
		for column_name in schema: 
			dataframe_columns.append(column_name)
		dvd_file = pd.DataFrame(columns=dataframe_columns)
	
	return dvd_file
		
		



