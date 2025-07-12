import logging
import os
import pathlib
import streamlit as st

#TODO - replace pathlib with OS

def scope_file_locations(scope):
	logging.warning("scope_file_locations")
	scope.folder_project = pathlib.Path(__file__).parent.parent.resolve()
	scope.folder_files = pathlib.Path.home().joinpath( scope.folder_project, 'files' )

	scope.folder_comic_covers = pathlib.Path.home().joinpath( scope.folder_files, 'comic_covers' )
	scope.folder_dvd_covers = pathlib.Path.home().joinpath( scope.folder_files, 'dvd_covers' )
	
	if not os.path.isdir( scope.folder_files ) 	 	  	: os.makedirs( scope.folder_files )
	if not os.path.isdir( scope.folder_comic_covers ) 	: os.makedirs( scope.folder_comic_covers )
	if not os.path.isdir( scope.folder_dvd_covers ) 	: os.makedirs( scope.folder_dvd_covers )


	# File Paths
	scope.file_path_comics = pathlib.Path.home().joinpath( scope.folder_files, 'comics.csv' )
	# scope.path_cards_file  = pathlib.Path.home().joinpath( scope.folder_files, 'cards.csv' )
	scope.file_path_dvds   = pathlib.Path.home().joinpath( scope.folder_files, 'dvds.csv' )

	scope.file_path_dvds_missing_cover = pathlib.Path.home().joinpath( scope.folder_dvd_covers, 'x.jpg' )



def path_comic_cover(scope, series_name, volume_number, issue_number):
	logging.trace(f"path_comic_cover {series_name=} {volume_number=} {issue_number=}")
	series_name = series_name.replace(' ', '_')

	file_name = series_name + '_Vol_' + str(volume_number) + '_' + str(issue_number) + '.jpg'

	path_comic_image = pathlib.Path.home().joinpath( scope.folder_comic_covers, file_name )

	return path_comic_image


def path_dvd_cover(scope, cover_number):
	logging.trace(f"path_dvd_cover {cover_number=}")
	file_name = str(cover_number) + '.jpg'
	path_comic_image = pathlib.Path.home().joinpath( scope.folder_dvd_covers, file_name )
	return path_comic_image