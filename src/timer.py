import tkinter as tk

timer_states = {"tomato": 5, "break": 3, "long_break": 10}

class Timer:
    current_state = "tomato"
    current_time = -1
    timer_text = "00:00"
    tomatos = 0
    paused = True

    def __init__(self, root) -> None:
        self.root: tk.Tk = root
        self.start_timer()
    
    def update_timer(self) -> None:
        if not self.paused:
            minutes, seconds = divmod(self.current_time, 60)
            self.timer_text = f"Time left: {minutes:02d}:{seconds:02d}"
            self.current_time -= 1
        if self.current_time < 0:
            self.switch_state()
        else:
            self.root.after(1000, self.update_timer)

    def switch_state(self) -> None:
        if self.current_state == "tomato":
            self.tomatos += 1
            if self.tomatos % 4 == 0 and self.tomatos != 0:
                self.current_state = "long_break"
            else:
                self.current_state = "break"
        elif self.current_state == "break" or self.current_state == "long_break":
            self.current_state = "tomato"
        self.paused = True

    def start_timer(self) -> None:
        if self.paused:
            self.paused = False
            if self.current_time < 0:
                self.current_time = timer_states[self.current_state]
                self.update_timer()
    
    def pause_timer(self) -> None:
        self.paused = True
    
    def stop_timer(self) -> None:
        self.paused = True
        self.current_time = -1
