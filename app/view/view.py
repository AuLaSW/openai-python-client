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


if __name__ == "__main__":
    pass