

def save_dvds_file( scope ): 
	print ( 'Saving the dvds file')
	
	saving_df = scope.dvds_file.copy()
	
	saving_df.reset_index(inplace=True)      	 # ensure that the index is saved as a normal column
	
	saving_df.to_csv( scope.path_dvds_file, index=False )
	
	print ( '\033[92mSaved DVDs File \033[0m')



