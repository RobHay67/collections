

def save_comic_file( scope ): 
	print ( 'Saving the comics file')
	
	saving_df = scope.comic_file.copy()
	
	saving_df.reset_index(inplace=True)      	 # ensure that the index is saved as a normal column
	
	saving_df.to_csv( scope.comic_file_path, index=False )
	
	print ( '\033[92mSaved Comics File \033[0m')



