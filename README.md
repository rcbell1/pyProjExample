# Python Project Example

This is meant to be a boilerplate repo that shows you how to setup a
python project that uses developer tools such as

1. pre-commit - when you run `git commit` a set of user defined tests will
automatically be run on your code before the commit is allowed to complete. If
any of the tests fail, the commit will fail and you will need to fix the errors
and try again. This prevents bad commits from making it into the repo.
2. poetry - this is a dependency management tool that keeps track of all the
required modules needed to run your project. When you want to use your project
on another computer, or update the modules you are using, peotry makes this
easy and automatic.
3. github actions - this allows you to automatically run tests on code that was
commited to the remote repo. It can activated on various events like pull
requests. An example use case is that when a pull request is made on the main
branch, a set of actions can be triggered and the code must pass for the pull
request to be considered.
4. pytest - this is a unit testing module that makes testing python code easy.
5. cmd module - this is a module that makes creation of command line interfaces
in python easy.
6. logging module - this is a module that makes logging easy
