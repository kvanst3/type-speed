import tkinter as tk
from tkinter.constants import E, LEFT

class TypeSpeed():

    def __init__(self):
        window = tk.Tk()
        window.title("Speed Typer")
        window.minsize(width=700, height=700)
        window.config(padx=10, pady=10)

        self.time_label = tk.Label(text="Time Left")
        self.time_label.pack(expand=True)

        self.listbox = tk.Listbox()
        self.listbox.pack(expand=True, fill='both')

        string_listener = tk.StringVar()
        string_listener.set("Init Text")
        string_listener.trace("w", self.text_changed)

        self.entry_widget = tk.Entry(window, textvariable=string_listener)
        self.entry_widget.pack(expand=True, fill='x')


        window.mainloop()



    def text_changed(self, *args):
        print("Text changed.")



ts = TypeSpeed()