# uv run src/comics/x_test.py




from dataclasses import dataclass, field
from typing import List, Any

@dataclass
class UniqueObject:
	index: int
	name: str
	description: str = ""


	comic_objects = []
	unique_identifiers = []
	# comic_objects: List[Any] = field(default_factory=list, init=False, repr=False)
	# unique_identifiers: set = field(default_factory=set, init=False, repr=False)

	def __post_init__(self):
		"""Add object to registry if index is unique, else raise error."""
		if self.index in self.unique_identifiers:
			raise ValueError(f"Duplicate index {self.index} found. Index must be unique.")
		# self.unique_identifiers.add(self.index)
		self.unique_identifiers.append(self.index)
		self.comic_objects.append(self)

	@classmethod
	def get_by_index(cls, index: int) -> Any:
		"""Retrieve an object by its index."""
		for obj in cls.comic_objects:
			if obj.index == index:
				return obj
		return None

	@classmethod
	def all_objects(cls) -> List[Any]:
		"""Return all registered objects."""
		return cls.comic_objects

	# @classmethod
	# def clearcomic_objects(cls):
	# 	"""Clear the registry and index set."""
	# 	cls.comic_objects.clear()
	# 	cls.unique_identifiers.clear()

	def __str__(self) -> str:
		return f"{self.name} (Index: {self.index})"

# Example usage
if __name__ == "__main__":
	# Create objects
	obj1 = UniqueObject(index=1, name="Object 1", description="First object")
	obj2 = UniqueObject(index=2, name="Object 2", description="Second object")

	# Try creating a duplicate index (will raise ValueError)
	try:
		obj3 = UniqueObject(index=1, name="Object 3", description="Duplicate index")
	except ValueError as e:
		print(e)  # Prints: Duplicate index 1 found. Index must be unique.

	# Access objects by index
	print(UniqueObject.get_by_index(1))  # Prints: Object 1 (Index: 1)
	print(UniqueObject.get_by_index(2))  # Prints: Object 2 (Index: 2)
	print(UniqueObject.get_by_index(3))  # Prints: None

	# List all objects
	print(UniqueObject.all_objects())  # Prints: [UniqueObject(...), UniqueObject(...)]


	print(UniqueObject.unique_identifiers)