import streamlit as st
from PIL import Image

from config.folders import path_comic_cover


def render_comics_star_wars(scope):

	st.title('Star Wars - Comics')

	st.subheader('Star Wars Volume 1')


	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,2,4,2,1,1,1])
	with col1: st.subheader('Issue')
	with col2: st.subheader('Cover Date')
	with col3: st.subheader('Cover Page')
	with col4: st.subheader('Title')
	with col5: st.subheader('Notes')
	with col6: st.subheader('Collected')
	with col7: st.subheader('Condition')
	with col8: st.subheader('Value')

	for index, row in scope.comics_file.iterrows():
		# print( 'Volumne = ', row['volume'], 'Issue No = ', row['issue_no'])
		path_to_comic_cover = path_comic_cover(scope, row['series'], row['volume'], row['issue_no'])

		print(path_to_comic_cover)
		image = Image.open(path_to_comic_cover)



		with col1: st.write(row['issue_no'])
		with col2: st.write(row['cover_date'])
		with col3: st.write('picture here rob')
		with col3: st.image(image, caption='Enter any caption here')
		with col4: st.write(row['title'])
		with col5: st.write(row['notes'])
		with col6: st.write(row['collected'])
		with col7: st.write(row['condition'])
		with col8: st.write(row['value'])


		

# '/Users/robhay/git_repo/collections/files/comic_covers/Star_Wars_Vol_1_19.jpg'
# Users/robhay/git_repo/collections/files/comic_covers/Star_Wars_Vol_1_1.jpg'


	# st.dataframe(scope.comics_file, 2000, 1200)



# series
# volume
# issue_no
# title
# cover_date
# collected
# condition
# value 
# notes


# series,		volume,	issue_no,	title,	cover_date,	collected,	condition,	value,	notes
# Star Wars,	1,		1,			,		,			1,			,50			,
# Star Wars,	1,		1.1,		,		,			,			,400		,35cent edition with UPC code
# Star Wars,	1,		2,			,		,			1,			,			30,