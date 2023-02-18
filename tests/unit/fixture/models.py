"""
This module replicates the Models class and contains the following:
"""


class Models:
    def __init__(self):
        self.models = {
            "Completion": [
                "text-davinci-003",
                "text-curie-001",
                "text-babbage-001",
                "text-ada-001"
            ],
            "Edit": [
                "text-davinci-edit-001"
            ]
        }

    def __contains__(self, item):
        return item in self.models["Completion"] + self.models["Edit"]
