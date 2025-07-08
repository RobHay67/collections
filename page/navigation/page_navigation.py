import logging
import streamlit as st


def sidebar_navigation(scope):
	logging.warning("sidebar_navigation")
	home_page = st.Page(
		page="page/page_home.py",
		title="Home",
		icon="🌤️",
		default=True
		)
	comics_page = st.Page(
		page="comics/views/page_comics.py",
		title="Comics",
		icon="🌤️",
		default=False
		)
	dvds_page 	= st.Page(
		page="dvds/views/page_dvds.py",
		title="DVDs",
		icon="🌤️",
		default=False
		)
	trading_cards_page = st.Page(
		page="trading_cards/page_trading_cards.py",
		title="Trading Cards",
		icon="🌤️",
		default=False
		)
	testing_page = st.Page(
		page="page/page_test.py",
		title="Testing",
		icon="🌤️",
		default=False
		)

	page_navigation = st.navigation(
		{
		"Research & Analysis"	: [
			home_page, 
			comics_page, 
			dvds_page,
			trading_cards_page, 
			],
		"Config"	: [
			testing_page
			],
		}
	)
	return page_navigation