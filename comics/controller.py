from numpy import issubsctype
import streamlit as st

# from comics.view.comics import render_comics_star_wars
from comics.model.series import series_selector


# series
# volume
# issue_no
# title
# cover_date
# collected
# condition
# value 
# notes

def update_collected(scope, i, widget_key):
	print('updated collected - ', i)

	changed_value = scope[widget_key]

	# store the selection
	# scope.user_df.at[user_name, df_col_name] = changed_value

	print('we want to update the comic_df')
	print('but we dont have a key for the df. So how do we update')



def widget_collected(scope, i):

	issue_no = str(scope.comic_issue_list[i])

	widget_key = 'widget_collected_' + issue_no

	st.checkbox(
				label='Collected',
				key=widget_key,
				on_change=update_collected,
				args=(scope, i, widget_key)
				)




def render_comic_details(scope, i):
	
	issue_no = str(scope.comic_issue_list[i])
	title = str(scope.comic_title_list[i])
	note = str(scope.comic_notes_list[i])

	

	if title == 'nan': title = 'Missing Title for this Issue'
	# if note == 'nan': title = ''

	comic_cover = scope.comic_covers[issue_no]

	st.header(issue_no)

	widget_collected(scope, i)



	st.image(comic_cover, caption=title)
	if note != 'nan':
		st.caption(note)
	


def render_comics_page(scope):

	st.title('Comic Collection Hi Fliss')

	col1,col2=st.columns([4,8])

	with col1: series_selector(scope)

	# sort the comics_df by issue_no
	scope.comic_df.sort_values(by='issue_no')
	no_of_comics = len(scope.comic_df)
	scope.comic_issue_list = list(scope.comic_df['issue_no'])
	scope.comic_title_list = list(scope.comic_df['title'])
	scope.comic_notes_list = list(scope.comic_df['notes'])


	for i in range(0, no_of_comics, 4):
		col1,col2,col3,col4=st.columns([2,2,2,2])
		with col1: render_comic_details(scope, i, )
		with col2: render_comic_details(scope, i+1)
		with col3: render_comic_details(scope, i+2)
		with col4: render_comic_details(scope, i+3)

	st.write(scope.comic_df)






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
