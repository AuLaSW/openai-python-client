"""
Class Request:

An abstract class used to model different request types to the
OpenAI API.
"""
from abc import ABC, abstractmethod


class RequestFactory(ABC):
    """
    An abstract factory for implementing request factories
    """
    @abstractmethod
    def createRequest(self):
        pass

    @abstractmethod
    def createModels(self):
        pass

    @abstractmethod
    def createRequestHandler(self):
        pass


class CompletionRequestFactory(RequestFactory):
    """
    Creates Completion Request Objects
    """

    def createRequest(self):
        return CompletionRequest()

    def createModels(self):
        return CompletionModels()

    def createRequestHandler(self):
        return CompletionRequestHandler()


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
