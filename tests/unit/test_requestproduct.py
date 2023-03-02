"""
This module tests the requesthandler module
"""
import unittest
from tests.unit.fixture import api
from openaiclient.model.modelsproduct import *
from openaiclient.model.requestproduct import *

class TestCompletionRequest(unittest.TestCase):
    """
    This class tests the CompletionRequest class.
    """
    
    def setUp(self):
        model = CompletionModels().text_davinci_003
        self.request = CompletionRequest(model)
    
    def test_Request(self):
        """
        Test that the object returned is a copy of the request values
        """
        # they are pointing to different objects in memory, 
        # so the addresses should not be the same.
        self.assertNotEqual(self.request, self.request.request)
    
    def test_RequestValues(self):
        """
        Test that the values for the request object are not RequestSettings objects
        """
        for value in self.request.request.values():
            with self.subTest(value=value):
                self.assertIsNot(value, RequestSetting)
    
    def test_Settings(self):
        """
        Test that the settings for the request object are not RequestSetting objects
        """
        for value in self.request.settings.values():
            with self.subTest(value=value):
                self.assertIsNot(value, RequestSetting)
    
    def test_OptionalArguments(self):
        """
        Test that the optional arguments for the request object are not RequestSetting objects
        """
        for value in self.request.optionalArguments.values():
            with self.subTest(value=value):
                self.assertIsNot(value, RequestSetting)
    
    def test_RequiredArguments(self):
        """
        Test that the required arguments for the request object are not RequestSetting objects
        """
        for value in self.request.requiredArguments.values():
            with self.subTest(value=value):
                self.assertIsNot(value, RequestSetting)
    
    def test_PromptEquality(self):
        """
        Test that when a prompt is entered, the request prompt correctly changes.
        """
        prompt = "this is a test"
        self.request.set_prompt(prompt)
        
        self.assertEqual(self.request.prompt.value, prompt)
    
    def test_PromptError(self):
        """
        Test that when a non-string is entered into the prompt, it throws an AttributeError.
        """
        prompts = [1, 1.0, None, True]
        
        for prompt in prompts:
            val = {"val": prompt}
            with self.subTest(val=val):
                self.assertRaises(AttributeError, self.request.set_prompt, val)