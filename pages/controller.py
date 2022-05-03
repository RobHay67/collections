

from pages.home import render_home_page
from comics.controller import render_comics_page
from pages.cards import render_cards_page
from dvds.controller import render_dvds_page




def render_selected_page(scope):
	
	page = scope.pages['display_page']
	# print( 'Rendering > ', page)
	
	page_map = {
						'home_page'			:render_home_page,
						'comics'			:render_comics_page,
						'cards'				:render_cards_page,
						'dvds'				:render_dvds_page,

					}

	if page in list(page_map.keys()):
		page_map[page](scope)


