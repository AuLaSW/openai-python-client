# completionsettings.py
from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
from openaiclient.view.frame.settings \
    .settingsframe import SettingsFrame
from openaiclient.view.frame.settings.requestsettings import RequestSettings


if TYPE_CHECKING:
    from openaiclient.controller.controller import Controller
    from openaiclient.view.frame.settings.settingsframe import SettingsFrame
    

"""
Class CompletionSettings:

This class is a child of SettingsFrame and implements a setting frame
with settings for an OpenAI API text-completion request.
"""


class CompletionSettings(RequestSettings):
    pass


if __name__ == "__main__":
    import tkinter as tk
    from openaiclient.controller.controller import Controller
    from openaiclient.view.view import View
    from tests.unit.fixture import api

    controller = Controller(api)
    controller.completionRequest()
    controller.view.completionSettingsWindow()
