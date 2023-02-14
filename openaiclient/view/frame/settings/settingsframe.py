"""
SettingsFrame Module
"""
import tkinter as tk
from openaiclient.view.frame.baseframe import BaseFrame
from openaiclient.view.frame.settingsinputframe import SettingsInputFrame


class SettingsFrame(BaseFrame):
    """
    Class SettingsFrame:

    This class is for a frame that holds settings for
    a user to change. Created to work with the Completion
    and Edit requests to OpenAI.
    """
    def __init__(self, main, controller):
        super().__init__(main, controller)

        # hold the settings we will be using
        self.settings = dict()
        # hold the tk variables for returning inputs from the frame
        self.options = dict()

        # row count
        self.row = 0

    # creates all of the widgets for
    # the frame. This default method
    # can be overriden for different
    # types of input in other settings
    # classes.
    def create(self):
        """
        Creates the settings input frames by looping through the settings
        dictionary (self.settings) and creating a SettingsInputFrame object
        for each setting. It then attaches each frame in the next row on
        the frame with the grid() method.

        Finally, it creates the save and exit buttons and attaches them to
        the settings frame (self).
        """
        for key, value in self.settings, self.settings.items():
            typeOfValue = type(value).__name__

            inputFrame = SettingsInputFrame(
                    self,
                    self.controller,
                    key,
                    value
                    )

            match typeOfValue:
                case "str":
                    self.strSetting(inputFrame)
                case "int":
                    self.intSetting(inputFrame)
                case "bool":
                    self.boolSetting(inputFrame)
                case _:
                    pass
            
            self.row += 1

            
            # potentially better way to implement this?
            # Allows a class to add entries to a
            # settingsDict dictionary, with the keys being
            # the name of the class and the values being
            # the function that that setting type calls
            # to create the correct entry.
            #
            # When a class inherits this class, it can
            # add setting types to the setting dictionary
            # making the settings generation more extensible
            """
            valueTypeName = type(value).__name__
            if valueTypeName is in self.settingsDict.keys():
                self.settingsDict[valueTypeName](key, value)
            else:
                return NotImplementedError()
            """

            self.saveAndExitButtons()


    def saveSettings(self):
        """saves the settings inputted in the window"""

    def exitSettings(self):
        """exits the window without savings the changes"""

    def saveAndExitButtons(self):
        """Creates the save and exit button for the frame"""
        # button for savings settings
        tk.Button(
            master=self,
            label="Save",
            command=self.saveSettings
        ).grid(
            column=0,
            row=self.row,
            padx=10,
            pady=10
        )

        # button to close the window
        tk.Button(
            master=self,
            label="Exit",
            commande=self.destroy,
        ).grid(
            column=1,
            row=self.row,
            padx=10,
            pady=10
        )

    # default setting generator. Cleans
    # up the code and makes it easier to
    # define a new setting type
    def baseSetting(self, tkVar, tkFunc, frame, **kwargs):
        """
        The function operates as follows:

        1. This function appends the output variable for the setting input
           frame to the kwargs dictionary. The output variable is generated
           by passing tkVar to frame.createOutput().
        2. Then, the function passes tkFunc and kwargs as arguments to
           frame.addSettingWidget(), which returns the labelWidget and the
           widget for inputting data.
        3. The widgets are then placed onto the settings frame with the grid()
           function on the current row.
        """
        kwargs = kwargs | frame.createOutput(tkVar)

        labelWidget, widget = frame.addSettingWidget(
            tkFunc,
            **kwargs
        )

        # generate label on the left
        labelWidget.grid(
            column=0,
            row=self.row,
            padx=5,
            pady=10
        )

        # setup the widget that we want
        # must pass the widget function
        # through the function
        widget.grid(
            column=1,
            row=self.row,
            padx=10,
            pady=10,
        )

    # string setting input
    def strSetting(self, frame):
        """
        Creates a string setting input with the Entry object.
        """
        self.baseSetting(tk.StringVar, tk.Entry, frame)

    # integer setting input
    def intSetting(self, frame):
        """
        Creates an integer setting input with the Entry object.
        """
        self.baseSetting(tk.IntVar, tk.Entry, frame)

    # boolean setting input
    def boolSetting(self, frame):
        """
        Creates a boolean setting input with on and off values as 1 and 0 and
        the input as a checkbutton.
        """
        kwargs = dict()
        kwargs["onvalue"] = 1
        kwargs["offvalue"] = 0

        self.baseSetting(tk.IntVar, tk.Checkbutton, frame, **kwargs)


if __name__ == "__main__":
    pass
