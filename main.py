import time
from tkinter import Tk, Frame, Button

class PomodoroTimer:
    def __init__(self) -> None:
        pass

def create_window() -> None:
    root: Tk = Tk()
    frm: Frame = Frame(root)
    frm.pack()

    button: Button = Button(frm, text="TEST")
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    print("hello there")
    create_window()
