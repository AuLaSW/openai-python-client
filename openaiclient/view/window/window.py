"""
This module creates windows for the openai-client program.

API:
    completionSettingsWindow():
        This creates the completion settings frame and attaches packs in into
        the current window.
"""
import tkinter as tk
from openaiclient.view.frame.settings.completionsettings import CompletionSettings


class Window:
    """
    This class generates and manages the different windows the program uses.

    Functions
    ---------

    __init__(self, controller):
        Initializes the window.

    completionSettingsWindow(self):
        Generates a completion settings window.
    """

    def __init__(self, controller):
        # the main window
        self.window = tk.Tk()
        # the controller managing the window
        # and the models
        self.controller = controller
        # the frame that will be packed onto the
        # window
        self.frame = None

    # function for drawing the window given the frame
    # the window will hold. Allows for a window to be
    # reset without starting a new window instance.
    def completionSettingsWindow(self):
        """Generates a window for the completion settings"""
        self.frame = CompletionSettings(self.window, self.controller)
        self.frame.pack()


if __name__ == "__main__":
    pass
