
# uv run src/dvds/model.py
import logging
from dataclasses import dataclass, asdict
import json
import os
from pathlib import Path
from PIL import Image

# index	,series		,season	,story	,title,doctor		,image				,collected	,url	,watched											,cover	,available
# 1		,Doctor Who	,1		,1		,An Unearthly Child	,William Hartnell	,True		,True	,http://en.wikipedia.org/wiki/An_Unearthly_Child	,True,1,True
# 2		,Doctor Who	,1		,2		,The Daleks			,William Hartnell	,True		,True	,http://en.wikipedia.org/wiki/The_Daleks,False		,2,True



# --------------------------------------------------------------------------------------------------------------------------------------------------------------

@dataclass()
# @dataclass(kw_only=True)
class Dvd:
	# Instance Variables (so called because they have a datatype declared)
	index 				: int 	= None				# unique Identifier
	series 				: str 	= None
	season 				: str 	= None
	story 				: str 	= None
	title 				: str 	= None		# "Missing Title for this Issue"
	doctor 				: str 	= None
	image 				: bool 	= False
	collected 			: bool 	= False
	url					: str 	= None
	watched 			: bool 	= False
	cover 				: str 	= None
	available 			: bool 	= False



	# Class Variables - application
	dvd_objects				= []			# list of all instances/objects
	unique_identifiers 		= []			# List of Unique identifiers
	
	series_list				= []			# i.e. Doctor Who or Star Trek
	seasons_list			= []			# 1, 2, 3
	doctors_list			= []			# subset for Doctor Who only
	# These are defaulted to Doctor Who as that is the only series that is
	# currently being collected. We can change this to None later if we
	# decide to collect additional series
	selected_series 		= "Doctor Who"			# Page Tracking 
	selected_season 		= "All Seasons"			# Page Tracking
	selected_doctor			= "All Doctors"			# Page Tracking
	selected_missing_only 	= False					# Page Tracking	
	
	page_dvds				= []			# list of the loaded Dvd covers ??
	page_covers 			= []			# store the images for the selected comics
	page_qty				= 0
	page_qty_collected		= 0
	page_qty_missing		= 0
	page_qty_available		= 0
	
	@property
	def path_to_cover_art(self) -> str:
		_file_name = str(self.cover) + ".jpg"
		_path_comic_image 	= Path.home().joinpath( Dvd._path_dvds_covers, _file_name )
		return _path_comic_image


	# Class Variables - internal system
	_path_dvds_json 			= Path(__file__).parent.parent.parent / "data" / "dvds.json"
	_path_dvds_covers			= Path(__file__).parent.parent.parent / "data" / "dvd_covers"
	path_dvds_covers_missing	= Path(__file__).parent.parent.parent / "data" / "dvd_covers" / "x.jpg"

	def __post_init__(self):
		"""Add object to registry if index is unique, else raise error."""
		print("Adding DVD > ", self.index, ' episode = ', self.story)
		
		if self.index in self.unique_identifiers:
			raise ValueError(f"Duplicate index {self.index} found. Index must be unique.")
		self.unique_identifiers.append(self.index)
		self.dvd_objects.append(self)

	@classmethod
	def save_dvds(cls):
		"""Save the Dvd Objects into a JSON file"""
		logging.warning("Save all Dvd instances to JSON file")
		try:
			with open(cls._path_dvds_json, 'w') as file:
				# Convert instances to dicts for JSON serialization
				json.dump([asdict(instance) for instance in cls.dvd_objects], file, indent=4)

		except Exception as e:
			print(f"Error saving instances: {e}")

	@classmethod
	def load_dvds(cls):
		"""Load the DVDs JSON file and create objects"""
		logging.warning("Load Dvd instances from JSON file")
		try:
			if os.path.exists(cls._path_dvds_json):
				with open(cls._path_dvds_json, 'r') as file:
					data = json.load(file)
				# Clear current instances to avoid duplicates
				cls.dvd_objects.clear()
				# Create new instances from loaded data
				for item in data:
					# Ensure all required fields are present
					instance = cls(**item)
				# Create the initial lists
				Dvd.create_series_list()
				Dvd.create_season_list()
				Dvd.create_doctors_list()
				Dvd.create_page_dvds()
				return cls.dvd_objects.index
			else:
				print(f"No file found at {cls._path_dvds_json}")
				return []
		except Exception as e:
			print(f"Error loading instances: {e}")
			return []

	@classmethod
	def get_by_index(cls, index: int):
		"""Return the first dvd object with the specified index, or None if not found."""
		logging.critical(f"get_by_index {index}")
		for dvd in cls.dvd_objects:
			if dvd.index == index:
				return dvd
		return None

	@classmethod
	def create_series_list(cls):
		logging.warning("create_series_list")
		cls.series_list = []
		for dvd in cls.dvd_objects:
			if dvd.series == cls.selected_series: # Doctor Who
				if dvd.series not in cls.series_list:
					cls.series_list.append(dvd.series)
	
	@classmethod
	def create_season_list(cls):
		logging.warning("create_season_list")
		
		_season_list = []
		for dvd in cls.dvd_objects:
			if dvd.series == cls.selected_series: # Doctor Who
				if dvd.season not in _season_list:
					_season_list.append(dvd.season)
		_season_list.insert(0, 'All Seasons')
		cls.seasons_list = _season_list

	@classmethod
	def create_doctors_list(cls):
		logging.warning("create_doctors_list")
		_doctors_list = []
		for dvd in cls.dvd_objects:
			if dvd.series == "Doctor Who":
				if dvd.doctor not in _doctors_list:
					_doctors_list.append(dvd.doctor)
		_doctors_list.insert(0, "All Doctors")
		cls.doctors_list = _doctors_list


	@classmethod
	def create_page_dvds(cls):
		"""contruct a list of dvds specifically for the page being rendered that
		takes into account any filters or criteria"""
		logging.warning(f"create_page_dvds {cls.selected_series}")
		
		cls.page_dvds = []

		for dvd in cls.dvd_objects:
			series = dvd.series
			season = dvd.season
			doctor = dvd.doctor

			if series == cls.selected_series: # Doctor Who
				if season == cls.selected_season or cls.selected_season == "All Seasons":
					if doctor == cls.selected_doctor or cls.selected_doctor == "All Doctors":
						cls.page_dvds.append(dvd)
								
		
		# Remove collected items if only interested in missing comics
		if cls.selected_missing_only:
			for dvd in cls.page_dvds[:]:
				if dvd.collected or not dvd.available:
					cls.page_dvds.remove(dvd)
		
		# sort the list
		cls.page_dvds.sort(key=lambda dvd: dvd.index)

		# Load the dvd covers for the page
		cls.page_covers = []
		for dvd in cls.page_dvds:
			_image = Image.open(dvd.path_to_cover_art)
			cls.page_covers.append(_image)

		# Update counts
		cls.count_page_objects()


	@classmethod
	def count_page_objects(cls):
		cls.page_qty 			= 0
		cls.page_qty_collected 	= 0
		# cls.page_qty_missing 	= 0
		cls.page_qty_available 	= 0
		# cls.page_qty_stories	= 0

		for dvd in cls.page_dvds:
			if dvd.collected:
				cls.page_qty_collected += 1
			# else:
			# 	cls.page_qty_missing += 1

			if dvd.available:
				cls.page_qty_available += 1	

		# Update Page Object Count Totals
		cls.page_qty = len(cls.page_dvds)



# change_series - ie 
# selected_series = selected_series		# Done
# - scope_list_of_seasons				# Done
# - scope_dvds_to_display				# Done
# - scope_dvd_covers_for_page			# Done

# change_season							# Done
# selected_season = selected_season		# Done
# - scope_dvds_to_display				# Done
# - scope_dvd_covers_for_page			# Done

# change_doctor
# selected_doctor = selected_doctor		# Done
# - scope_list_of_seasons				# Done
# - scope_dvds_to_display				# Done
# - scope_dvd_covers_for_page			# Done

# change_show_missing_episodes			# Done
# selected_missing_only = new_vale		# Done
# - scope_dvds_to_display				# Done
# - scope_dvd_covers_for_page			# Done
