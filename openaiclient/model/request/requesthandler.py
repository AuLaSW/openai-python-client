"""
Factory for generating request handlers
"""
from abc import ABC, abstractmethod
from openaiclient.model.response import *


class RequestHandlerFactory(ABC):
    """
    An abstract factory for creating request handlers
    """

    """
    @abstractmethod
    def setRequest(self, request):
        pass
    """


class CompletionRequestHandler(RequestHandlerFactory):
    """
    Creates a completion response object
    """

    def __init__(self, request, api):
        self._request = request
        self._api = api

    def createCompletionResponse(self):
        return CompletionResponse(self._request, self._api)

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, val):
        self._request = val
