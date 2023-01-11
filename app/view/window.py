# window.py
import tkinter as tk

"""
Class Window:

Creates the different windows used by the application and acts
as a buffer between the View class and the tkinter package.

This is an abstract class. All of the windows produced by
the application should have their own class for extensibility
reasons.
"""


class Window:
    def __init__(self, controller):
        self.window = tk.Tk()
        self.controller = controller

        self.window.title("openai-python-client")

    def init(self):
        self.window.mainloop()

    # draw the window
    def draw(self):
        return NotImplementedError()

    # get return value from window
    # if it has a return
    # this should yield a dictionary?
    # haven't decided yet
    def get(self):
        return NotImplementedError()

    def set(self, input):
        return NotImplementedError()


if __name__ == "__main__":
    pass
