import logging


def save_comic_file( scope ): 
	logging.warning("save_comic_file")
	saving_df = scope.comics_file.copy()
	# ensure that the index is saved as a normal column
	saving_df.reset_index(inplace=True)
	saving_df.to_csv( scope.file_path_comics, index=False )



