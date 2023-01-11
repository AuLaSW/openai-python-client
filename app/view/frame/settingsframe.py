# settingsframe.py
from baseframe import BaseFrame
import tkinter as tk


class SettingsFrame(BaseFrame):
    def __init__(self, main, controller):
        super().__init__(main, controller)

        self.settings
        
        self.row = 0

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
        
        self.row += 1

    def strSetting(self, label, default):
        self.baseSetting(tk.Entry, label, default, **kwargs)

    def intSetting(self, label, default)
        self.baseSetting(tk.Entry, label, default, **kwargs)

    def boolSetting(self, label, default)
        self.baseSetting(tk.Checkbutton, label, default, **kwargs)