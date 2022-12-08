import tkinter as tk


class MyFrame:
    def __init__(self):
        root = tk.Tk()
        self.root = root

        root.title("Josephus problem")
        root.minsize(300, 200)

        # input label:
        self.entry_label = tk.Label(text="Enter you Number: ")
        self.entry_label.pack()

        # entry for number:
        self.number_entry = tk.Entry(justify="center")
        self.number_entry.pack()

        # button:
        self.start_button = tk.Button(text="Ok", command=self.run)
        self.start_button.pack()

        root.mainloop()

    def run(self):
        try:
            number = int(self.number_entry.get())
        except:
            raise Exception("Enter a valid number.")

        if number == 0: return

        # kill all elements and reBuild the frame:
        self.start_button.destroy()
        self.number_entry.destroy()
        self.entry_label.destroy()

        self.root.minsize(400, 400)