# settingsframe.py
from openaiclient.view.frame.baseframe import BaseFrame
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

        self.settings = {}
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
                    # this won't work because the function
                    # returns two values, so how to make
                    # this work?
                    labelWidget, widget = SettingsInputFrame(
                        self,
                        self.controller,
                        key,
                        value
                    )

                    labelWidget.grid(
                        column=0,
                        row=self.row,
                        padx=10,
                        pady=10,
                    )

                    widget.grid(
                        column=0,
                        row=self.row,
                        padx=10,
                        pady=10,
                    )
                case "int":
                    self.intSetting(key, value)
                case "bool":
                    self.boolSetting(key, value)
                case _:
                    pass

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
            # command=self.saveSettings
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
            # command=self.exitSettings
        ).grid(
            column=1,
            row=self.row,
            padx=10,
            pady=10
        )

    def saveSettings(self):
        pass

    # default setting generator. Cleans
    # up the code and makes it easier to
    # define a new setting type
    def baseSetting(self, tkFunc, label, **kwargs):
        # generate label on the left
        tk.Label(
            master=self,
            text=label
        ).grid(
            column=0,
            row=self.row,
            padx=5,
            pady=10
        )

        # setup the widget that we want
        # must pass the widget function
        # through the function
        tkFunc(
            master=self,
            **kwargs
        ).grid(
            column=1,
            row=self.row,
            padx=5,
            pady=10
        )

        # move down one row
        self.row += 1

    # string setting input
    def strSetting(self, label, default):
        kwargs = dict()

        self.addOutput(tk.StringVar, lable, default, kwargs)

        self.baseSetting(tk.Entry, label, **kwargs)

    # integer setting input
    def intSetting(self, label, default):
        kwargs = dict()

        self.addOutput(tk.IntVar, lable, default, kwargs)

        self.baseSetting(tk.Entry, label, **kwargs)

    # boolean setting input
    def boolSetting(self, label, default):
        kwargs = dict()

        self.addOutput(tk.IntVar, lable, default, kwargs)

        kwargs["onvalue"] = 1
        kwargs["offvalue"] = 0

        self.baseSetting(tk.Checkbutton, label, **kwargs)

    def addOutput(self, tkVar, label, default, kwaDict):
        output = tkVar
        output.set(default)

        self.outputs[label] = output

        kwaDict["variable"] = output


if __name__ == "__main__":
    pass
