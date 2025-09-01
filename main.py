from src.timer import Timer
from tkinter import Tk, Frame, Button, Label

def create_window(root: Tk, timer: Timer):
    base_frame: Frame = Frame(root)
    base_frame.pack()

    label: Label = Label(base_frame, text="Hello, world >w<")
    start_button: Button = Button(base_frame, text="Start", command=timer.start_timer)
    start_button.pack()
    pause_button: Button = Button(base_frame, text="Pause", command=timer.pause_timer)
    pause_button.pack()

if __name__ == "__main__":
    #timer.run()
    root: Tk = Tk()
    root.geometry('640x320')

    timer = Timer(root)
    create_window(root, timer)
    root.mainloop()
