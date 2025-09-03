import ctypes
from src.settings import init as settings_init, update_setting
from src.timer import Timer
from tkinter import Tk, Frame, Button, Label, StringVar, PhotoImage, Menu, simpledialog, messagebox

appid = u'shadowcrafter.py_pomodoro_app.1.0'

def create_window(root: Tk, timer: Timer) -> None:
    base_frame: Frame = Frame(root)
    base_frame.pack()

    menu_bar: Menu = Menu(base_frame)
    settings: Menu = Menu(menu_bar, tearoff=0)

    def set_time(paramater: str) -> None:
        new_time = simpledialog.askinteger(
            f"Set {paramater} time",
            f"Enter {paramater} time in minutes:",
            parent=root,
            minvalue=1,
            maxvalue=120)
        update_setting("timer", paramater, str(new_time))
        timer.update_timer_settings()
    
    def set_notification() -> None:
        show_notifications = messagebox.askyesnocancel(
            "Show Notifications",
            "Enable notifications?"
            )
        update_setting("timer", "show_notifications", str(show_notifications))
        timer.update_timer_settings()
        
    settings.add_command(label="Set tomato time", command=lambda: set_time("tomato"))
    settings.add_command(label="Set break time", command=lambda: set_time("break"))
    settings.add_command(label="Set long break time", command=lambda: set_time("long_break"))
    settings.add_command(label="Show notifications", command=set_notification)
    menu_bar.add_cascade(label="settings", menu=settings)

    root.config(menu=menu_bar)

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

    def update_labels() -> None:
        if not timer.paused or timer.current_time < 0:
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
    stop_button: Button = Button(base_frame, text="Stop", command=timer.stop_timer)
    stop_button.pack()

if __name__ == "__main__":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid) #identifier so icon loads

    settings_init()

    root: Tk = Tk()
    root.title("Pomodoro Timer")
    root.iconphoto(True, PhotoImage(file="imgs/tomato.png"))
    root.geometry('640x320')

    timer = Timer(root)
    create_window(root, timer)

    root.mainloop()
