import tkinter
from typing import Type

class TypeSpeed():

    def __init__(self):
        window = tkinter.Tk()
        window.title("Speed Typer")
        window.minsize(width=800, height=800)
        window.config(padx=10, pady=10)


        window.mainloop()



ts = TypeSpeed()