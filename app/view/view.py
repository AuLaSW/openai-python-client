# view.py
import tkinter as tk
"""
Class View:

Manages the GUI, interacts with the Controller and Model classes.

This class uses tkinter to generate the GUI.
"""


class View:
    def __init__(self, controller):
        # bind the controller to the view object
        # by passing the controller to the view,
        # we can bind controller functions to view
        # functions
        self.controller = controller

        # the Window class will be directly
        # interacting with the tkinter package
        # this will give us specific frames and
        # windows to call and use without having
        # to go through tkinter directly
        self.window = Window()


if __name__ == "__main__":
    pass