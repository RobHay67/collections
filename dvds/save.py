

def save_dvd_file( scope ): 
	print ( 'Saving the dvds file')
	
	saving_df = scope.dvd_file.copy()
	
	saving_df.reset_index(inplace=True)      	 # ensure that the index is saved as a normal column
	
	saving_df.to_csv( scope.dvd_file_path, index=False )
	
	print ( '\033[92mSaved DVDs File \033[0m')



