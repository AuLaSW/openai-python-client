"""
Class Request:

An abstract class used to model different request types to the
OpenAI API.
"""
from abc import ABC, abstractmethod
from openaiclient.model.models import *
from openaiclient.model.request.request import *
from openaiclient.model.request.requesthandler import CompletionRequestHandler


class RequestFactory(ABC):
    """
    An abstract factory for implementing request factories
    """

    @abstractmethod
    def createModels(self):
        pass

    @abstractmethod
    def createRequest(self, model):
        pass

    @abstractmethod
    def createRequestHandler(self, request):
        pass


class CompletionRequestFactory(RequestFactory):
    """
    Creates Completion Request Objects
    """

    def createModels(self):
        return CompletionModels()

    def createRequest(self, model):
        return CompletionRequest(model)

    def createRequestHandler(self, request, api):
        return CompletionRequestHandler(request, api)


class EditRequestFactory(RequestFactory):
    """
    Creates Edit Request Objects
    """

    def createRequest(self):
        return EditRequest()

    def createModels(self):
        return EditModels()

    def createRequestHandler(self):
        return EditRequestHandler()


class CodexRequestFactory(RequestFactory):
    """
    Creates Codex Request Objects
    """

    def createRequest(self):
        return CodexRequest()

    def createModels(self):
        return CodexModels()

    def createRequestHandler(self):
        return CodexRequestHandler()

