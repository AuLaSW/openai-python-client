"""
Factory for generating request handlers
"""
from abc import ABC, abstractmethod


class RequestHandlerFactory(ABC):
    """
    An abstract factory for creating request handlers
    """

    @abstractmethod
    def setRequest(self, request):



class CompletionRequestHandler(RequestHandlerFactory):
    """
    Creates a completion response object
    """

    def __init__(self, request):
        self._request = request

    def createCompletionResponse(self):
        return CompletionResponse(self._request)

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, val):
        self._request = val
