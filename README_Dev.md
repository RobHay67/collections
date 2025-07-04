
# Developer Notes

## Utilise the UV package and project manager
### https://docs.astral.sh/uv/

|   |  |
|---|-----------|
| a | virtual environments|
| b | python version|
| c | package installation and management|

<br>


## UV Workflow (new project)
|Step|Tool|Details| Command Line (Terminal)			|
|---|---		|-----------														|------------ |
| 1	| Git		| Create new project on GitHub										|
| 2	| Terminal	| Clone Git Repo to local machine									| git clone https://github.com/RobHay67/Pluto_blue.git |
| 3	| UV	    | Create UV Managed Project								            | uv init { project name }  |
| 3	| UV	    | Initialise UV  (cd into project folder)							| uv init |
| 4	| UV	    | Set Python Version 												| uv python pin 3.12.0 |
| 8	| UV	    | Run project which automatically activates the virtual environment | uv run streamlit run streamlit_app.py |
| 3	| UV        | cleanup - delete the main.py file        							| rm main.py |
| 3	| .gitignore| cleanup - delete the main.py file        							| rm main.py |
| 3	| log_file  | cleanup - delete the main.py file        							| rm main.py |
| 3	| log_file  | cleanup - delete the main.py file        							| rm main.py |



## UV Python Management
|Step|Tool|Details| Command Line (Terminal)			|
|---|---		|-----------														|------------ |
| 5	| UV	    | Help - List all UV options										| uv --help |
| 4	| UV	    | Which Python Versions are available								| uv python list |
| 8	| UV		| Download/Install Specific Version of Python						| uv python install 3.12.3 |
| 4	| UV	    | Set Python Version 												| uv python pin 3.12.0 |



## UV Package Management
### https://docs.astral.sh/uv/getting-started/features/
|Step|Tool|Details| Command Line (Terminal)			|
|---|---		|-----------														|------------ |
| 5	| UV	    | Help - List all UV options										| uv --help |
| 5	| UV	    | Install Packages 													| uv add streamlit |
| 6	| UV		| Remove a package (latest)											| uv remove streamlit |
| 7	| UV	    | Check for Package conflicts or missing dependencis				| uv pip check |



<br>
<br>

## Workflow (Download project to new machine)
|Step|Tool|Details|
|---|---|-----------|
| B	|Terminal	| Clone Git Repo to local machine|
| B	|Terminal	| Clone Git Repo to local machine|
| B	|Terminal	| Clone Git Repo to local machine|
| B	|Terminal	| Clone Git Repo to local machine|

<br>
<br>


## Git Commands
|Step|Tasks										|Command Line (Terminal)|
|---|-----------								|-----------|
| 1 |Log into GitHub and create project			|https://www.github.com|
| 2 |Navigate to project parent folder			| cd {project parent folder}|
| 2 |Create project folder and Clone repo		|git clone https://github.com/RobHay67/Pluto_blue.git|
|	|Cd into the project folder					| cd {project folder} 
|   |Push Local brach to GitHub					|git push -u origin {branch name i.e master} |
|	|delete local branch						|git branch -d {branch name i.e master} |
|   |create new branch                          |git branch new_branch_name|
|   |create merge feature branch into master    |git checkout main |
|   |                                           |git merge feature_branch|

<br>
<br>

## Terminal Commands (Python and Pip / Pip3)
|Step|Tasks										|Command Line (Terminal)|example|
|-------|-----------								|-----------|-----------|
|python |download python version from web			|https://www.python.org/downloads/|
|terminal|check installed python versions			|check machine Applications folder to see installed versions|
|python	|Show ALL versions and paths				|which -a python python2 python2.7 python3 python3.6 python3.13|
|python	|											|which -a python3|
|python	|											|which -a python3.13|
|python |Show Python version (system)				|python --version | Python 3.13.8 |
|python |Show PATH to current version				|where python	|/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 |
|Pip   	|package list (for system)					|pip list / pip3 list|
|Pip   	|Install a package							|pip3 install {package_name}|
|Pip   	|Upgrade a package							|pip3 install --user --upgrade django|

<br>
<br>

## Visual Studio Code (VSC)
### Set Up **Pipenv** Project to work seamlessly with VSC
https://benjaminpack.com/blog/vs-code-python-Pipenv/
|Task												|Command Line (Terminal)|
|-----------|-----------|
|CD into Project File								|cd [project_folder]|
|Ensure that Pipenv has been set up					|(see above)|
|Determine Path to Pipenv Setup File				|Pipenv --py|
|Create project settings file fo VS Code to use		|mkdir .vscode && touch .vscode/settings.json|
|Open the Settings File and paste in the following	|Change the VirtualENV path to yours|
```
	{
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "**/*.pyc": true,
        "**/__pycache__": true
    },
    "python.pythonPath": "<VIRTUALENV_PYTHON_PATH_HERE>",
	"python.defaultInterpreterPath": "<VIRTUALENV_PYTHON_PATH_HERE>",
	}
```
Restart VSC Project by File/Open Folder/[choose your project]

<br>
<br>

### pip show Pipenv
##### show where the package is installed


## Template Table 
|Header_1|Header_2|
|-----------|-----------|
|text|text|
|text|text|

pip3 show pandas > will detail the package including its location (handy)

https://bilard.medium.com/change-python-version-in-pipenv-1ac7b8f9b7b9

A recent upgrade to Ubuntu 20.04 messed up one of my projects which depended on python3.7 and I had to switch over to a higher version, however, it took a lot of googling, trial and error before I figured out how to make the switch in Pipenv.
Here’s a step by step guide on how to do this:
1. Change the “python_version” variable in your Pipfile to the new version you want. In my case it was
python_version = “3.8”
2. Open your terminal and run
pipenv install --python=/path/to/your/python
This would remove the previous virtual environment and create a new one using the python version specified.
Hope this helps :)

pipenv install --python=/Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13




virtualenv : 	packages in env/ then modify PATH - relies on requirements.txt
pipenv:			same as above but kinda slow
venv:			same as virtualenv > lightweight VE with their won site directions in isolation