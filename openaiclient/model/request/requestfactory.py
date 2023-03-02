"""
Class Request:

An abstract class used to model different request types to the
OpenAI API.
"""
from abc import ABC, abstractmethod
from openaiclient.model.modelsproduct import *
from openaiclient.model.request.requestproduct import *
from openaiclient.model.request.requesthandler import CompletionRequestHandler


class RequestFactory(ABC):
    """
    An abstract factory for implementing request factories.
    
    Remember that the factory is how you directly interact with the products!
    """

    def __init__(self):
        self._models = self.createModels()
        self._request = self.createRequest()
        self._handler = self.createRequestHandler(
            self._request,
            api
        )
    
    def __getattr__(self, name):
        if hasattr(self._reqeust, name):
            return getattr(self._request, name)
        elif hasattr(self._models, name):
            return getattr(self._models, name)
        else:
            raise AttributeError
        
    def updateRequest(self, **kwargs):
        """
        Accepts a dictionary of values to update for
        the request object.
        """
        for key, value in kwargs.items():
            # if the update involves the model, then make sure
            # we are replacing the model with a model object
            # and not the model name
            if key == "model":
                value = getattr(self._models, value.replace("-", "_"))
            # get the function and pass value to it
            getattr(self._request, "set_"+key)(value)
    
    def getResponse(self):
        """
        Returns a dictionary of the response object
        """
        return self._handler.getResponse()

    @abstractmethod
    def createModels(self):
        pass

    @abstractmethod
    def createRequest(self, model):
        pass

    @abstractmethod
    def createRequestHandler(self, request, api):
        pass


class CompletionRequestFactory(RequestFactory):
    """
    Creates Completion Request Objects
    """

    def createModels(self):
        return CompletionModels()

    def createRequest(self):
        """
        Create a completion request with the default
        model text-davinci-003.
        
        This requires self._models to be created before
        self._request.
        """
        return CompletionRequest(self._models.text_davinci_003)

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

