# Pomodoro App

This app is a simple [pomodoro timer](). Built with Python and Tkinter.

## Installtion

### From Source Code

- Firstly, <b>make sure that you have</b> [Python](https://www.python.org/downloads/) and PIP installed and working.

- Next, extract the project and place it somewhere <b>that makes sense to you.</b>

Once these steps are done, you need to install the dependencies.
To do this, follow these steps:

- Open your terminal, and navigate to the project.
- (Optional, but reccommended) create a venv environment first in the project with this command: `python -m venv venv`
- If you decide to use venv, activate it with `./venv/scripts/activate`
- Now install the dependencies by running `pip install -r requirements.txt`
- Finally to create the .exe, run `pip install pyinstaller`, then `pyinstaller --onefile --windowed --icon imgs/tomato.ico main.py`

### From Release

TBA

### Updates

Keep in mind that this program does not auto-update. Make sure to check occasionally for new releases.

## Contributing

Contributions to the project are welcome.