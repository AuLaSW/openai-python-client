# view.py
"""
Class View:

Manages the GUI, interacts with the Controller and Model classes.
"""


class View:
    def __init__(self, controller):
        # bind the controller to the view object
        # by passing the controller to the view,
        # we can bind controller functions to view
        # functions and have a better time working
        # with everything
        self.controller = controller
    
    def get(self, nextView):
        pass
    
    def initView(self):
        pass
        
    def getRequest(self, req):
        pass

if __name__ == "__main__":
    pass