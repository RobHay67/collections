import os
import pathlib
import streamlit as st

#TODO - replace pathlib with OS

def scope_file_locations(scope):

	scope.folder_project = pathlib.Path(__file__).parent.parent.resolve()
	scope.folder_files = pathlib.Path.home().joinpath( scope.folder_project, 'files' )

	scope.comic_folder_covers = pathlib.Path.home().joinpath( scope.folder_files, 'comic_covers' )
	scope.dvd_folder_covers = pathlib.Path.home().joinpath( scope.folder_files, 'dvd_covers' )
	
	if not os.path.isdir( scope.folder_files ) 	 	  	: os.makedirs( scope.folder_files )
	if not os.path.isdir( scope.comic_folder_covers ) 	: os.makedirs( scope.comic_folder_covers )
	if not os.path.isdir( scope.dvd_folder_covers ) 	: os.makedirs( scope.dvd_folder_covers )


	# File Paths
	scope.comic_file_path = pathlib.Path.home().joinpath( scope.folder_files, 'comics.csv' )
	# scope.path_cards_file  = pathlib.Path.home().joinpath( scope.folder_files, 'cards.csv' )
	scope.dvd_file_path   = pathlib.Path.home().joinpath( scope.folder_files, 'dvds.csv' )

	scope.dvd_file_path_missing_cover = pathlib.Path.home().joinpath( scope.dvd_folder_covers, 'x.jpg' )



def path_comic_cover(scope, series_name, volume_number, issue_number):

	series_name = series_name.replace(' ', '_')

	file_name = series_name + '_Vol_' + str(volume_number) + '_' + str(issue_number) + '.jpg'

	path_comic_image = pathlib.Path.home().joinpath( scope.comic_folder_covers, file_name )

	return path_comic_image



def path_dvd_cover(scope, idx):

	file_name = str(idx) + '.jpg'

	path_comic_image = pathlib.Path.home().joinpath( scope.dvd_folder_covers, file_name )

	return path_comic_image

