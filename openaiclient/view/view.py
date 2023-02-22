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
        self._controller = controller

    def settingsWindow(self):
        """
        Create a default settings window with default settings, for testing
        purposes only
        """
        newWindow = tk.Tk()
        newWindow.resizable(False, False)
        frame = SettingsWindow(newWindow, self._controller)
        frame.draw()

    def completionSettingsWindow(self):
        """
        Create a completion settings window with settings from the
        CompletionRequest class
        """
        newWindow = tk.Tk()
        newWindow.resizable(False, False)
        frame = CompletionSettingsWindow(newWindow, self._controller)
        frame.draw()

    def completionInputWindow(self):
        """
        Create a completion input window for writing prompts for the OpenAI API
        """
        newWindow = tk.Tk()
        frame = CompletionInputWindow(newWindow, self._controller)
        frame.draw()


if __name__ == "__main__":
    from openaiclient.controller.controller import Controller
    from tests.unit.fixture import api

    controller = Controller(api)
    controller.compReq()
    controller.view.completionInputWindow()
