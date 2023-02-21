"""
This module contains the class View, which is part of the MVC pattern for the
openai-client application.

API:
    run():
        Creates the window and starts the mainloop() for it.
"""
from openaiclient.view.window.window import *


class View:
    """
    Class View:

    Manages the GUI, interacts with the Controller and Model classes.

    This class uses tkinter to generate the GUI.
    """

    def __init__(self, controller):
        # bind the controller to the view object
        # by passing the controller to the view,
        # we can bind controller functions to view
        # functions
        self._controller = controller

    def settingsWindow(self):
        newWindow = tk.Tk()
        frame = SettingsWindow(newWindow, self._controller)
        frame.draw()


if __name__ == "__main__":
    from openaiclient.controller.controller import Controller

    view = View(None)

    view.settingsWindow()