

def save_comics_file( scope ): 
	print ( 'Saving the comics file')
	
	saving_df = scope.comics_file.copy()
	
	saving_df.reset_index(inplace=True)      	 # ensure that the index is saved as a normal column
	
	saving_df.to_csv( scope.path_comics_file, index=False )
	
	print ( '\033[92mSaved Comics File \033[0m')



