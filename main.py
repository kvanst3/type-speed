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

        self.text_widget = tk.Text()
        self.text_widget.pack(expand=True, fill='both')
        self.text_widget.config(state="disabled")


        self.string_listener = tk.StringVar()
        self.string_listener.set("Init Text")

        self.entry_widget = tk.Entry(self.window, textvariable=self.string_listener)
        self.entry_widget.pack(expand=True, fill='x')

        self.count = 60
        self.count_switch = False

        self.window.bind("<space>", self.text_changed)
        self.entry_widget.bind('<FocusIn>', lambda x: self.entry_widget.delete(0, 'end'))

        self.wordlist = ['date', 'the', 'old', 'hag', 'ok?']

        self.window.mainloop()

    def delete_text(self):
        self.string_listener.delete(0, "end")

    def text_changed(self, *args):
        self.string_listener.set(" ")
        print("here")
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