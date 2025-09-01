from src.timer import Timer
from tkinter import Tk, Frame, Button

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
