"""Controller

This file should be imported as a module and contains the followings functions:

    * buildRequest - builds the request from a request object
"""
from enum import Enum
# from openaiclient.model.request.edit import EditRequest
from openaiclient.view.view import View
from openaiclient.model.request.requesthandler import *


class Controller:
    """
    This class manages the data model and the view model.

    ...

    Attributes
    ----------


    Methods
    -------

    """

    def __init__(self, api):
        # initialized variables

        # the view
        self._view = View(self)

        self._api = api

        # uninitialized variables

        # the request we are making
        self._handler = None
        # the response
        self._response = None

    def start(self, startVal) -> None:
        match startVal:
            case StartKey.GOOD_START:
                self.view.mainWindow()
            case StartKey.NO_API_KEY:
                self.view.apiWindow()

    @property
    def models(self):
        return self._handler._models

    @property
    def view(self):
        return self._view

    @property
    def handler(self):
        return self._handler

    def completionRequest(self) -> None:
        self._handler = CompletionRequestHandler(api=self._api)

    def getResponse(self) -> None:
        self._response = self._handler.getResponse()

    """
    def editReq(self) -> None:
        self._handler = EditRequest(self._module, self.models)
    """

    @property
    def response(self):
        return self._response


class StartKey(Enum):
    GOOD_START = 0
    NO_API_KEY = 1


if __name__ == "__main__":

    controller = Controller()

    nextView = controller.initView()

    while True:
        nextView = controller.getView(nextView)
