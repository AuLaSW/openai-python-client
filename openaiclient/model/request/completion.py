# import openai
from openaiclient.model.request.request import Request
from openaiclient.model.response import Response

"""
Class CompletionRequest

This is a derived class, with the Request class being the base class.
Handles sending requests to OpenAI for completion.
"""


class CompletionRequest(Request):
    def __init__(self, module):
        # initialize from parent class Request
        super().__init__()

        # set up API class
        self.module = module

        # setup self.requestDict

        self.requestDict = {
            "model": "text-davinci-003",
            "prompt": "",
            "max_tokens": 16,
            "temperature": 0,
            "top_p": 0,
            "n": 1,
            "stream": False,
            "echo": False,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "best_of": 1,
            "user": ""
            # these keys I cannot get to work and are optional,
            # so they are commented out until they work
            #
            # "suffix": NULL,
            # "logprobs": 0,
            # "stop": "",
            # "logit_bias": {},
        }

        # required values
        self.requiredArgs = {
            "model",
        }

        # optional values
        self.optionalArgs = set(self.requestDict.keys())
        self.optionalArgs -= self.requiredArgs

        # set of setting arguments
        self.settings = set(self.requestDict.keys())
        self.settings.remove("prompt")

    def getResponse(self):
        return Response(
            self.module.Completion.create(
                **self.requestDict,
            )
        )

    def addToPrompt(self, newInput, newLine=False):
        if len(self.requestDict["prompt"]) == 0:
            self.set("prompt", newInput)
        elif newLine:
            self.requestDict["prompt"] += "\n" + newInput
        else:
            self.requestDict["prompt"] += " " + newInput

    # Properties
    
    ## Arguments
    
    @property
    def requiredArguments(self):
        return self.requiredArgs
    
    @property
    def optionalArguments(self):
        return self.optionalArgs
    
    @property
    def settings(self):
        return self.settings
        
    @settings.setter
    def settings(self, vals):
        try:
            var, val = vals
        except ValueError:
            raise ValueError("Please pass an iterable with two values.")
        
        if var in self.settings:
            self.requestDict[var] = val
        else:
            raise RuntimeError
    
    # request dictionary arguments
    
    @property
    def model(self):
        return self.requestDict["model"]
    
    """
    TODO: link openaiclient.model.models to validate against known models.
    """
    @model.setter
    def model(self, val):
        if val in self.models:
            self.requestDict["model"] = val
        else:
            raise RuntimeError(f"The model '{val}' is not a valid model.")

    
    @property
    def prompt(self):
        return self.requestDict["prompt"]
        
    @prompt.setter
    def prompt(self, val):
        if isinstance(val, string):
            self.requestDict["prompt"] = val
        else:
            raise RuntimeError("The prompt must be a string.")
    
    @property
    def max_tokens(self):
        return self.requestDict["max_tokens"]
        
    """
    TODO: validate maximum length
    """
    @max_tokens.setter
    def max_tokens(self, val):
        if isinstance(val, int) and val > 0:
            self.requestDict["max_tokens"] = val
        elif:
            raise RuntimeError("max_tokens must be an integer greater than 0.")
    
    @property
    def temperature(self):
        return self.requestDict["temperature"]
        
    """
    TODO: validate maximum length
    """
    @temperature.setter
    def temperature(self, val):
        if isinstance(val, int) and val > 0:
            self.requestDict["temperature"] = val
        elif:
            raise RuntimeError("temperature must be an integer greater than 0.")
        
    @property
    def top_p(self):
        return self.requestDict["top_p"]
        
    """
    TODO: validate maximum length
    """
    @top_p.setter
    def top_p(self, val):
        if isinstance(val, int) and val > 0:
            self.requestDict["top_p"] = val
        elif:
            raise RuntimeError("top_p must be an integer greater than 0.")
        
    @property
    def n(self):
        return self.requestDict["n"]
    
    """
    TODO: validate maximum length
    """
    @n.setter
    def n(self, val):
        if isinstance(val, int) and val > 0:
            self.requestDict["top_p"] = val
        elif:
            raise RuntimeError("top_p must be an integer greater than 0.")
        
    @property
    def stream(self):
        return self.requestDict["stream"]
        
    @mstream.setter
    def stream(self, val):
        # self.requestDict["max_tokens"] = val
        
    @property
    def echo(self):
        return self.requestDict["echo"]
        
    @echo.setter
    def echo(self, val):
        # self.requestDict["max_tokens"] = val
        
    @property
    def presence_penalty(self):
        return self.requestDict["presence_penalty"]
        
    @presence_penalty.setter
    def presence_penalty(self, val):
        # self.requestDict["max_tokens"] = val
        
    @property
    def frequency_penalty(self):
        return self.requestDict["frequency_penalty"]
        
    @frequency_penalty.setter
    def frequency_penalty(self, val):
        # self.requestDict["max_tokens"] = val
        
    @property
    def best_of(self):
        return self.requestDict["best_of"]
        
    @best_of.setter
    def best_of(self, val):
        # self.requestDict["max_tokens"] = val
        
    @property
    def user(self):
        return self.requestDict["user"]
        
    @user.setter
    def user(self, val):
        # self.requestDict["max_tokens"] = val

if __name__ == "__main__":
    pass
"""
    req = CompletionRequest()
    req.setPrompt("Tell me a joke")
    req.setEcho(True)

    # print(req)

    response = req.getResponse()

    print("\nPrompt One:\n")
    print(response.getText())

    req.setPrompt(response.getText())
    req.addToPrompt("I don't know. What?", True)

    response = req.getResponse()

    print("\nPrompt Two:\n")
    print(response.getText())
"""
