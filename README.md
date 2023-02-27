# Python Project Example

This is meant to be a boilerplate repo that shows you how to setup a
python project that uses developer tools such as

1. pre-commit - when you run `git commit` a set of user defined tests will
automatically be run on your code before the commit is allowed to complete. If
any of the tests fail, the commit will fail and you will need to fix the errors
and try again. This prevents bad commits from making it into the repo.
<https://pre-commit.com/>
2. poetry - this is a dependency management tool that keeps track of all the
required modules needed to run your project. When you want to use your project
on another computer, or update the modules you are using, poetry makes this
easy and automatic. <https://python-poetry.org/docs/>
3. github actions - this allows you to automatically run tests on code that are
commited to the remote repo. It can be activated by various events like pull
requests. An example use case is when a pull request is made on the main
branch, a set of actions can be triggered and the code must pass for the pull
request to be completed. <https://docs.github.com/en/actions>
4. virtualenv - this is one of the popular virtual environment managers.
<https://realpython.com/python-virtual-environments-a-primer/#the-virtualenv-project>
5. pytest - this is a unit testing module that makes testing python code easy.
<https://realpython.com/pytest-python-testing/>
6. cmd module - this is a module that makes creation of command line interfaces
in python easy. <https://docs.python.org/3/library/cmd.html>
7. logging module - this is a module that makes logging easy.
<https://betterstack.com/community/guides/logging/how-to-start-logging-with-python/>
8. pytorch module - the ubiquotous machine learning module for python. The
cuda version will be installed allowing you to train machine learning algorithms
using a GPU. If you do not have a supported GPU, this may fail to install.
<https://pytorch.org/>

## How to use this project

1. Make sure the version of python you want to work with is installed on the
machine you will be working with. If you are ok with using the pre-installed
system version you can use that. This project requires Python 3.8+. To install
a different version of python I recommend using the deadsnakes PPA.\
`sudo add-apt-repository ppa:deadsnakes/ppa`\
`sudo apt update`\
`sudo apt install python3.XX`
2. Make sure poetry is installed.
Follow the instructions for installing poetry using the script method.
I recommend you do not use `pipx` or `pip` to install poetry as the version
you get tends to be older. This project was made with poetry v1.3.2.\
`curl -sSL https://install.python-poetry.org | python3 -`
3. Make sure virtualenv is installed. Other python virtual environment managers
should work, but this has only been tested using virtualenv. Having anaconda installed
has given me problems making this work in the past. If you use anaconda just for 
virtual environment management, I recommend uninstalling anaconda and using virtualenv.\
`pip install virtualenv`
4. Create the virtual environment.\
`mkdir -p ~/virtualenvs && virtualenv -p /usr/bin/python3.XX ~/virtualenvs/pyexamp`
5. Activate the virtual environment you just created.\
`source ~/virtualenvs/pyexamp/bin/activate`
6. `git clone git@github.com:rcbell1/pyProjExample.git`
7. `cd pyProjExample`
8. Now let poetry install all the dependencies defined in the pyproject.toml
file.\
`poetry install`
9. Install the pre-commit tests to this git repo.\
`pre-commit install`
