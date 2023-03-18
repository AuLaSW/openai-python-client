"""
Factory for generating request handlers
"""
from abc import ABC, abstractmethod
from openaiclient.model.responseproduct import *


class ResponseHandlerFactory(ABC):
    """
    An abstract factory for creating request handlers
    """

    """
    @abstractmethod
    def setRequest(self, request):
        pass
    """

    @abstractmethod
    def getResponse(self):
        pass


class CompletionResponseHandler(ResponseHandlerFactory):
    """
    Creates a completion response object
    """

    def __init__(self, request, api):
        self._request = request
        self._api = api

    def getResponse(self):
        return CompletionResponse(self._request, self._api)


class EditResponseHandler(ResponseHandlerFactory):
    """
    Creates a edit response object
    """

    def __init__(self, request, api):
        self._request = request
        self._api = api

    def getResponse(self):
        return EditResponse(self._request, self._api)


class CodexResponseHandler(ResponseHandlerFactory):
    """
    Creates a Codex response object
    """

    def __init__(self, request, api):
        self._request = request
        self._api = api

    def getResponse(self):
        return CodexResponse(self._request, self._api)
