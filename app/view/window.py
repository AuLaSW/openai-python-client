# window.py
import tkinter as tk

"""
Class Window:

An abstract class that builds windows from composite frames.
Frame classes are stacked to creating a single frame that
is added to the window then packed. This creates a dyanmic
window that can change as the user navigates through the UI.

"""


class Window:
    def __init__(self, controller):
        # the main window
        self.window = tk.Tk()
        # the controller managing the window
        # and the models
        self.controller = controller
        # the frame that will be packed onto the
        # window
        self.frame
    
    # function for drawing the window given the frame
    # the window will hold. Allows for a window to be 
    # reset without starting a new window instance.
    def startWindow(self):
        self.frame = StartFrame(self.window, self.controller)
        self.frame.pack()


if __name__ == "__main__":
    pass