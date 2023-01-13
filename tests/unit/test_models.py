# test_models.py
from openai.model.models import Models
import unittest


class testModels(unittest.Test):
    def setup(self):
        self.modelObj = Models()
        self.models = self.modelObj.models
        self.comp = self.modelObj.COMPLETION
        self.comp = self.modelObj.EDIT

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
            for model in list
                self.assertIn("text", model)
                self.assertNotIn("code", model)
                self.assertNotIn("search", model)
                self.assertNotIn("similarity", model)
                self.assertNotIn("insert", model)
                self.assertNotIn("embedding", model)
                self.assertNotIn(":", model)
    
    # tests that the model dictionary does
    # contain the model
    def test_containsModel(self):
        exModel = "text-davinci-003"
        
        self.assertIn(sels.modelObj, exModel)
    
    # tests taht the model dictionar doesn't
    # contain the model
    def test_notContainsModel(self):
        exModel = "text-code-davinci-003"
        
        self.assertIn(self.modelObj, exModel)

    def test_getModels(self):
        self.assertEqual(self.modelObj.getModels(), self.models)