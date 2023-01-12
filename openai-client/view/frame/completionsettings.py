# completionsettings.py
from openai-client.view.frame.settingsframe import SettingsFrame

"""
Class CompletionSettings:

This class is a child of SettingsFrame and implements a setting frame
with settings for an OpenAI API text-completion request.
"""


class CompletionSettings(SettingsFrame):
    def __init__(self, main, controller):
        super().__init__(main, controller)

        self.settings = self.controller.getCompletionSettings()

        self.create()