"""
Class Response:

A class that turns the response JSON from the OpenAI API
into an object that can be used within Python
"""
from abc import ABC, abstractmethod
from tests.unit.fixture import api


class ResponseProduct(ABC):
    """
    An interface for working with response products
    """
    
    def __getattr__(self, name):
        if '_response' in self.__dict__:
            return self.__dict__['_response'][name]


class CompletionResponse(ResponseProduct):
    """
    A competion response object
    """

    def __init__(self, request, api):
        self._response = {
                "obj": None,
                "text": None,
                "index": None,
                "model": None,
                "finish_reason": None,
        }

        self._api = api

        self.getResponse(request)

    def getResponse(self, request):
        response = self._api.Completion.create(
            **request.request
        )

        self.obj = response["object"]
        self.text = response["choices"][0]["text"]
        self.index = response["choices"][0]["index"]
        self.model = response["model"]
        self.finish_reason = response["choices"][0]["finish_reason"]


if __name__ == "__main__":
    pass
