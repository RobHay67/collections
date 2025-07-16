
# uv run src/comics/rob.py

# from comics.model import Comic

# from src.comics.model import Comic


# from comics.model import Comic

from model import Comic


# try:
# 	# Attempting to import a function that does not exist in the module
# 	from comics.model import Comic
# except ImportError as e:
# 	print(f"ImportError: {e}")


# Testing code
def testing_header(test_name):
	print()
	print("="*88)
	print(test_name)
	print("-"*88)





testing_header("Load JSON objects")
Comic.load_comics()




testing_header("Test Access to Class Variabless")
print(Comic.series_list)
print(Comic.selected_series)
print(Comic.selected_missing_only)
print(Comic._path_comic_covers)
print(Comic._pathc_comics_json)

testing_header("Test create_list_of_comic_indexes_for_page")
Comic.selected_series = "Star Wars"
Comic.selected_missing_only = False
Comic.create_page_comics()
print(Comic.series_list)
print(Comic.unique_identifiers)
print(Comic.page_qty)
print(Comic.page_qty_missing)
print(Comic.page_qty_collected)

# testing_header("test Manual Creation of Comic Object")
# comic_1 = Comic(index=113, series="Star Wars", title="The Wheel of Death")
# # print(Comic._comics_list)
# print(comic_1)

# # print(Comic.list_of_series)
# print(Comic._comics_list)
# comic_2 = Comic(index=113, series="Star Wars", title="Return of the Jedi")
# print(comic_2)
# print(Comic._comics_list)

# print(Comic.get_by_index(113))



# Comic.create_list_of_comic_indexes_for_page()

# # print(Comic._comics_list_for_page)

# # print(Comic._comics_list)

# print(Comic)

# for object in Comic:
# 	print(object)

# [Comic(index=1, series='Star Wars', volume=1, issue_no='1a', title='Revenge of the Sith', cover_date='2001-01-01', collected=True, value=50.0, notes=None), 
#  Comic(index=2, series='Star Wars', volume=1, issue_no='1b', title='The Wheel of Death', cover_date='2001-01-01', collected=True, value=400.0, notes='35cent edition with UPC code'), 
#  Comic(index=3, series='Star Wars', volume=1, issue_no='2', title='Comic 2', cover_date='2001-01-01', collected=True, value=30.0, notes=None)]
# testing_header("output loaded objects")
# # print(Comic._comics_list)
# for comic in Comic._comics_list:
# 	print(comic.index, comic.series, comic.title, comic.path_to_cover_art)

# testing_header("test creation of list_of_series")
# print(Comic.list_of_series)



# testing_header("Test create_list_of_comic_indexes_for_page")
# Comic.selected_series = "Star Wars"
# Comic.selected_missing_only = False
# Comic.create_list_of_comic_indexes_for_page()
# print(Comic._comics_list_for_page)
# print(len(Comic._comics_list_for_page))

# testing_header("Test Images")
# print(Comic.list_of_covers_for_page)
# for key, cover in Comic.list_of_covers_for_page.items():
# 	print(key)
# 	print(cover)




# # Load the old CSV
# import pandas as pd

# file_path_comics = Path(__file__).parent.parent.parent / "data" / "comics.csv"
# dtypes={
# 	"index" 	: "int",
# 	"series" 	: "str",
# 	"volume" 	: "int",
# 	"issue_no" 	: "str",
# 	"title" 	: "str",
# 	"collected" : "boolean",
# 	"condition" : "str",
# 	"value" 	: "float64",
# 	"notes" 	: "str",
# }

# comic_file = pd.read_csv(  file_path_comics, 
# 							index_col='index',
# 							dtype=dtypes,
# 							# parse_dates=["cover_date"],
# 							)
# # comic_file['cover_date'] = pd.to_datetime( comic_file['cover_date'].dt.date  )

# # Iterate through the CSV file
# comic_file.reset_index(drop=False, inplace=True)
# for index, row in comic_file.iterrows():



# 	objects = [Comic(
# 					row['index'], 
# 					row['series'],
# 					row['volume'],
# 					row['issue_no'],
# 					row['title'],
# 					row['cover_date'],
# 					row['collected'],
# 					row['condition'],
# 					row['value'],
# 					row['notes'],
# 					) for _, row in comic_file.iterrows()]
# 	print(objects)

# # Save the json file
# Comic.save_comics()

