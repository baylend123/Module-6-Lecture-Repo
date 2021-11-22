'''
Pip, Virtualenv, and Pipenv
    pyenv: version manager for Python
    pip: package manager for Python (but only works for globally installing packages)
    virtualenv: the environment containing a specified python version and a collection of installed packages(in a .venv folder)
    pipenv: dependency manager for individual projects
'''
'''
Pip, Virtualenv, and Pipenv
Python tool	Node.js equivalent
    pyenv |	nvm
    pip	 |  npm --global
    virtualenv  |	nvm + node_modules
    pipenv  |	npm + nvm
    Pipfile  |	package.json
    Pipfile.lock  |	package-lock.json
'''

'''
Using pipenv
Create a virtual environment by running pipenv install. 
If there is a Pipfile present, this will install the dependencies 
in the Pipfile, otherwise it will create a new Pipfile along with a virtual environment.

You can specify a particular version of Python to use in your virtual environment with --python flag.
'''

# pipenv install --python 3.9.4
# You can also pass in a path instead of a number .
# pipenv install --python "/Users/username/.pyenv/versions/3.9.4/bin/python"

'''
Specifying a Python version (note for projects this week)
Many of the projects this week will specify a version of Python to use. 
If you try to use a version that you don’t have installed, it will not work. 
Also, these projects expect you to be specifying the path instead of just a number.

    If you see something like this
        pipenv install --python "$PYENV_ROOT/versions/3.8.3/bin/python"

    Run this instead:
        pipenv install --python 3.9.4 # or whatever version you do have installed
If you aren’t sure, you can check to see which version you have available with 
the command

 pyenv versions.
'''

'''
Installing packages with pipenv
    Install a dependency:
        pipenv install package-name
    
    Install a development-only dependency:
        pipenv install --dev package-name
    Uninstall a dependency:
        pipenv uninstall package-name


More pipenv commands
    Activate your virtual environment shell:
        pipenv shell

    Remove a virtual environment:
        pipenv --rm
'''

