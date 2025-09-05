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

If this command does not work, you may need to specify imports. Use this command instead:
`pyinstaller --onefile --windowed --icon imgs/tomato.ico --paths src --hidden-import=desktop_notifier --hidden-import=desktop_notifier.resources --hidden-import=playsound  main.py`

After, copy the imgs/ and sounds/ directory into dist. You may also need to include the default config.ini file.

### From Release

Simply download the .zip in the release, and extract and run the .exe. Only works for windows.

### Updates

Keep in mind that this program does not auto-update. Make sure to check occasionally for new releases.

## Contributing

Contributions to the project are welcome.