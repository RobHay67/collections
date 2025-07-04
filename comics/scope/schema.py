import logging
import pandas as pd


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Comic File Schema
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
schema = {
		'index'				:{'dtype':'int'				, 'default':None},
		'series'			:{'dtype':'str'				, 'default':'unknown series'},
		'volume'			:{'dtype':'int'				, 'default':None},
		'issue_no'			:{'dtype':'str'				, 'default':None},
		'title'				:{'dtype':'str'				, 'default':'unknown comic title'},
		'cover_date'		:{'dtype':'datetime64[ns]'	, 'default':pd.to_datetime('2000-01-01')},
		'collected'			:{'dtype':'boolean'			, 'default':False},
		'condition'			:{'dtype':'str'				, 'default':'unknown condition'},
		'value'				:{'dtype':'float64'			, 'default':0.0},
		'notes'				:{'dtype':'str'				, 'default':None},
		
	}


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Index file Schema - Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def data_types(schema):
	logging.warning(f"data_types (schema)")
	dtypes={}
	for field, schema in schema.items():
		dtypes[field] = schema['dtype']
	return dtypes

def default_values(schema):
	logging.warning(f"default_values (schema)")
	default_values={}
	for field, schema in schema.items():
		default_values[field] = schema['default']
	return default_values

def csv_dtypes(schema):
	logging.warning(f"csv_dtypes (schema)")
	dtypes={}
	for field, schema in schema.items():
		if schema['dtype'] != 'datetime64[ns]': 
			dtypes[field] = schema['dtype']
	return dtypes

def csv_dates(schema):
	logging.warning(f"csv_dates (schema)")
	dates_to_parse = []
	for field, schema in schema.items():
		if schema['dtype'] == 'datetime64[ns]': 
			dates_to_parse.append(field)
	return dates_to_parse

