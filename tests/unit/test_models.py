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

    def test_CompletionModels(self):
        for model in self.modelObj.completionModels:
            with self.subTest(model=model):
                self.assertEqual(model.type, self.modelObj.COMPLETION)

    def test_EditModels(self):
        for model in self.modelObj.editModels:
            with self.subTest(model=model):
                self.assertEqual(model.type, self.modelObj.EDIT)
    
    def test_Text_Davinci_003(self):
        self.assertEqual(
            self.modelObj.text_davinci_003.name,
            "text-davinci-003"
        )
    
    def test_Text_Curie_001(self):
        self.assertEqual(
            self.modelObj.text_curie_001.name,
            "text-curie-001"
        )
    
    def test_Text_Babbage_001(self):
        self.assertEqual(
            self.modelObj.text_babbage_001.name,
            "text-babbage-001"
        )
    
    def test_Text_Ada_001(self):
        self.assertEqual(
            self.modelObj.text_ada_001.name,
            "text-ada-001"
        )
    
    def test_Text_Davinci_Edit_003(self):
        self.assertEqual(
            self.modelObj.text_davinci_edit_003.name,
            "text-davinci-edit-003"
        )
    

if __name__ == "__main__":
    unittest.mainloop()
