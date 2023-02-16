"""
This module replicates the OpenAI openai class and has the folowing functions:

    Completion.create()

    Edit.create()
"""

class Completion:
    """
    This class mimics the Completion class for the OpenAI API
    """
    def create(**kwargs):
        """
        This function returns a generic response for the Completion API.
        """
        response = {
            "object": "text_completion",
            "choices": [{
                "text": "input text",
                "index": 0,
                "finish_reason": "finished"
                }
            ],
            "model": "text-davinci-003"
        }

        return response


class Edit:
    """
    This class mimics the Edit class for the OpenAI API
    """
    def create(**kwargs):
        """
        This function returns a generic response for the Edit API.
        We do not pass a cls argument because we are not working on the
        class, just need a method inside of a class to accept a dictionary
        and return a generic value
        """
        response = {
            "object": "edit",
            "choices": [{
                "text": "input text",
                "index": 0,
            }
            ],
        }

        return response
