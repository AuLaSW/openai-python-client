# completionsettings.py
from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
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


class EditSettings(SettingsFrame):
    def __init__(self, main: SettingsFrame | tk.Tk, controller: Controller):
        super().__init__(main, controller)

        self.settings = self.controller.handler.settings

    def setAttr(self, key: str, val) -> None:
        setter = getattr(self.controller.handler, "set_" + key)

        setter(val)

    # Model setting input
    def modelSetting(self, key: str, value) -> SettingsFrame.Setting:
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
            width=20
        )

        return setting

    def modelArgs(self, args=set()):
        for model in self.controller.models:
            args.add(model)

        return tuple(args)


if __name__ == "__main__":
    import tkinter as tk
    from openaiclient.controller.controller import Controller
    from openaiclient.view.view import View
    from tests.unit.fixture import api

    controller = Controller(api)
    controller.completionRequest()
    controller.view.completionSettingsWindow()
