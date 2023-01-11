# settingsframe.py
from baseframe import BaseFrame
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

        self.settings
        
        self.row = 0

    # creates all of the widgets for
    # the frame. This default method
    # can be overriden for different
    # types of input in other settings
    # classes.
    def create(self):
        for key, value in self.settings:
            switch type(value):
                case str:
                    self.strSetting(key, value)
                    break
                case int:
                    self.intSetting(key,value)
                    break
                case bool:
                    self.boolSetting(key, value)
                    break
                default:
                    break

    # default setting generator. Cleans
    # up the code and makes it easier to
    # define a new setting type
    def baseSetting(self, tkFunc, label, default, **kwargs):
        # generate label on the left
        tk.Label(
            main=self,
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
        tk.tkFunc(
            main=self,
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
        self.baseSetting(tk.Entry, label, default, **kwargs)

    # integer setting input
    def intSetting(self, label, default)
        self.baseSetting(tk.Entry, label, default, **kwargs)

    # boolean setting input
    def boolSetting(self, label, default)
        self.baseSetting(tk.Checkbutton, label, default, **kwargs)