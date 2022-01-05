


from comics.view.comics import view_comics_star_wars
from comics.model.load import load_comics_file



def comics_star_wars(scope):


	print ( 'have called comics_star_wars')


	# load a list of comics if we have not already - maybe some scope for this

	if scope.loaded_comics == False:
		print ( 'Load the comics file')
		load_comics_file(scope)
		scope.loaded_comics = True
	else:
		print ( 'Already loaded the comics file')



	view_comics_star_wars(scope)