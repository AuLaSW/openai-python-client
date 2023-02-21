"""
SettingsFrame Module
"""
import tkinter as tk
import tkinter.messagebox as messagebox
import inspect
from openaiclient.view.frame.baseframe import BaseFrame


class SettingsFrame(BaseFrame):
    """
    Class SettingsFrame:

    This class is for a frame that holds settings for
    a user to change. Created to work with the Completion
    and Edit requests to OpenAI.
    """

    def __init__(self, main, controller):
        super().__init__(main, controller)

        # hold the settings we will be using
        self.settings = dict()
        # hold the tk variables for returning inputs from the frame
        self.outputs = dict()

        # row count
        self.row = 0

    # creates all of the widgets for
    # the frame. This default method
    # can be overriden for different
    # types of input in other settings
    # classes.
    def create(self):
        """
        Creates the settings input frames by looping through the settings
        dictionary (self.settings) and creating a SettingsInputFrame object
        for each setting. It then attaches each frame in the next row on
        the frame with the grid() method.

        Finally, it creates the save and exit buttons and attaches them to
        the settings frame (self).
        """
        # key is the label, value is the value in the
        # dictionary of settings
        for key, value in self.settings.items():
            # get the name of the input type
            # str, int, float, or bool
            typeOfValue = type(value).__name__

            try:
                # get the correct setting function
                # based on value type
                func = getattr(self, typeOfValue+"Setting")
            except AttributeError:
                # skip the current attribute.
                # later, this will be logged into a logger
                print(f"No widget of type {typeOfValue} defined.")
                continue

            # get label and widget from function
            setting = func(key, value)

            # attach label
            setting.label.grid(
                column=0,
                row=self.row,
                padx=10,
                pady=10,
                sticky=tk.E
            )

            # attach widget
            setting.widget.grid(
                column=1,
                row=self.row,
                padx=10,
                pady=10,
                sticky=tk.W
            )

            # move down to the next row
            self.row += 1

        self.saveAndExitButtons()

    def saveSettings(self):
        """saves the settings inputted in the window"""
        for key in self.settings:                
            try:
                val = self.outputs[key].get()
                self.setAttr(key, val)

            except KeyError:
                pass
            except tk.TclError as error:
                messagebox.showerror(
                    f"Incorrect input in {key}", f"Key \"{key}\" " + str(error))
    
    def setAttr(self, key):
        """This should be overridden. Returns setter for saveSettings() method"""
        raise NotImplementedError

    def exitSettings(self):
        """exits the window without savings the changes"""
        self.master.destroy()

    def saveAndExitButtons(self):
        """Creates the save and exit button for the frame"""

        frame = tk.Frame(self)

        # button for savings settings
        tk.Button(
            master=frame,
            text="Save",
            command=self.saveSettings
        ).grid(
            column=0,
            row=0,
            padx=10,
            pady=10,
            ipadx=30
        )

        # button to close the window
        tk.Button(
            master=frame,
            text="Exit",
            command=self.exitSettings,
        ).grid(
            column=1,
            row=0,
            padx=10,
            pady=10,
            ipadx=30
        )

        frame.grid(
            column=0,
            row=self.row,
            columnspan=2,
            padx=10,
            pady=10
        )

    # default setting generator. Cleans
    # up the code and makes it easier to
    # define a new setting type
    def baseSetting(
            self,
            tkVar,
            tkFunc,
            key,
            value,
            varKey,
            args=(),
            kwargs={}):
        """
        The function operates as follows:

        1. This function appends the output variable for the setting input
           frame to the kwargs dictionary. The output variable is generated
           by passing tkVar to frame.createOutput().
        2. Then, the function passes tkFunc and kwargs as arguments to
           frame.addSettingWidget(), which returns the labelWidget and the
           widget for inputting data.
        3. The widgets are then placed onto the settings frame with the grid()
           function on the current row.
        """
        args = tuple(args)

        kwargs = kwargs | {varKey: tkVar()}

        # add the output variable to the outputs dictionary
        self.outputs[key] = kwargs[varKey]

        # set value to default value
        kwargs[varKey].set(self.settings[key])

        # setup the widget that we want.
        # must pass the widget function
        # through the function and pass
        # the kwargs with at least the
        # option tracking variable to
        # track what the entry value
        # is
        widget = tkFunc(
            self,
            *args,
            **kwargs
        )

        return widget

    # string setting input
    def strSetting(self, key, value):
        """
        Creates a string setting input with the Entry object.
        """
        setting = Setting()
        
        setting.label = tk.Label(
            master=self,
            text=key
        )
        
        tkFunc = tk.Entry
        
        kwargs = self._kwargs(tkFunc, tk.StringVar, key)

        setting.widget = tkFunc(
            self,
            **kwargs
        )
        
        return setting

    # integer setting input
    def intSetting(self, key, value):
        """
        Creates an integer setting input with the Entry object.
        """
        setting = Setting()
        
        setting.label = tk.Label(
            master=self,
            text=key
        )
        
        tkFunc = tk.Entry
        
        kwargs = self._kwargs(tkFunc, tk.IntVar, key)

        setting.widget = tkFunc(
            self,
            **kwargs
        )
        
        return setting

    # float setting input
    def floatSetting(self, key, value):
        """
        Creates an integer setting input with the Entry object.
        """
        setting = Setting()

        setting.label = tk.Label(
            master=self,
            text=key
        )
        
        tkFunc = tk.Entry
        
        kwargs = self._kwargs(tkFunc, tk.DoubleVar, key)

        setting.widget = tkFunc(
            self,
            **kwargs
        )
        
        return setting

    # boolean setting input
    def boolSetting(self, key, value):
        """
        Creates a boolean setting input with on and off values as 1 and 0 and
        the input as a checkbutton.
        """
        setting = Setting()
        kwargs = dict()

        kwargs["onvalue"] = 1
        kwargs["offvalue"] = 0
        
        setting.label = tk.Label(
            master=self,
            text=key
        )
        
        tkFunc = tk.Checkbutton
        
        kwargs = self._kwargs(tkFunc, tk.IntVar, key, kwargs)

        setting.widget = tkFunc(
            self,
            **kwargs
        )

        return setting

    # float setting input
    def ModelSetting(self, key, value):
        """
        Creates a drop-down setting with models as names
        """
        setting = Setting()
        args = set()

        for model in self.controller.models.completionModels.keys():
            args.add(model)

        args = tuple(args)

        tkFunc = tk.OptionMenu

        self._kwargs(tkFunc, tk.StringVar, key)

        setting.label = tk.Label(
            master=self,
            text=key
        )

        setting.widget = tkFunc(
            self,
            self.outputs[key],
            *args
        )
        
        return setting

    def _kwargs(self, tkFunc, tkVar, key, kwargs={}):
        """Sets up the kwargs for a setting input"""
        # get the signature of the function tkFunc
        sig = inspect.signature(tkFunc)

        # find the variable parameter in the signature
        # and set varKey to that string
        for param in sig.parameters.values():
            if "variable" in param.name:
                varKey = param.name

        # add varKey: tkVar() to the kwargs
        kwargs = kwargs | {varKey: tkVar()}

        # point the output dictionary value key to
        # the tkVar() we just set up
        self.outputs[key] = kwargs[varKey]

        # set the value of the tkVar
        kwargs[varKey].set(value=self.settings[key].name)

        # return kwargs
        return kwargs


class Setting:
    """Holds a setting with label and widget"""
    def __init__(self, label=None, widget=None):
        self._label = label
        self._widget = widget

    @property
    def label(self):
        """return label widget"""
        return self._label
    
    @label.setter
    def label(self, val):
        """set label widget"""
        self._label = val

    @property
    def widget(self):
        """return input widget"""
        return self._widget

    @widget.setter
    def widget(self, val):
        self._widget = val


if __name__ == "__main__":
    settingsWindow = tk.Tk()

    settingsFrame = SettingsFrame(
        main=settingsWindow,
        controller=None
    )

    settingsFrame.settings = {
        "testKey": "testVal",
        "testIntKey": 1,
        "testBoolKey": True,
        "testFloatKey": 1.0,
        "testNotInOptions": None
    }

    settingsFrame.create()

    settingsFrame.pack()

    settingsWindow.mainloop()
