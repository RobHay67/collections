
import pandas as pd

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Comic File Schema
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
schema = {
		'index'		:{'dtype':'int'		, 'default':None},
		'series'	:{'dtype':'str'		, 'default':None},
		'season'	:{'dtype':'str'		, 'default':None},
		'story'		:{'dtype':'str'		, 'default':None},
		'title'		:{'dtype':'str'		, 'default':None},
		'doctor'	:{'dtype':'str'		, 'default':None},
		'image'		:{'dtype':'boolean'	, 'default':False},
		'url'		:{'dtype':'str'		, 'default':None},
	}





# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Index file Schema - Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def data_types(schema):
	dtypes={}
	for field, schema in schema.items():
		dtypes[field] = schema['dtype']
	return dtypes

def default_values(schema):
	default_values={}
	for field, schema in schema.items():
		default_values[field] = schema['default']
	return default_values

def csv_dtypes(schema):
	dtypes={}
	for field, schema in schema.items():
		if schema['dtype'] != 'datetime64[ns]': 
			dtypes[field] = schema['dtype']
	return dtypes

def csv_dates(schema):
	dates_to_parse = []
	for field, schema in schema.items():
		if schema['dtype'] == 'datetime64[ns]': 
			dates_to_parse.append(field)
	return dates_to_parse

