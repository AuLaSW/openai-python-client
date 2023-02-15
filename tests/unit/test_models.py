# test_models.py
import unittest
from openaiclient.model.models import Models


class TestModels(unittest.TestCase):
    def setUp(self):
        self.modelObj = Models()
        self.models = self.modelObj.models
        self.comp = self.modelObj.COMPLETION
        self.edit = self.modelObj.EDIT

    # tests that the model dictionary does
    # contain the model
    def test_ContainsModel(self):
        exModel = "text-davinci-003"

        self.assertIn(exModel, self.modelObj)

    # tests that the model dictionary doesn't
    # contain the model
    def test_NotContainsModel(self):
        exModel = "text-code-davinci-003"

        self.assertNotIn(exModel, self.modelObj)

    def test_StrMethodUpdated(self):
        """
        Tests that the __str__() method is updated to work with the class
        """
        try:
            self.modelObj.__str__()
        except Exception:
            self.fail(
                "The string function is not able to run!" + \
                " Make sure you've updated the string function."
            )


if __name__ == "__main__":
    unittest.mainloop()
