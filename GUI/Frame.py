import tkinter as tk
from logic.survivingPosition import survivor_number_binary
from utils.utils import main_circle
import time as t


class MyFrame:
    def __init__(self):
        self.number = None

        root = tk.Tk()
        self.root = root

        root.title("Josephus problem")
        root.minsize(300, 200)
        root.geometry("800x700+350+10")

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

    def kill_next(self):
        if self.current.after == self.current.after.after: return
        self.canvas.itemconfig(self.current.data["data"], fill="green")
        self.canvas.itemconfig(self.current.after.data["data"], fill="red")
        self.canvas.itemconfig(self.current.after.after.data["data"], fill="black")

        self.current.after = self.current.after.after
        self.current = self.current.after

