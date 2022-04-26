

from pages.view.welcome import view_project_welcome
# from pages.view.comics import view_comics_star_wars
# from comics.controller import comics_star_wars
from pages.view.comics import render_star_wars_comics
from pages.view.cards import view_cards_star_wars
from pages.view.dvds import view_dr_who_dvds




def render_selected_page(scope):
	
	page = scope.pages['display_page']
	# print( 'Rendering > ', page)
	
	page_map = {
						'home_page'			:view_project_welcome,
						'sw_comics'			:render_star_wars_comics,
						'sw_cards'			:view_cards_star_wars,
						'dr_who'			:view_dr_who_dvds,

					}

	if page in list(page_map.keys()):
		page_map[page](scope)


