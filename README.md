# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Trello Secrets
Create a trello account at https://trello.com 

You can get your API key by logging into Trello and visiting https://trello.com/app-key
On the same page, click the hyperlinked "Token" under the API key to generate your API token.

To generate the Board ID run a GET API request on the following url: https://api.trello.com/1/members/me/boards?key={yourKey}&token={yourToken} 

Update the Trello secrets in the .env.template file and or the .env file.

The lists used in Trello for testing were: "Not Started", "In Progress", "Peer Review", "On Hold", "Completed".

## Testing with PyTest
The lists used in Trello for testing were: "Not Started", "In Progress", "Peer Review", "On Hold", "Completed", "To Do", "Doing", "Done" - in that order left to right on trello.

For Not Started, include 3 cards called "Item 1", "Item 9" and "Item 10" (in that order)

For "In Progress" create 2 cards called "Item 5" and "Item 7" (In that order)

For "Peer Review" create 2 cards called "Item 4" and "Item 6" (In that order)

For "On Hold" create 1 card called "Item 2"

For "Completed" create 1 card called "Item 3"

for "To Do" create 1 card called "To Do Card"

for "Doing" create 1 card called "Doing Card"

For "Done" create 1 card called "Done Card"

In Visual Studio Code, press ctrl + shift + p and select "Python: Configure Tests", select "pytest" and then "todo_app"

Select the beaker icon in visual studio code, and click the play button in the test explorer section of the window.

To run from the command line, open cmd / powershell in the devops_course_starter folder, and run "poetry run pytest"

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.
