# test_models.py
from openai.model.models import Models
import unittest


class testModels(unittest.Test):
    def setup(self):
        self.modelObj = Models()
        self.models = self.modelObj.models
        self.comp = self.modelObj.COMPLETION
        self.comp = self.modelObj.EDIT
    
    # test that when the model object is
    # initialized, the models follow the
    # designated filters
    def test_modelDictInit(self):
        # assert that comp is a key in dictionary
        self.assertIn(self.comp, self.models.keys())
        # assert that edit is a key in dictionary
        self.assertIn(self.edit, self.models.keys())
        
        # assert the completion models are not empty
        self.assertIsNotEqual(self.models[self.comp], [])
        # assert the edit models are not empty
        self.assertIsNotEqual(self.models[self.edit], [])
        
        # make sure that all models contain
        # the word "text", since that means
        # it is a text model
        for list in self.models.items():
            for model in list
                self.assertIn(model, "text")
                self.assertNotIn(model, "code")
                self.assertNotIn(model, "search")
                self.assertNotIn(model, "similarity")
                self.assertNotIn(model, "insert")
                self.assertNotIn(model, "embedding")
                self.assertNotIn(model, ":")
    
    # tests that the model dictionary does
    # contain the model
    def test_containsModel(self):
        exModel = "text-davinci-003"
        
        self.assertIn(self.modelObj, exModel)
    
    # tests taht the model dictionar doesn't
    # contain the model
    def test_notContainsModel(self):
        exModel = "text-code-davinci-003"
        
        self.assertIn(self.modelObj, exModel)

    def test_getModels(self):
        self.assertEqual(self.modelObj.getModels(), self.models)