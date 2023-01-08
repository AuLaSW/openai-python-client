from request import Request, openai


class CompletionRequest(Request):
    def __init__(self):
        # initialize from parent class Request
        super().__init__()

        # setup self.requestDict

        # required values
        self.requestDict[self.REQUIRED] = {
            "model": "text-davinci-003"
        }

        # optional values
        self.requestDict[self.OPTIONAL] = {
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

    def getResponse(self, dict):
        required, optional = self.separateDict(dict)

        response = openai.Completion.create(
                # required inputs
                model=required["model"],

                # optional inputs
                prompt=optional["prompt"],
                max_tokens=optional["max_tokens"],
                temperature=optional["temperature"],
                top_p=optional["top_p"],
                n=optional["n"],
                stream=optional["stream"],
                echo=optional["echo"],
                presence_penalty=optional["presence_penalty"],
                frequency_penalty=optional["frequency_penalty"],
                best_of=optional["best_of"],
                user=optional["user"]
                # suffix=optional["suffix"],
                # logprobs=optional["logprobs"],
                # stop=optional["stop"],
                # logit_bias=optional["logit_bias"],
                )
        return response


if __name__ == "__main__":
    req = CompletionRequest()

    print(req)
