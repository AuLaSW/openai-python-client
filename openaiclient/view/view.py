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
        self._root = tk.Tk()
        self._root.resizable(False, False)
        self._frame = None
    
    @property
    def frame(self):
        return self._frame
    
    @frame.setter
    def frame(self, frame):
        self._frame = frame

    def settingsWindow(self):
        """
        Create a default settings window with default settings, for testing
        purposes only
        """
        newWindow = tk.Toplevel(self._root)
        newWindow.resizable(False, False)
        frame = SettingsWindow(newWindow, self._controller)
        frame.draw()

    def completionSettingsWindow(self):
        """
        Create a completion settings window with settings from the
        CompletionRequest class
        """
        newWindow = tk.Toplevel(self._root)
        newWindow.resizable(False, False)
        frame = CompletionSettingsWindow(newWindow, self._controller)
        frame.draw()

    def completionInputWindow(self):
        """
        Create a completion input window for writing prompts for the OpenAI API
        """
        self.frame.destroy()
        window = CompletionInputWindow(self._root, self._controller)
        self.frame = window.draw()

        self._root.mainloop()
    
    def mainWindow(self):
        """
        Create the main splash window for when the program starts
        """
        window = MainWindow(self._root, self._controller)
        self.frame = window.draw()

        self._root.mainloop()


if __name__ == "__main__":
    from openaiclient.controller.controller import Controller
    from tests.unit.fixture import api

    controller = Controller(api)
    controller.view.mainWindow()
