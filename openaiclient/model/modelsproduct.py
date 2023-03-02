from abc import ABC, abstractmethod
import pickle
from pathlib import Path


class ModelProduct(ABC):
    """
    Abstract Product class for Model Products
    """

    def __getattr__(self, name):
        if '_models' in self.__dict__:
            return self.__dict__['_models'][name]
    
    def __contains__(self, val):
        return val in self._models.keys()
    
    def __iter__(self):
        return self._models.__iter__()

    def _pickle_dump(self):
        with open(self.PICKLE_PATH, "wb") as file:
            pickle.dump(self._models, file)
    
    def _setPicklePath(self):
        return Path(
            f"./defaults/model/request/{self.__class__.__name__}.pickle"
        )
    
    @property
    def models(self):
        return self._models


class CompletionModels(ModelProduct):
    """
    A completion model object
    """

    def __init__(self):
        self.PICKLE_PATH = self._setPicklePath()
        
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
