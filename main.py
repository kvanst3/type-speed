import tkinter as tk
import math

class TypeSpeed():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Speed Typer")
        self.window.minsize(width=700, height=700)
        self.window.config(padx=10, pady=10)

        self.time_label = tk.Label(text="Time Left: 60")
        self.time_label.pack(expand=True)

        self.listbox = tk.Listbox()
        self.listbox.pack(expand=True, fill='both')

        string_listener = tk.StringVar()
        string_listener.set("Init Text")
        string_listener.trace("w", self.text_changed)

        self.entry_widget = tk.Entry(self.window, textvariable=string_listener)
        self.entry_widget.pack(expand=True, fill='x')

        self.count = 60
        self.count_switch = False

        self.window.mainloop()



    def text_changed(self, *args):
        print("Text changed.")
        if self.count_switch is False:
            self.count_down()
            self.count_switch = True

    def count_down(self, *args):
        secs = self.count
        if secs < 10:
            secs = f"0{secs}"

        self.time_label.config(text=f"Time Left: {secs}")
        if self.count <= 0:
            print('Times up!')
        else:
            self.window.after(1000, self.count_down)
            self.count -= 1


ts = TypeSpeed()