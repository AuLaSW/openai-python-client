"""
Class Request:

An abstract class used to model different request types to the
OpenAI API.
"""
from abc import ABC, abstractmethod
from openaiclient.model.modelsproduct import *
from openaiclient.model.requestproduct import *
from openaiclient.model.responsehandler import *


class RequestHandlerFactory(ABC):
    """
    An abstract factory for implementing request factories.
    
    Remember that the factory is how you directly interact with the products!
    """

    def __init__(self, api):
        self._models = self.createModels()
        self._request = self.createRequest()
        self._handler = self.createResponseHandler(
            self._request,
            api
        )
    
    def __getattr__(self, name):
        try:
            return getattr(self._request, name)
        except KeyError:
            try:
                return getattr(self._models, name)
            except KeyError as error:
                raise KeyError from error
        
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
        Returns a response object.
        """
        return self._handler.getResponse()

    @abstractmethod
    def createModels(self):
        pass

    @abstractmethod
    def createRequest(self):
        pass

    @abstractmethod
    def createResponseHandler(self, request, api):
        pass


class CompletionRequestHandler(RequestHandlerFactory):
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

    def createResponseHandler(self, request, api):
        return CompletionResponseHandler(request, api)

    def setPrompt(self, prompt):
        self._request.set_prompt(prompt)


class EditRequestHandler(RequestHandlerFactory):
    """
    Creates Edit Request Objects
    """

    def createModels(self):
        return EditModels()

    def createRequest(self):
        return EditRequest(self._models.text_davinci_edit_001)

    def createResponseHandler(self, request, api):
        return EditResponseHandler(request, api)

    def setInstructions(self, prompt):
        self._request.set_instruction(prompt)

    def setInput(self, prompt):
        self._request.set_input(prompt)


class CodexRequestHandler(CompletionRequestHandler):
    """
    Creates Codex Request Objects
    """

    def createModels(self):
        return CodexModels()

    def createRequest(self):
        return CodexRequest(self._models.code_davinci_002)

    def createRequestHandler(self, request, api):
        return CodexResponseHandler(request, api)
