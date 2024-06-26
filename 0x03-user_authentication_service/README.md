# User Authentication Service

## Overview
This project is part of a curriculum focused on short specializations in backend development. The goal is to implement a user authentication service using Python Flask and SQLAlchemy. The service allows users to register, log in, log out, reset passwords, and retrieve user profiles.

### Resources
Read or watch:
- [Flask documentation](https://flask.palletsprojects.com/)
- [Requests module](https://docs.python-requests.org/en/master/)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- You should use SQLAlchemy 1.3.x
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- All your functions should be type annotated
- The flask app should only interact with Auth and never with DB directly
- Only public methods of Auth and DB should be used outside these classes

## Setup
You will need to install bcrypt:

```bash
pip3 install bcrypt
git clone https://github.com/YohanesSenbeto/alx-backend-user-data.git
cd 0x03-user_authentication_service

