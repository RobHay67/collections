# ------------------------------------------------- Application
# activate pipend	- pipenv shell
# run application	- streamlit run home.py
# ------------------------------------------------- GitHub
# git push -u origin <branch>
# git branch -d <branch>   will delete local branch
# ------------------------------------------------- Package Management
# pip3 install --user --upgrade django
# ------------------------------------------------- Pipenv
# cd into project folder 
# activate Pipenv 	- pipenv shell
# deactivate env	- exit
# install packages  - pipenv install
# add a package 	- pipenv install django
# upgrade package	- 
# specify ver   	- pipenv install mplfinance==0.12.7a5
# latest ver		- pipenv update pandas
# delete pkg		- pipenv uninstall django
# -------------------------------------------------
# configure vscode to work with pipenv
# https://benjaminpack.com/blog/vs-code-python-pipenv/


for i in range(10):print('')
print ( '\033[94m' + 'Application Re-Rendering - see below this line ' + '>'*33 + '\033[0m')
for i in range(5):print('')



import streamlit as st
from config import set_scope


scope = set_scope(st.session_state)


st.title('Robs Hobbies - Collection Databases')



print('-'*77)
print( 'List of all keys in the st.session_state')
print('-'*77)
if 'initial_load' in st.session_state:
	ignore_keys = ['comic_file', 'comic_df', 'comic_covers', 'dvd_file', 'dvd_df', 'dvd_covers']
	for key in sorted(st.session_state):
		print(key)
		# if key not in  ignore_keys:
		# 	print ( key.ljust(40), scope[key])
		# else:
		# 	print(key.ljust(40), 'Dataframe too large to print')
print('-'*77)


















# # Set Up the Initial Streamlit Environment ======================================================================
# from config.streamlit import set_streamlit_page_config
# from scope.scope import set_scope
# from pages.controller import set_initial_scope
# from scope.dropdowns.refresh_selectors import update_dropdowns


# set_streamlit_page_config()
# scope = set_scope(st.session_state, project_description)

# if scope.config['dropdowns']['update_dropdowns']: 
# 	update_dropdowns(scope)

# print ( '\033[94mApplication Refreshed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \033[0m')

# render_selected_page(scope)
# render_sidebar(scope)


