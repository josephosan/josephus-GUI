import tkinter as tk
from logic.survivingPosition import survivor_number_binary
from utils.utils import main_circle
from config.config import background_color, input_bg_color, text_color
from config.config import killing_speed


class MainFrame:
    def __init__(self):
        self.reload_btn = None
        self.win_text = None
        self.win_window = None
        self.winning_sit = None
        self.run_loop_btn = None
        self.number = None
        self.current = None
        self.canvas = None
        self.kill_btn = None
        self.kill_all_btn = None
        self.null_text = None

        root = tk.Tk()
        self.root = root

        photo_icon_circle = tk.PhotoImage(file="assets/rec.png")
        self.photo_icon_cup = tk.PhotoImage(file="assets/trophy.png")
        root.title("Josephus problem")
        root.minsize(300, 200)
        root.geometry("800x720+350+10")
        root.iconphoto(False, photo_icon_circle)
        # root.configure(bg=background_color)

        # input label:
        self.null_text = tk.Label(text="\n", font=("Times", 50))
        self.null_text.pack()

        self.entry_label = tk.Label(text="Enter you Number: ", foreground=text_color, font=("Times", 24), pady=10)
        self.entry_label.pack()

        # entry for number:
        self.number_entry = tk.Entry(justify="center", bg=input_bg_color, width=30, borderwidth=10, relief=tk.FLAT,
                                     font=("Times", 15))
        self.number_entry.pack()

        # button:
        ok_image = tk.PhotoImage(file="assets/checked.png")
        self.start_button = tk.Button(root, image=ok_image, borderwidth=0, pady=20, command=self.view_result)
        self.start_button.pack()

        root.mainloop()

    def view_result(self):
        try:
            self.number = int(self.number_entry.get())
        except:
            raise Exception("Enter a valid number.")

        if self.number == 0:
            return

        # kill all elements and reBuild the frame:
        self.start_button.destroy()
        self.number_entry.destroy()
        self.entry_label.destroy()

        winning_sit = survivor_number_binary(self.number)

        self.winning_sit = tk.Label(text=f"The Winning sit is: {winning_sit}", foreground=text_color,
                                    font=("Times", 10))
        self.winning_sit.pack()
        self.run()

    def run(self):
        self.null_text.destroy()

        self.canvas = tk.Canvas(self.root, bg="white", width=700, height=500)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        window_data = {
            "window_width": self.root.winfo_width(),
            "window_height": self.root.winfo_height()
        }

        self.current = main_circle(self.number, self.canvas.create_oval, self.canvas.create_text, window_data)

        self.kill_btn = tk.Button(text="Kill", command=self.kill_next, borderwidth=0)
        self.kill_btn.pack()

        self.kill_all_btn = tk.Button(text="Kill all", command=self.kill_all, borderwidth=0)
        self.kill_all_btn.pack()

    def kill_next(self):
        if self.current.after == self.current.after.after:
            self.canvas.itemconfig(self.current.after.data["data"], fill="green")
            self.kill_btn.destroy()
            self.kill_all_btn.destroy()
            self.winner()
            return
        self.canvas.itemconfig(self.current.data["data"], fill="green")
        self.canvas.itemconfig(self.current.after.data["data"], fill="red")
        self.canvas.itemconfig(self.current.after.after.data["data"], fill="black")

        self.current.after = self.current.after.after
        self.current = self.current.after

    def kill_all(self):
        self.kill_all_btn["state"] = "disable"
        self.kill_btn["state"] = "disable"
        for i in range(self.number):
            self.kill_next()
            self.tkSleep(killing_speed(self.number))

    def tkSleep(self, time: float) -> None:

        self.root.after(int(time * 1000), self.root.quit)
        self.root.mainloop()

    def winner(self):
        self.root.iconphoto(False, self.photo_icon_cup)
        self.kill_btn.destroy()
        self.kill_all_btn.destroy()
        # self.reload_btn = tk.Button(text="Exit", command=self.destroy_self)
        # self.reload_btn.pack()

    def destroy_self(self):
        self.root.destroy()
