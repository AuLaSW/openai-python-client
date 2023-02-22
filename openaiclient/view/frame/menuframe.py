# menuframe.py
from __future__ import annotations
from abc import ABC, abstractmethod
import tkinter as tk


class MenuFactory(ABC):
    """
    An abstract factory for generating menus
    """
    @property
    @abstractmethod
    def menubar(self):
        pass

    @abstractmethod
    def create(self):
        pass


class MainMenu(MenuFactory):
    """
    Creates a main menu
    """
    def __init__(self, root, controller):
        self._menubar = tk.Menu(root)
        self._controller = controller
    
    @property
    def menubar(self):
        return self._menubar
    
    def create(self) -> None:
        self.addFileMenu()
        self.addSettingMenu()

    def createFileMenu(self) -> tk.Menu:
        return MainFileMenu(self._menubar).menu
    
    def addFileMenu(self):
        self._menubar.add_cascade(
            label="File",
            menu=self.createFileMenu()
        )
    
    def createSettingMenu(self) -> tk.Menu:
        return MainSettingMenu(self._menubar).menu
    
    def addSettingMenu(self):
        self._menubar.add_cascade(
            label="Settings",
            menu=self.createSettingMenu()
        )


class CompletionRequestMenu(MenuFactory):
    """
    Creates the menu when working with a completion request
    """


class EditRequestMenu(MenuFactory):
    """
    Creates the menu when working with an edit request
    """
    

class AbstractMenu(ABC):
    """
    An abstract menu class, parent to all menu product classes.
    """
    @abstractmethod
    def create(self):
        pass
    
    @property
    @abstractmethod
    def menu(self):
        pass


class DropdownMenu(AbstractMenu):
    """
    Creates a dropdown menu for use inside of another menu
    """


class EndpointDropdownMenu(DropdownMenu):
    """
    Creates a dropdown menu for selecting the different endpoints
    """
    def __init__(self, menu):
        self._menu = tk.Menu(
            menu,
            tearoff=0
        )
        
        self.create()

    def create(self):
        self._menu.add_command(label="Completion", command=None)
        self._menu.add_command(label="Edit", command=None)
        self._menu.add_command(label="Codex", command=None)

    @property
    def menu(self):
        return self._menu


class FileMenu(AbstractMenu):
    """
    Abstract product for file menus
    """


class MainFileMenu(FileMenu):
    """
    Creates a file menu for the main menu
    """
    def __init__(self, menubar):
        self._menu = tk.Menu(
            menubar, 
            tearoff=0
        )
        
        self.create()
    
    def create(self):
        endpointMenu = EndpointDropdownMenu(self.menu).menu
        self._menu.add_cascade(label="Change endpoint...", menu=endpointMenu)

    @property
    def menu(self):
        return self._menu


class EditMenu(AbstractMenu):
    """
    Abstract product for edit menus
    """


class SettingMenu(AbstractMenu):
    """
    Abstract product for setting menus
    """


class MainSettingMenu(SettingMenu):
    """
    Creates a setting menu for the main menu.
    """
    def __init__(self, menubar):
        self._menu = tk.Menu(
            menubar,
            tearoff=0
        )
        
        self.create()
    
    def create(self):
        self._menu.add_command(label="Completion Settings", command=None)
        self._menu.add_command(label="Edit Settings", command=None)
    
    @property
    def menu(self):
        return self._menu


class HelpMenu(AbstractMenu):
    """
    Abstract product for help menus
    """



if __name__ == "__main__":
    """
    An example of how to create a menu
    """
    root = tk.Tk()
    menu = MainMenu(root, None)
    menu.create()
    
    root.config(menu=menu.menubar)

    root.mainloop()