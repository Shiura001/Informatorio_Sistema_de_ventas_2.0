import tkinter as tk
from customtkinter import *

def clean(canvas):
    if canvas.winfo_exists():
        for widget in canvas.winfo_children():
            widget.destroy()
        

