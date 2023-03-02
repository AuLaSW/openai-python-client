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
    
    def test_PromptTypeError(self):
        """
        Test that when a non-string is entered into the prompt, it throws an AttributeError.
        """
        prompts = [1, 1.0, None, True]
        
        for prompt in prompts:
            val = {"val": prompt}
            with self.subTest(val=val):
                self.assertRaises(AttributeError, self.request.set_prompt, val)
    
    def test_Max_Tokens(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        model = self.request.model.value
        
        tokens = [*range(1, model.max_tokens, 50), model.max_tokens]
        
        for max_tokens in tokens:
            with self.subTest(max_tokens=max_tokens):
                self.request.set_max_tokens(max_tokens)

                self.assertEqual(
                    self.request.max_tokens.value, 
                    max_tokens
                )
    
    def test_Max_TokensBoundsError(self):
        """
        Asserts that an AttributeError is raised when an input outside the bounds is used.
        """
        model = self.request.model.value
        
        tokens = [*range(-10, 1), *range(model.max_tokens + 1, model.max_tokens + 10)]
        
        for max_tokens in tokens:
            val = {"val": max_tokens}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_max_tokens, 
                    val
                )
    
    def test_Max_TokensTypeError(self):
        """
        Asserts than an AttributeError is raised when an invalid type is inputted.
        """
        model = self.request.model.value
        
        tokens = ["test", True, None]
        
        for max_tokens in tokens:
            val = {"val": max_tokens}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_max_tokens, 
                    val
                )
    
    def test_Temperature(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        model = self.request.model.value
        
        temps = [number*0.01 for number in range(0, 201, 5)]
        
        for temp in temps:
            with self.subTest(temp=temp):
                self.request.set_temperature(temp)

                self.assertEqual(
                    self.request.temperature.value, 
                    temp
                )
    
    def test_TemperatureBoundsError(self):
        """
        Asserts that an AttributeError is raised when an input outside the bounds is used.
        """
        model = self.request.model.value
        
        temps = [number*0.01 for number in range(-200, 1, 5)]
        
        for temp in temps:
            val = {"val": temp}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_temperature, 
                    val
                )
    
    def test_TemperatureTypeError(self):
        """
        Asserts than an AttributeError is raised when an invalid type is inputted.
        """
        model = self.request.model.value
        
        temps = [1, "test", True, None]
        
        for temp in temps:
            val = {"val": temp}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_temperature, 
                    val
                )
    
    def test_Top_P(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        model = self.request.model.value
        
        vals = [number*0.01 for number in range(0, 101, 5)]
        
        for val in vals:
            with self.subTest(val=val):
                self.request.set_top_p(val)

                self.assertEqual(
                    self.request.top_p.value, 
                    val
                )
    
    def test_Top_PBoundsError(self):
        """
        Asserts that an AttributeError is raised when an input outside the bounds is used.
        """
        model = self.request.model.value
        
        vals = [number*0.01 for number in range(-100, 1, 5)]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_top_p, 
                    val
                )
    
    def test_Top_PTypeError(self):
        """
        Asserts than an AttributeError is raised when an invalid type is inputted.
        """
        model = self.request.model.value
        
        vals = [1, "test", True, None]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_top_p, 
                    val
                )