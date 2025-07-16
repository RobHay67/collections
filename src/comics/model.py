
# uv run src/comics/model.py
import logging
from dataclasses import dataclass, asdict
import datetime
import json
import os
from pathlib import Path
from PIL import Image

# --------------------------------------------------------------------------------------------------------------------------------------------------------------

@dataclass()
# @dataclass(kw_only=True)
class Comic:
	# Instance Variables (so called because they have a datatype declared)
	index 				: int 	= None				# unique Identifier
	series 				: str 	= "unknown series"
	volume 				: int 	= None
	issue_no 			: str 	= None
	title 				: str 	= "Missing Title for this Issue"
	cover_date 			: datetime.datetime = datetime.datetime(2001,1,1).strftime("%Y-%m-%d")
	collected 			: bool 	= False
	condition			: str 	= 'unknown condition'
	value 				: float = 0.0
	notes 				: str 	= None

	# Class Variables - application
	comic_objects			= []			# list of all instances/objects
	unique_identifiers 		= []
	series_list				= []
	selected_series 		= None			# Page Tracking
	selected_missing_only 	= None			# Page Tracking
	page_comics				= []			# list of the loaded comic covers ??
	page_covers 			= []			# store the images for the selected comics
	page_qty				= 0
	page_qty_collected		= 0
	page_qty_missing		= 0
	
	@property
	def path_to_cover_art(self) -> str:
		_series_name 		= self.series.replace(' ', '_')
		_file_name 			= _series_name + '_Vol_' + str(self.volume) + '_' + str(self.issue_no) + '.jpg'
		_path_comic_image 	= Path.home().joinpath( Comic._path_comic_covers, _file_name )
		return _path_comic_image

	# Class Variables - internal system
	_pathc_comics_json 	= Path(__file__).parent.parent.parent / "data" / "comics.json"
	_path_comic_covers	= Path(__file__).parent.parent.parent / "data" / "comic_covers"

	def __post_init__(self):
		"""Add object to registry if index is unique, else raise error."""
		if self.index in self.unique_identifiers:
			raise ValueError(f"Duplicate index {self.index} found. Index must be unique.")
		self.unique_identifiers.append(self.index)
		self.comic_objects.append(self)

		if self.series not in self.series_list:
			self.series_list.append(self.series)

	@classmethod
	def save_comics(cls):
		"""Save the Comics Objects into a JSON file"""
		logging.warning("Save all Comic instances to JSON file")
		try:
			with open(cls._pathc_comics_json, 'w') as file:
				# Convert instances to dicts for JSON serialization
				json.dump([asdict(instance) for instance in cls.comic_objects], file, indent=4)

		except Exception as e:
			print(f"Error saving instances: {e}")

	@classmethod
	def load_comics(cls):
		"""Load the Comics JSON file and create objects"""
		logging.warning("Load Comic instances from JSON file")
		try:
			if os.path.exists(cls._pathc_comics_json):
				with open(cls._pathc_comics_json, 'r') as file:
					data = json.load(file)
				# Clear current instances to avoid duplicates
				cls.comic_objects.clear()
				# Create new instances from loaded data
				for item in data:
					# Ensure all required fields are present
					instance = cls(**item)
				return cls.comic_objects.index
			else:
				print(f"No save file found at {cls._pathc_comics_json}")
				return []
		except Exception as e:
			print(f"Error loading instances: {e}")
			return []

	@classmethod
	def get_by_index(cls, index: int):
		"""Return the first Comic object with the specified index, or None if not found."""
		logging.critical(f"get_by_index {index}")
		for comic in cls.comic_objects:
			if comic.index == index:
				return comic
		return None

	@classmethod
	def create_page_comics(cls):
		"""contruct a list of comics specifically for the page being rendered that
		takes into account any filters or criteria"""
		logging.warning(f"create_page_comics {cls.selected_series}")
		cls.page_comics 		= []
		for comic in cls.comic_objects:
			if comic.series == cls.selected_series:
				cls.page_comics.append(comic)
		
		# Remove collected items if use only interested in missing comics
		if cls.selected_missing_only:
			for comic in cls.page_comics:
				if comic.collected:
					cls.page_comics.remove(comic)
		# sort the list
		cls.page_comics.sort(key=lambda comic: comic.index)

		# Load the comics covers for the page
		cls.page_covers = []
		for comic in cls.page_comics:
			_image = Image.open(comic.path_to_cover_art)
			# cls.page_covers[comic.index] = _image
			cls.page_covers.append(_image)

		# Update counts
		cls.count_page_objects()

	@classmethod
	def count_page_objects(cls):
		cls.page_qty 			= 0
		cls.page_qty_collected 	= 0
		cls.page_qty_missing 	= 0

		for comic in cls.page_comics:
			if comic.collected:
				cls.page_qty_collected += 1
			else:
				cls.page_qty_missing += 1			

		# Update Page Object Count Totals
		cls.page_qty = len(cls.page_comics)
