import streamlit as st

from comics.view.comics import render_comics_star_wars



def render_star_wars_comics(scope):

	st.title('Star Wars - Comic Collection')


	# st.


	series = st.selectbox(
							label='CHoose Comic Series',
							options=['Star Wars', 'Return of the Jedi', 'Star Trek', 'X-Men']
							)




	# filter the dataframe to the series

	# produce an ordered list of the comics

	# st.write each one to the web page



	st.write(scope.comics_file)


	render_comics_star_wars(scope)