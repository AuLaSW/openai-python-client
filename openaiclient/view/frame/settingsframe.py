# settingsframe.py
from openaiclient.view.frame.baseframe import BaseFrame
from openaiclient.view.frame.settingsinputframe import SettingsInputFrame
import tkinter as tk

"""
Class SettingsFrame:

This class is for a frame that holds settings for
a user to change. Created to work with the Completion
and Edit requests to OpenAI.
"""


class SettingsFrame(BaseFrame):
    def __init__(self, main, controller):
        super().__init__(main, controller)

        self.settings = dict()
        self.options = dict()

        self.row = 0

    # creates all of the widgets for
    # the frame. This default method
    # can be overriden for different
    # types of input in other settings
    # classes.
    def create(self):
        for key in self.settings:
            value = self.settings[key]
            typeOfValue = type(value).__name__
            
            match typeOfValue:
                case "str":
                    self.strSetting(
                        key,
                        value
                    )
                case "int":
                    self.intSetting(
                        key,
                        value
                    )
                case "bool":
                    self.boolSetting(
                        key,
                        value
                    )
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
            
        # save settings button at bottom of window
        saveButton = tk.Button(
            master=self,
            label="Save",
            command=self.saveSettings
        ).grid(
            column=0,
            row=self.row,
            padx=10,
            pady=10
        )

        # don't save settings button at bottom of window
        exitButton = tk.Button(
            master=self,
            label="Exit",
            commande=self.destroy,
        ).grid(
            column=1,
            row=self.row,
            padx=10,
            pady=10
        )

    # Save the settings when the save button is pressed
    def saveSettings(self):
        for var in self.settings:
            val = self.settings[var]
            
            self.controller.request.set(var, val)

    # default setting generator. Cleans
    # up the code and makes it easier to
    # define a new setting type
    def baseSetting(self, tkVar, tkFunc, label, default, **kwargs=dict()):
        # creating the SettingsInputFrame
        input = SettingsInputFrame(
            self,
            self.controller,
            label,
            default,
            tkVar,
            tkFunc,
            kwargs
        )
        
        # attach the input frame to the
        # current frame at column 0
        input.grid(
            column=0, 
            row=self.row,
            padx=10,
            pady=10,
        )

    # string setting input
    def strSetting(self, label, default):
        self.baseSetting(
            tkVar=tk.StringVar,
            tkFunc=tk.Entry,
            label,
            default,
        )

    # integer setting input
    def intSetting(self, label, default):
        self.baseSetting(
            tkVar=tk.IntVar,
            tkFunc=tk.Entry,
            label,
            default,
        )

    # boolean setting input
    def boolSetting(self, label, default):
        kwargs = dict()
        
        kwargs["onvalue"] = 1
        kwargs["offvalue"] = 0

        self.baseSetting(
            tkVar=tk.StringVar,
            tkFunc=tk.Checkbutton,
            label,
            default,
            kwargs
        )


if __name__ == "__main__":
    pass
