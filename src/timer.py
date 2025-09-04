import asyncio
from desktop_notifier import DesktopNotifier, Icon
from pathlib import Path
import playsound
from src.settings import get_settings, update_setting
import threading
import tkinter as tk

SOUND_PATH = "sounds/alarm.mp3" #sound used is from https://pixabay.com/sound-effects/timer-terminer-342934/, feel free to modify it

#specific loop for handling notifications
notification_loop = asyncio.new_event_loop()
def start_notification_loop():
    asyncio.set_event_loop(notification_loop)
    notification_loop.run_forever()
notification_thread = threading.Thread(target=start_notification_loop, daemon=True)
notification_thread.start()

class Timer:
    current_state: str = "tomato"
    current_time: int = -1
    paused: bool = True
    settings: dict = {}
    timer_states: dict = {}
    timer_text: str = "00:00"
    tomatos: int = 0

    def __init__(self, root) -> None:
        self.root: tk.Tk = root
        self.update_timer_settings()
    
    def update_timer_settings(self) -> None:
        self.settings = get_settings()

        self.timer_states["tomato"] = self.settings["tomato"] * 60
        self.timer_states["break"] = self.settings["break"] * 60
        self.timer_states["long_break"] = self.settings["long_break"] * 60

        self.tomatos = self.settings["tomatos_completed"]
    
    async def send_notification(self, notification_message) -> None:
        notifier = DesktopNotifier(
            app_name="Pomodoro Timer",
            app_icon=Icon(Path("imgs/tomato.png").resolve())
        )
        await notifier.send(
            title="Pomodoro App",
            message=notification_message,
            icon=Icon(Path("imgs/tomato.png").resolve())
        )

    def notify(self, notification_message) -> None: #handles notification thread and sound
        asyncio.run_coroutine_threadsafe(
            self.send_notification(notification_message),
            notification_loop
        )
    
    def update_timer_text(self) -> None:
        if self.current_time > 0:
            minutes, seconds = divmod(self.current_time, 60)
            self.timer_text = f"{minutes:02d}:{seconds:02d}"
        else:
            self.timer_text = "00:00"
    
    def update_timer(self) -> None:
        if not self.paused:
            self.update_timer_text()
            self.current_time -= 1
        if self.current_time < 0:
            self.switch_state()
        else:
            self.root.after(1000, self.update_timer)

    def switch_state(self) -> None:
        if self.paused:
            return
        message = ""

        if self.current_state == "tomato":
            message = "Time's up! Time for a break! (￣o￣) . z Z"
            self.tomatos += 1
            update_setting("timer", "tomatos_completed", str(self.tomatos))
            if self.tomatos % 4 == 0 and self.tomatos != 0:
                self.current_state = "long_break"
            else:
                self.current_state = "break"
        elif self.current_state == "break" or self.current_state == "long_break":
            message = "Time's up! Get back to work! ಠ╭╮ಠ"
            self.current_state = "tomato"
        
        self.paused = True
        self.current_time = -1
        self.update_timer_text()

        playsound.playsound(SOUND_PATH)
        if self.settings["show_notifications"] == True:
            threading.Thread(
                target=lambda: self.notify(message),
                daemon=True
            ).start()

    def start_timer(self) -> None:
        if self.paused:
            self.paused = False
            if self.current_time < 0:
                self.current_time = self.timer_states[self.current_state]
                self.update_timer()
    
    def pause_timer(self) -> None:
        self.paused = True
    
    def stop_timer(self) -> None:
        self.paused = False
        self.switch_state()
