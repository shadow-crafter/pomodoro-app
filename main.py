import time
from tkinter import Tk, Frame, Button

timer_states = {"tomato": 25, "break": 5, "long_break": 15}

class Timer:
    current_state = "tomato"
    current_time = -1
    tomatos = 0
    paused = False

    def __init__(self) -> None:
        pass

    def run(self) -> None:
        self.current_time = timer_states[self.current_state]
        while self.current_time > 0:
            if self.paused:
                print("Timer paused...")
            print(f"Time left: {self.current_time}")
            self.current_time -= 1
            time.sleep(1)
        self.tomatos += 1
        self.switch_state()
    
    def switch_state(self) -> None:
        if self.current_state == "tomato":
            if self.tomatos % 4 == 0 and self.tomatos != 0:
                self.current_state = "long_break"
                self.tomatos = 0
            else:
                self.current_state = "break"
        elif self.current_state == "break" or self.current_state == "long_break":
            self.current_state = "tomato"
        self.run()

def create_window() -> None:
    root: Tk = Tk()
    frm: Frame = Frame(root)
    frm.pack()

    button: Button = Button(frm, text="Hello, world >w<")
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    timer = Timer()
    timer.run()
    create_window()
