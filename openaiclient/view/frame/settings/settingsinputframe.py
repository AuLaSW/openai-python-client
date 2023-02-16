# settingsinputframe.py
import tkinter as tk
from openaiclient.view.frame.baseframe import BaseFrame


class SettingsInputFrame(BaseFrame):
    def __init__(self, main, controller, label, default):
        super().__init__(main, controller)

        # this should be handled by master in the
        # tk.Frame class
        # self.main = main
        self.label = label
        self.default = default

    # default setting generator. Cleans
    # up the code and makes it easier to
    # define a new setting type
    def addSettingWidget(self, tkFunc, **kwargs):
        # generate label on the left
        labelWidget = tk.Label(
            master=self,
            text=self.label
        )

        # setup the widget that we want.
        # must pass the widget function
        # through the function and pass
        # the kwargs with at least the
        # option tracking variable to
        # track what the entry value
        # is
        widget = tkFunc(
            master=self,
            **kwargs
        ).grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )


    # create the output variable for the widget
    # and point kwargs and self.main.options to it
    def createOutput(self, tkVar):
        kwargs = dict()

        output = tkVar
        output.set(self.default)

        self.master.outputs[self.label] = output

        kwargs["variable"] = output

        return kwargs
