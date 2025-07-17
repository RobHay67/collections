# uv run src/dvds/testing.py

from model import Dvd



# Testing code
def testing_header(test_name):
	print()
	print("="*88)
	print(test_name)
	print("-"*88)





testing_header("Load Comics JSON objects")
Dvd.load_dvds()

print(Dvd.unique_identifiers)








# from pathlib import Path

# # Load the old CSV
# import pandas as pd



# file_path_dvds = Path(__file__).parent.parent.parent / "data" / "dvds.csv"
# dtypes={
# 	"index" 	: "int",
# 	"series" 	: "str",
# 	"season" 	: "int",
# 	"story" 	: "str",
# 	"title" 	: "str",
# 	"doctor" 	: "str",
# 	"image" 	: "boolean",
# 	"collected" : "boolean",
# 	"url" 		: "str",
# 	"watched" 	: "boolean",
# 	"cover" 	: "str",
# 	"available" : "boolean",
# }

# dvd_df = pd.read_csv(  file_path_dvds, 
# 							index_col='index',
# 							dtype=dtypes,
# 							)

# dvd_df.reset_index(drop=False, inplace=True)
# # dvd_df = dvd_df.sample(5)
# # print(dvd_df)
# # print("total rows = ", len(dvd_df))
# # print(dvd_df.tail(5))
# # print(dvd_df.head(5))
# # Iterate through the CSV file
# # dvd_df.reset_index(drop=False, inplace=True)
# for index, row in dvd_df.iterrows():
# 	# print(row['index'])

# 	objects = Dvd(
# 					row['index'], 
# 					row['series'],
# 					row['season'],
# 					row['story'],
# 					row['title'],
# 					row['doctor'],
# 					row['image'],
# 					row['collected'],
# 					row['url'],
# 					row['watched'],
# 					row['cover'],
# 					row['available'],
# 					) 
# 	# print(objects)

# # Save the json file
# Dvd.save_dvds()

