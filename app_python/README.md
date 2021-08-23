# Python app

This app is a simple Flask application that displays the current time in Moscow.
The Black formatter is used (by VS Code) to ensure that the code is formatted correctly.
Flask was chosen as the web framework because it is very simple to use and has a very simple API.
It helps bootstrap the app quickly and is very easy to extend.
It also does not compromise on powerfulness and increases the readability of the code and productivity of the developer.

## Installing

First, create a virtual environment for the project:

```
python -m venv venv
```

and activate it using the appropiate command for your OS.

The dependencies are listed in the `requirements.txt` file (using `pip freeze`) and can be installed using:

```
pip install -r requirements.txt
```

## Running

Either run the app directly from the command line:

```
python app.py
```

or using the `flask` command:

```
flask run
```

or use the provided Dockerfile to run for production:

```
docker build -t python-app .
docker run -d -p 5000:5000 python-app
```
