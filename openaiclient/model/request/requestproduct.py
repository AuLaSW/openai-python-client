"""
Holds the request product classes
"""
from abc import ABC, abstractmethod
import pickle
from pathlib import Path


class RequestProduct(ABC):
    """
    Abstract Product class for Request Products
    """

    def __getattr__(self, name):
        if '_requestDict' in self.__dict__:
            return self.__dict__['_requestDict'][name]

    def _pickle_dump(self):
        with open(self.PICKLE_PATH, "wb") as file:
            pickle.dump(self._requestDict, file)

    @property
    @abstractmethod
    def request(self):
        pass

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


class CompletionRequest(RequestProduct):
    """
    A Completion Request object
    """

    def __init__(self, model=None) -> None:
        self.PICKLE_PATH = Path(
            f"./defaults/model/request/{self.__class__.__name__}.pickle"
        )

        self._requestDict = {}

        try:
            with open(self.PICKLE_PATH, "rb") as file:
                self._requestDict = pickle.load(file)
        except Exception as err:
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

    def set_model(self, val):
        """
        Check that the input is the correct type and set the value
        """
        typeName = type(val).__name__

        if typeName == "Model":
            self.model._value = val
        else:
            raise RuntimeError(
                f"The model '{val}' is not a valid model.")

    def set_prompt(self, val):
        if isinstance(val, str):
            self.prompt._value = val
        else:
            raise RuntimeError("The prompt must be a string.")

    def set_max_tokens(self, val):
        max_tokens = self._models.models[self.model.name].max_tokens

        if isinstance(val, int) and 0 < val <= max_tokens:
            self.max_tokens._value = val
        else:
            raise RuntimeError(
                "max_tokens must be an integer greater than 0 and " +
                f"less than {max_tokens}"
            )

    def set_temperature(self, val):
        if isinstance(val, float) and 0 <= val <= 2:
            self.temperature._value = val
        else:
            raise RuntimeError("temperature must be number between 0 and 2.")

    def set_top_p(self, val):
        if isinstance(val, float) and 0 <= val <= 1:
            self.top_p._value = val
        else:
            raise RuntimeError(
                "top_p must be an integer greater than 0.")

    def set_n(self, val):
        if isinstance(val, int)\
                and not isinstance(val, bool)\
                and 0 < val:
            self.n._value = val
        else:
            raise RuntimeError("n must be an integer greater than 0.")

    def set_stream(self, val):
        if val in [True, False]:
            self.stream._value = bool(val)
        else:
            raise RuntimeError("stream must be a boolean value.")

    def set_echo(self, val):
        if val in [True, False]:
            self.echo._value = bool(val)
        else:
            raise RuntimeError("echo must be a boolean value.")

    def set_presence_penalty(self, val):
        if isinstance(val, float) and -2.0 <= val <= 2.0:
            self.presence_penalty._value = val
        else:
            raise RuntimeError(
                "presence_penalty must be a float between -2.0 and 2.0.")

    def set_frequency_penalty(self, val):
        if isinstance(val, float) and -2.0 <= val <= 2.0:
            self.frequency_penalty._value = val
        else:
            raise RuntimeError(
                "frequency_penalty must be a float between -2.0 and 2.0.")

    def set_best_of(self, val):
        if isinstance(val, int) and not isinstance(val, bool) and 0 < val:
            self.best_of._value = val
        else:
            raise RuntimeError(
                "best_of must be an integer greater than 0.")

    def set_user(self, val):
        if isinstance(val, str):
            self.user._value = val
        else:
            raise RuntimeError("The user must be a string.")

    @property
    def request(self):
        """
        Returns a cleaned dictionary of the request dictionary
        """
        temp = {}

        for key, item in self._requestDict.items():
            temp[key] = item.value
        
        temp['model'] = temp['model'].name

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

    @property
    def settings(self):
        """
        Returns a dictionary of the settings in the request
        """

        temp = {}

        for key, item in self._requestDict.items():
            if item.setting:
                temp[key] = item.value

        return temp


class EditRequest(RequestProduct):
    """
    A Edit Request object
    """


class CodexRequest(RequestProduct):
    """
    A Codex Request object
    """


class RequestSetting:
    """
    Holds setting objects for request objecs
    """

    def __init__(self, value, setting=False, optional=False) -> None:
        self._value = value
        self._setting = setting
        self._optional = optional

    @property
    def value(self):
        return self._value

    @property
    def setting(self):
        return self._setting

    @property
    def optional(self):
        return self._optional


if __name__ == "__main__":
    req = CompletionRequest()
    req._pickle_dump()
