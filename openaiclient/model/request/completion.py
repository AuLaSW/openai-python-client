# import openai
from openaiclient.model.request.request import Request
from openaiclient.model.response import Response

"""
Class CompletionRequest

This is a derived class, with the Request class being the base class.
Handles sending requests to OpenAI for completion.
"""


class CompletionRequest(Request):
    def __init__(self, module, models):
        # initialize from parent class Request
        super().__init__()

        # set up API class
        self._module = module
        self._models = models

        # setup self._requestDict

        self._requestDict = {
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
        self._requiredArgs = {
            "model",
        }

        # optional values
        self._optionalArgs = set(self._requestDict.keys())
        self._optionalArgs -= self._requiredArgs

        # set of setting arguments
        self._settings = set(self._requestDict.keys())
        self._settings.remove("prompt")

    def getResponse(self):
        return Response(
            self._module.Completion.create(
                **self._requestDict,
            )
        )

    def addToPrompt(self, newInput, newLine=False):
        if len(self.prompt) == 0:
            self.set_prompt(newInput)
        elif newLine:
            self.set_prompt(self.prompt + "\n" + newInput)
        else:
            self.set_prompt(self.prompt + " " + newInput)

    # Properties
    
    ## Arguments
    
    @property
    def requiredArguments(self):
        return self._requiredArgs
    
    @property
    def optionalArguments(self):
        return self._optionalArgs
    
    # request dictionary arguments
    
    @property
    def model(self):
        return self._requestDict["model"]
    
    def set_model(self, val):
        if val in self._models:
            self._requestDict["model"] = val
        else:
            raise RuntimeError(f"The model '{val}' is not a valid model.")

    
    @property
    def prompt(self):
        return self._requestDict["prompt"]
        
    def set_prompt(self, val):
        if isinstance(val, str):
            self._requestDict["prompt"] = val
        else:
            raise RuntimeError("The prompt must be a string.")
    
    @property
    def max_tokens(self):
        return self._requestDict["max_tokens"]
        
    def set_max_tokens(self, val):
        max_tokens = self._models.models[self.model].max_tokens
        
        if isinstance(val, int) and not isinstance(val, bool) and val > 0 and val <= max_tokens:
            self._requestDict["max_tokens"] = val
        else:
            raise RuntimeError(f"max_tokens must be an integer greater than 0 and less than {max_tokens}")
    
    @property
    def temperature(self):
        return self._requestDict["temperature"]

    def set_temperature(self, val):
        if isinstance(val, float) and val >= 0 and val <=2:
            self._requestDict["temperature"] = val
        else:
            raise RuntimeError("temperature must be number between 0 and 2.")
        
    @property
    def top_p(self):
        return self._requestDict["top_p"]
        
    def set_top_p(self, val):
        if isinstance(val, float) and val >= 0 and val <=1:
            self._requestDict["top_p"] = val
        else:
            raise RuntimeError("top_p must be an integer greater than 0.")
        
    @property
    def n(self):
        return self._requestDict["n"]
    
    def set_n(self, val):
        if isinstance(val, int) and not isinstance(val, bool) and val > 0:
            self._requestDict["n"] = val
        else:
            raise RuntimeError("n must be an integer greater than 0.")
        
    @property
    def stream(self):
        return self._requestDict["stream"]

    def set_stream(self, val):
        if isinstance(val, bool):
            self._requestDict["stream"] = val
        else:
            raise RuntimeError("stream must be a boolean value.")
        
    @property
    def echo(self):
        return self._requestDict["echo"]

    def set_echo(self, val):
        if isinstance(val, bool):
            self._requestDict["echo"] = val
        else:
            raise RuntimeError("echo must be a boolean value.")
        
    @property
    def presence_penalty(self):
        return self._requestDict["presence_penalty"]

    def set_presence_penalty(self, val):
        if isinstance(val, float) and val >= -2.0 and val <= 2.0:
            self._requestDict["presence_penalty"] = val
        else:
            raise RuntimeError("presence_penalty must be a float between -2.0 and 2.0.")
        
    @property
    def frequency_penalty(self):
        return self._requestDict["frequency_penalty"]
        
    def set_frequency_penalty(self, val):
        if isinstance(val, float) and val >= -2.0 and val <= 2.0:
            self._requestDict["frequency_penalty"] = val
        else:
            raise RuntimeError("frequency_penalty must be a float between -2.0 and 2.0.")
        
    @property
    def best_of(self):
        return self._requestDict["best_of"]
        
    def set_best_of(self, val):
        if isinstance(val, int) and not isinstance(val, bool) and val > 0:
            self._requestDict["best_of"] = val
        else:
            raise RuntimeError("best_of must be an integer greater than 0.")
        
    @property
    def user(self):
        return self._requestDict["user"]
        
    def set_user(self, val):
        if isinstance(val, str):
            self._requestDict["user"] = val
        else:
            raise RuntimeError("The user must be a string.")

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
