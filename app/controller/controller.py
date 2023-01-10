from model.request.completion import CompletionRequest
from model.request.edit import EditRequest
from model.models import Models
from model.response import Response
from view.view import View

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
            
    # initialize view
    def initView(self):
        return self.view.init()
    
    # get the next view
    def getView(self, nextView):        
        return nextView
        # return self.view.get(nextView)


if __name__ == "__main__":
    
    controller = Controller()
    
    nextView = controller.initView()
    
    for:
        nextView = controller.getView(nextView)
    
    pass