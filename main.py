from src.app import PomodoroApp
from src.settings import init

def main() -> None:
    init()
    app = PomodoroApp()
    app.root.mainloop()

if __name__ == "__main__":
    main()
