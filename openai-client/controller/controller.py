from openai-client.model.request.completion import CompletionRequest
from openai-client.model.request.edit import EditRequest
from openai-client.model.models import Models
from openai-client.model.response import Response
from openai-client.view.view import View

"""
Class Controller:

This class manages the data model and the view model.
"""


class Controller:
    def __init__(self):
        # initialized variables

        # different models we can use
        self.models = Models()
        # the view
        self.view = View()

        # uninitialized variables

        # the request we are making
        self.request = None
        # the response
        self.response = None

    """Manage requests"""

    # creates a request
    def buildRequest(self, req):
        self.request = self.view.getRequest(req)
        self.response = self.request.getResponse()

        self.view.updateResponse(self.response)

    # build an edit request
    def buildEditRequest(self):
        if not isinstance(self.request, EditRequest):
            self.request = EditRequest()
        self.buildRequest(self.request)

    # build a completion request
    def buildCompletionRequest(self):
        if not isinstance(self.request, CompletionRequest):
            self.request = CompletionRequest()
        self.buildRequest(self.request)

    # reset the current request
    def resetRequest(self):
        if isinstance(self.request, CompletionRequest):
            self.request = CompletionRequest()
        else:
            self.request = EditRequest()

    """Request Settings Data"""
    
    # returns keys for settings
    def getSettings(self, className):
        if not isinstance(self.request, className):
            # return an error
            pass
        
        return self.request.getSettings()

    # returns the keys that are settings for
    # the completion request
    def getCompletionSettings(self):
        return self.getSettings(CompletionRequest)

    # returns the keys that are settings for
    # the completion request
    def getEditSettings(self):
        return self.getSettings(EditRequest)


if __name__ == "__main__":

    controller = Controller()

    nextView = controller.initView()

    while True:
        nextView = controller.getView(nextView)
