# baseframe.py
import tkinter as tk


class BaseFrame(tk.Frame):
    def __init__(self, window, controller):
        super().__init__(master=window)
        self.controller=controller

if __name__ == "__main__":
    pass