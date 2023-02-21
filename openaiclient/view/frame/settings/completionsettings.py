# completionsettings.py
from __future__ import annotations
from typing import TYPE_CHECKING
from openaiclient.view.frame.settings \
    .settingsframe import SettingsFrame

    
if TYPE_CHECKING:
    from openaiclient.controller.controller import Controller
    from openaiclient.view.frame.settings.settingsframe import SettingsFrame

"""
Class CompletionSettings:

This class is a child of SettingsFrame and implements a setting frame
with settings for an OpenAI API text-completion request.
"""


class CompletionSettings(SettingsFrame):
    def __init__(self, main: SettingsFrame, controller: Controller):
        super().__init__(main, controller)

        self.settings = self.controller.request.settings
    
    def setAttr(self, key:str, val) -> None:
        setter = getattr(self.controller.request, "set_"+key)
        
        if type(self.settings[key]).__name__ == "Model":
            model = getattr(self.controller.models, val.replace("-", "_"))
            setter(model)
        else:
            setter(type(val)(val))
    
    # Model setting input
    def ModelSetting(self, key:str, value) -> SettingsFrame.Setting:
        """
        Creates a drop-down setting with models as names
        """
        setting = self.Setting()
        args = self.modelArgs()
        tkFunc = tk.OptionMenu

        self._kwargs(tkFunc, tk.StringVar, "variable", key)
        
        self.outputs[key].set(self.settings[key].name)

        setting.label = tk.Label(
            master=self,
            text=key
        )

        setting.widget = tkFunc(
            self,
            self.outputs[key],
            *args
        )
        
        setting.widget.config(
            width=15
        )
        
        return setting
    
    def modelArgs(self, args=set()):
        for model in self.controller.models.completionModels.keys():
            args.add(model)

        return tuple(args)


if __name__ == "__main__":
    import tkinter as tk
    from openaiclient.controller.controller import Controller
    from tests.unit.fixture import api

    controller = Controller(api)
    window = controller.view.window.window
    window.resizable(False, False)
    controller.compReq()

    frame = CompletionSettings(
        main=window,
        controller=controller
    )

    frame.create()

    frame.pack()

    window.mainloop()
