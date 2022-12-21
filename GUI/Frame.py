import tkinter as tk
from logic.survivingPosition import survivor_number_binary
from utils.utils import main_circle
from config.config import project_title


class MyFrame:
    def __init__(self):
        self.winning_sit = None
        self.run_loop_btn = None
        self.number = None
        self.current = None
        self.canvas = None
        self.kill_btn = None
        self.kill_all_btn = None

        root = tk.Tk()
        self.root = root

        root.title(project_title)
        root.minsize(300, 200)
        root.geometry("800x720+350+10")

        # input label:
        self.entry_label = tk.Label(text="Enter you Number: ")
        self.entry_label.pack()

        # entry for number:
        self.number_entry = tk.Entry(justify="center")
        self.number_entry.pack()

        # button:
        self.start_button = tk.Button(text="Ok", command=self.view_result)
        self.start_button.pack()

        root.mainloop()

    def view_result(self):
        try:
            self.number = int(self.number_entry.get())
        except:
            raise Exception("Enter a valid number.")

        if self.number == 0: return

        # kill all elements and reBuild the frame:
        self.start_button.destroy()
        self.number_entry.destroy()
        self.entry_label.destroy()

        winning_sit = survivor_number_binary(self.number)

        self.winning_sit = tk.Label(text=f"The Winning sit is: {winning_sit}")
        self.winning_sit.pack()

        self.run_loop_btn = tk.Button(text="Run", command=self.run)
        self.run_loop_btn.pack()

    def run(self):
        self.run_loop_btn.destroy()

        self.canvas = tk.Canvas(self.root, bg="white", width=700, height=500)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        window_data = {
            "window_width": self.root.winfo_width(),
            "window_height": self.root.winfo_height()
        }

        self.current = main_circle(self.number, self.canvas.create_oval, self.canvas.create_text, window_data)

        self.kill_btn = tk.Button(text="Kill", command=self.kill_next)
        self.kill_btn.pack()

        self.kill_all_btn = tk.Button(text="Kill all", command=self.kill_all)
        self.kill_all_btn.pack()

    def kill_next(self):
        if self.current.after == self.current.after.after:
            self.canvas.itemconfig(self.current.after.data["data"], fill="green")
            return
        self.canvas.itemconfig(self.current.data["data"], fill="green")
        self.canvas.itemconfig(self.current.after.data["data"], fill="red")
        self.canvas.itemconfig(self.current.after.after.data["data"], fill="black")

        self.current.after = self.current.after.after
        self.current = self.current.after

    def kill_all(self):
        for i in range(self.number):
            self.kill_next()
            self.tkSleep(.7)

    def tkSleep(self, time: float) -> None:

        self.root.after(int(time * 1000), self.root.quit)
        self.root.mainloop()
