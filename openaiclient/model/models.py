import openai
from abc import ABC, abstractmethod
import pickle
from pathlib import Path

"""
Class Models

This class retrieves the models from the OpenAI API
and creates a dictionary of the usable classes.
"""


"""
class Models:
    def __init__(self):
        self.COMPLETION = "Completion"
        self.EDIT = "Edit"

        # dictionary of models
        self._models = {
            "text-davinci-003": Model(
                name="text-davinci-003",
                max_tokens=4_000,
                type=self.COMPLETION
            ),
            "text-curie-001": Model(
                name="text-curie-001",
                max_tokens=2_048,
                type=self.COMPLETION
            ),
            "text-babbage-001": Model(
                name="text-babbage-001",
                max_tokens=2_048,
                type=self.COMPLETION
            ),
            "text-ada-001": Model(
                name="text-ada-001",
                max_tokens=2_048,
                type=self.COMPLETION
            ),
            "text-davinci-edit-001": Model(
                name="text-davinci-edit-001",
                type=self.EDIT
            ),
        }

    def __str__(self):
        strModels = "Usable Models:\n"

        strModels += "  " + self.COMPLETION + " Models:\n"

        for _, model in self.models.items():
            if model.type == self.COMPLETION:
                strModels += "    " + model.name + "\n"

        strModels += "  " + self.EDIT + " Models:\n"

        for _, model in self.models.items():
            if model.type == self.EDIT:
                strModels += "    " + model.name + "\n"

        return strModels

    def __contains__(self, item):
        return item in self._models

    @property
    def models(self):
        return self._models

    @property
    def completionModels(self):
        modelDict = {}
        for key, model in self.models.items():
            if model.type == self.COMPLETION:
                modelDict[key] = model

        return modelDict

    @property
    def editModels(self):
        modelList = []
        for _, model in self.models.items():
            if model.type == self.EDIT:
                modelList.append(model)

        return modelList

    @property
    def text_davinci_003(self):
        return self.models["text-davinci-003"]

    @property
    def text_curie_001(self):
        return self.models["text-curie-001"]

    @property
    def text_babbage_001(self):
        return self.models["text-babbage-001"]

    @property
    def text_ada_001(self):
        return self.models["text-ada-001"]

    @property
    def text_davinci_edit_001(self):
        return self.models["text-davinci-edit-001"]
"""

class ModelProduct(ABC):
    """
    Abstract Product class for Model Products
    """

    def __getattr__(self, name):
        if '_models' in self.__dict__:
            return self.__dict__['_models'][name]

    def _pickle_dump(self):
        with open(self.PICKLE_PATH, "wb") as file:
            pickle.dump(self._models, file)


class CompletionModels(ModelProduct):
    """
    A completion model object
    """

    def __init__(self):
        self.PICKLE_PATH = Path(
            f"./defaults/model/request/{self.__class__.__name__}.pickle"
        )
        print(self.PICKLE_PATH)

        self._models = {}

        try:
            with open(self.PICKLE_PATH, "rb") as file:
                self._models = pickle.load(file)
        except Exception:
            self._models = {
                "text_davinci_003": Model(
                    name="text-davinci-003",
                    max_tokens=4_000,
                ),
                "text_curie_001": Model(
                    name="text-curie-001",
                    max_tokens=2_048,
                ),
                "text_babbage_001": Model(
                    name="text-babbage-001",
                    max_tokens=2_048,
                ),
                "text_ada_001": Model(
                    name="text-ada-001",
                    max_tokens=2_048,
                ),
                # "text_davinci_edit_001": Model(
                #    name="text-davinci-edit-001",
                #    endpoint=self.EDIT
                # ),
            }

    @property
    def models(self):
        return self._models


class Model:
    def __init__(self, name, max_tokens=-1):
        self._name = name
        self._max_tokens = max_tokens

    @property
    def name(self):
        return self._name

    @property
    def max_tokens(self):
        return self._max_tokens


if __name__ == "__main__":
    model = CompletionModels()
    model._pickle_dump()

    print(model)
