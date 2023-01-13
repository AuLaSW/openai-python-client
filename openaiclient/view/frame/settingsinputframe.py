# settingsinputframe.py
from openai-client.view.frame.baseframe import BaseFrame


class SettingsInputFrame(BaseFrame):
    def __init__(self, main, controller, label, default):
        super().__init__(self, main, controller)

        self.main = main
        self.label = label
        self.default = default

    # default setting generator. Cleans
    # up the code and makes it easier to
    # define a new setting type
    def addSettingWidget(self, tkFunc, label, **kwargs):
        # generate label on the left
        labelWidget = tk.Label(
            master=self,
            text=label
        )

        # setup the widget that we want
        # must pass the widget function
        # through the function
        widget = tkFunc(
            master=self,
            **kwargs
        )
        
        return labelWidget, widget

    # create the output variable for the widget
    # and point kwargs and self.main.options to it
    def createOutput(self, tkVar, label, default):
        kwargs = dict()

        output = tkVar
        output.set(default)
        
        self.main.options[label] = output

        kwargs["variable"] = output

        return kwargs