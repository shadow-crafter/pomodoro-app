import ctypes
from src.timer import Timer
from tkinter import Tk, Frame, Button, Label, StringVar, PhotoImage

appid = u'shadowcrafter.py_pomodoro_app.1.0'

def create_window(root: Tk, timer: Timer):
    base_frame: Frame = Frame(root)
    base_frame.pack()

    label: Label = Label(base_frame, text="Hello, world >w<")
    label.pack()

    state_text_var: StringVar = StringVar()
    state_label: Label = Label(base_frame, textvariable=state_text_var)
    state_label.pack()
    tomatos_text_var: StringVar = StringVar()
    tomato_label: Label = Label(base_frame, textvariable=tomatos_text_var)
    tomato_label.pack()
    timer_text_var: StringVar = StringVar()
    timer_label: Label = Label(base_frame, textvariable=timer_text_var)
    timer_label.pack()

    def update_labels():
        if not timer.paused:
            state_text_var.set(timer.current_state)
        else:
            state_text_var.set("paused")
        tomatos_text_var.set(f"Tomatos: {timer.tomatos}")
        timer_text_var.set(timer.timer_text)
        root.after(100, update_labels)
    
    update_labels()

    start_button: Button = Button(base_frame, text="Start", command=timer.start_timer)
    start_button.pack()
    pause_button: Button = Button(base_frame, text="Pause", command=timer.pause_timer)
    pause_button.pack()

if __name__ == "__main__":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid) #identifier so icon loads

    root: Tk = Tk()
    root.title("Pomodoro Timer")
    root.iconphoto(True, PhotoImage(file="imgs/tomato.png"))
    root.geometry('640x320')

    timer = Timer(root)
    create_window(root, timer)

    root.mainloop()
