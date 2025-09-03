import configparser
import os

FILE_PATH = "config.ini"
config = configparser.ConfigParser()

def init() -> None:
    if not os.path.exists(FILE_PATH):
        config["timer"] = {
            "tomato": "25",
            "break": "5",
            "long_break": "15",
            "show_notifications": "true"
        }

        save_file()

def get_settings() -> dict:
    config.read(FILE_PATH)
    settings = {
        "tomato": config.getint("timer", "tomato"),
        "break": config.getint("timer", "break"),
        "long_break": config.getint("timer", "long_break"),
        "show_notifications": config.getboolean("timer", "show_notifications")
    }

    return settings

def update_setting(section: str, setting: str, value: str) -> None:
    if value == None or value == "None":
        return
    config.set(section, setting, value)
    save_file()

def save_file() -> None:
    with open(FILE_PATH, 'w') as config_file:
        config.write(config_file)
