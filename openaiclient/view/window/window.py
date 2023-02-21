"""
This module creates windows for the openai-client program.
"""
from __future__ import annotations
import tkinter as tk
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from openaiclient.view.frame.settings.completionsettings import CompletionSettings
from openaiclient.view.frame.settings.settingsframe import SettingsFrame
from openaiclient.view.frame.input.completioninput import CompletionInputFrame

if TYPE_CHECKING:
    from openaiclient.controller.controller import Controller

class Window(ABC):
    """
    An abstract constructor class for different windows
    """
    def __init__(self, window: tk.Tk, controller: Controller):
        self._window = window
        self._controller = controller

    @abstractmethod
    def windowConstructor(self):
        """Constructs the frame product"""
        pass

    def draw(self):
        """Packs the product onto the window and starts the window"""
        frame = self.windowConstructor()
        frame.create()
        frame.pack()

        self._window.mainloop()


class CompletionSettingsWindow(Window):
    """
    A concrete factory class for the CompletionSettings window.
    """
    def windowConstructor(self) -> CompletionSettings:
        """Constructs a CompletionSettings frame product"""
        return CompletionSettings(self._window, self._controller)


class SettingsWindow(Window):
    """
    A concrete factory class for the CompletionSettings window.
    """
    def windowConstructor(self) -> SettingsFrame:
        """Constructs a CompletionSettings frame product"""
        return SettingsFrame(self._window, self._controller)


class CompletionInputWindow(Window):
    """
    A concrete factor class for the CompletionInput window.
    """
    def windowConstructor(self) -> CompletionInputFrame:
        return CompletionInputFrame(self._window, self._controller)


if __name__ == "__main__":
    from openaiclient.controller.controller import Controller

    window = tk.Tk()

    csw = SettingsWindow(window, None)
    
    csw.draw()