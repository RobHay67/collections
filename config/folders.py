import os
import pathlib
import streamlit as st

#TODO - replace pathlib with OS

def scope_file_locations(scope):

	scope.folder_project = pathlib.Path(__file__).parent.parent.resolve()
	scope.folder_files = pathlib.Path.home().joinpath( scope.folder_project, 'files' )

	scope.folder_comic_covers = pathlib.Path.home().joinpath( scope.folder_files, 'comic_covers' )
	
	if not os.path.isdir( scope.folder_files ) 	 	  : os.makedirs( scope.folder_files )
	if not os.path.isdir( scope.folder_comic_covers ) : os.makedirs( scope.folder_comic_covers )


	# File Paths
	scope.path_comics_file = pathlib.Path.home().joinpath( scope.folder_files, 'comics.csv' )
	scope.path_cards_file  = pathlib.Path.home().joinpath( scope.folder_files, 'cards.json' )
	scope.path_dvds_file   = pathlib.Path.home().joinpath( scope.folder_files, 'dvds.json' )




def path_comic_cover(scope, series_name, volume_number, issue_number):

	series_name = series_name.replace(' ', '_')
	print(series_name)


	file_name = series_name + '_Vol_' + str(volume_number) + '_' + str(issue_number) + '.jpg'


	path_comic_image = pathlib.Path.home().joinpath( scope.folder_comic_covers, file_name )

	return path_comic_image





# from PIL import Image
# # image = Image.open('sunrise.jpg')

# def path_comic_cover(scope, volume_number, issue_number):

# 	# file_name = 'Star_Wars_Vol_' + str(volume_number) + '_' + str(issue_number) + '.webp'
# 	file_name = 'Star_Wars_Vol_' + str(volume_number) + '_' + str(issue_number) + '.jpg'

# 	path_comic_image = pathlib.Path.home().joinpath( scope.folder_comic_covers, file_name )

# 	print(path_comic_image)

# 	if os.path.exists( path_comic_image ):
# 		print('-'*100)
# 		print( 'Opening Image > ', issue_number)
# 		# print(path_comic_image)

# 		image = Image.open(path_comic_image).covert('RGB')
# 		print(image)
# 	# else:
# 	# 	print('Path does not exist')




# # Star_Wars_Vol_1_4.webp

