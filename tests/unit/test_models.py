# test_models.py
import unittest
from openaiclient.model.models import Models


class TestModels(unittest.TestCase):
    def setUp(self):
        self.modelObj = Models()
        self.models = self.modelObj.models
        self.comp = self.modelObj.COMPLETION
        self.edit = self.modelObj.EDIT

    def test_CompletionKeyInDict(self):
        # assert that comp is a key in dictionary
        self.assertIn(self.comp, self.models.keys())

    def test_EditKeyInDict(self):
        # assert that edit is a key in dictionary
        self.assertIn(self.edit, self.models.keys())

    def test_CompletionListNotEmpty(self):
        # assert the completion models are not empty
        self.assertTrue(self.models[self.comp])

    def test_EditListNotEmpty(self):
        # assert the completion models are not empty
        self.assertTrue(self.models[self.edit])

    def test_ModelsFilterCorrectly(self):
        # make sure that all models contain
        # the word "text", since that means
        # it is a text model
        for list in self.models.items():
            for model in list:
                with self.subTest(model=model):
                    self.assertIn("text", model)
                    self.assertNotIn("code", model)
                    self.assertNotIn("search", model)
                    self.assertNotIn("similarity", model)
                    self.assertNotIn("insert", model)
                    self.assertNotIn("embedding", model)
                    self.assertNotIn(":", model)

    # tests that the model dictionary does
    # contain the model
    def test_ContainsModel(self):
        exModel = "text-davinci-003"

        self.assertIn(exModel, self.modelObj)

    # tests that the model dictionary doesn't
    # contain the model
    def test_NotContainsModel(self):
        exModel = "text-code-davinci-003"

        self.assertIn(exModel, self.modelObj)

    def test_GetModels(self):
        self.assertEqual(self.modelObj.getModels(), self.models)


if __name__ == "__main__":
    unittest.mainloop()
