import logging

def save_dvd_file( scope ): 
	logging.warning(f"save_dvd_file")
	saving_df = scope.dvds_file.copy()
	# ensure that the index is saved as a normal column
	saving_df.reset_index(inplace=True)
	saving_df.to_csv( scope.file_path_dvds, index=False )


