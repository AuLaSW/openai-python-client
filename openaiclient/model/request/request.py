"""
Holds the request product classes
"""
from abc import ABC, abstractmethod


class RequestProduct(ABC):
    """
    Abstract Product class for Request Products
    """

    def __getattr__(self, name):
        if '_requestDict' in self.__dict__:
            return self.__dict__['_requestDict'][name]
        else:
            pass

    """
    @property
    @abstractmethod
    def requiredArguments(self):
        pass

    @property
    @abstractmethod
    def optionalArguments(self):
        pass

    @property
    @abstractmethod
    def settings(self):
        pass

    @property
    @abstractmethod
    def request(self):
        pass
    """


class CompletionRequest(RequestProduct):
    """
    A Completion Request object
    """

    def __init__(self, model=None) -> None:
        # I'm wondering if this should just be read from a database of
        # default values for differnt types of requests? Would be easier
        # than trying to type it all out programatically.
        self._requestDict = {
            "model": RequestSetting(
                value=model,
                setting=True,
                optional=False,
                ),
            "prompt": RequestSetting(
                value="",
                setting=False,
                optional=True,
                ),
            "max_tokens": RequestSetting(
                value=16,
                setting=True,
                optional=True,
                ),
            "temperature": RequestSetting(
                value=0.0,
                setting=True,
                optional=True,
                ),
            "top_p": RequestSetting(
                value=0.0,
                setting=True,
                optional=True,
                ),
            "n": RequestSetting(
                value=1,
                setting=True,
                optional=True,
                ),
            "stream": RequestSetting(
                value=False,
                setting=True,
                optional=True,
                ),
            "echo": RequestSetting(
                value=False,
                setting=True,
                optional=True,
                ),
            "presence_penalty": RequestSetting(
                value=0.0,
                setting=True,
                optional=True,
                ),
            "frequency_penalty": RequestSetting(
                value=0.0,
                setting=True,
                optional=True,
                ),
            "best_of": RequestSetting(
                value=1,
                setting=True,
                optional=True,
                ),
            "user": RequestSetting(
                value="",
                setting=True,
                optional=True,
                ),
            # these keys I cannot get to work and are optional,
            # so they are commented out until they work
            #
            # "suffix": NULL,
            # "logprobs": 0,
            # "stop": "",
            # "logit_bias": {},
        }

    @property
    def request(self):
        """
        Returns a cleaned dictionary of the request dictionary
        """
        temp = {}

        for key, item in self._requestDict.items():
            temp[key] = item.value

        return temp

    @property
    def optionalArguments(self):
        """
        Returns a dictionary of optional arguments for the request
        """

        temp = {}

        for key, item in self._requestDict.items():
            if item.optional:
                temp[key] = item.value

        return temp

    @property
    def requiredArguments(self):
        """
        Returns a dictionary of optional arguments for the request
        """

        temp = {}

        for key, item in self._requestDict.items():
            if not item.optional:
                temp[key] = item.value

        return temp


class RequestSetting:
    """
    Holds setting objects for request objecs
    """

    def __init__(self, value, setting=False, optional=False) -> None:
        self._value = value
        self._setting = setting
        self._optional = optional

    def set(self, name, val) -> None:
        datafield = getattr(self, name, None)
        if type(val) == type(datafield):
            setattr(self, name, val)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self.set('_value', val)

    @property
    def setting(self):
        return self._setting

    @setting.setter
    def setting(self, val):
        self.set('_setting', val)

    @property
    def optional(self):
        return self._optional

    @optional.setter
    def optional(self, val):
        self.set('_optional', val)


if __name__ == "__main__":
    setting = RequestSetting(1)

    setting.setting = True

    setting.optional = True

    print(setting.value)

    req = CompletionRequest()

    print(req.optionalArguments)
