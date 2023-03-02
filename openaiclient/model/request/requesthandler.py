"""
Factory for generating request handlers
"""
from abc import ABC, abstractmethod
from openaiclient.model.responseproduct import *


class RequestHandlerFactory(ABC):
    """
    An abstract factory for creating request handlers
    """

    """
    @abstractmethod
    def setRequest(self, request):
        pass
    """

    @abstractmethod
    def createResponse(self):
        pass


class CompletionRequestHandler(RequestHandlerFactory):
    """
    Creates a completion response object
    """

    def __init__(self, request, api):
        self._request = request
        self._api = api

    def createResponse(self):
        return CompletionResponse(self._request, self._api)