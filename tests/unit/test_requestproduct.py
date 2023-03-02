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
    
    def test_Prompt(self):
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
    
    def test_N(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        model = self.request.model.value
        
        vals = range(1, 10)
        
        for val in vals:
            with self.subTest(val=val):
                self.request.set_n(val)

                self.assertEqual(
                    self.request.n.value, 
                    val
                )
    
    def test_NBoundsError(self):
        """
        Asserts that an AttributeError is raised when an input outside the bounds is used.
        """
        model = self.request.model.value
        
        vals = range(-10, 0)
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_n, 
                    val
                )
    
    def test_NTypeError(self):
        """
        Asserts than an AttributeError is raised when an invalid type is inputted.
        """
        model = self.request.model.value
        
        vals = [1.0, "test", True, None]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_n, 
                    val
                )
    
    def test_Stream(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        model = self.request.model.value
        
        vals = [True, False]
        
        for val in vals:
            with self.subTest(val=val):
                self.request.set_stream(val)

                self.assertEqual(
                    self.request.stream.value, 
                    val
                )
    
    def test_StreamTypeError(self):
        """
        Asserts than an AttributeError is raised when an invalid type is inputted.
        """
        model = self.request.model.value
        
        vals = [1, -1.0, "test", None]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_stream, 
                    val
                )
    
    def test_Echo(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        model = self.request.model.value
        
        vals = [True, False]
        
        for val in vals:
            with self.subTest(val=val):
                self.request.set_echo(val)

                self.assertEqual(
                    self.request.echo.value, 
                    val
                )
    
    def test_EchoTypeError(self):
        """
        Asserts than an AttributeError is raised when an invalid type is inputted.
        """
        model = self.request.model.value
        
        vals = [1, -1.0, "test", None]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_echo, 
                    val
                )
    
    def test_Presence_Penalty(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        model = self.request.model.value
        
        vals = [number*0.01 for number in range(-200, 201, 5)]
        
        for val in vals:
            with self.subTest(val=val):
                self.request.set_presence_penalty(val)

                self.assertEqual(
                    self.request.presence_penalty.value, 
                    val
                )
    
    def test_Presence_PenaltyBoundsError(self):
        """
        Asserts that an AttributeError is raised when an input outside the bounds is used.
        """
        model = self.request.model.value
        
        vals = [number*0.01 for number in range(-300, -200, 5)]
        vals = [*vals, *(number*0.01 for number in range(201, 301, 5))]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_presence_penalty, 
                    val
                )
    
    def test_Presence_PenaltyTypeError(self):
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
                    self.request.set_presence_penalty, 
                    val
                )
    
    def test_Frequency_Penalty(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        model = self.request.model.value
        
        vals = [number*0.01 for number in range(-200, 201, 5)]
        
        for val in vals:
            with self.subTest(val=val):
                self.request.set_frequency_penalty(val)

                self.assertEqual(
                    self.request.frequency_penalty.value, 
                    val
                )
    
    def test_Frequency_PenaltyBoundsError(self):
        """
        Asserts that an AttributeError is raised when an input outside the bounds is used.
        """
        model = self.request.model.value
        
        vals = [number*0.01 for number in range(-300, -200, 5)]
        vals = [*vals, *(number*0.01 for number in range(201, 301, 5))]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_frequency_penalty, 
                    val
                )
    
    def test_Frequency_PenaltyTypeError(self):
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
                    self.request.set_frequency_penalty, 
                    val
                )
                
    def test_Best_Of(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        model = self.request.model.value
        
        vals = range(1, 10)
        
        for val in vals:
            with self.subTest(val=val):
                self.request.set_best_of(val)

                self.assertEqual(
                    self.request.best_of.value, 
                    val
                )
    
    def test_Best_OfBoundsError(self):
        """
        Asserts that an AttributeError is raised when an input outside the bounds is used.
        """
        model = self.request.model.value
        
        vals = range(-10, 0)
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_best_of, 
                    val
                )
    
    def test_Best_OfTypeError(self):
        """
        Asserts than an AttributeError is raised when an invalid type is inputted.
        """
        model = self.request.model.value
        
        vals = [1.0, "test", True, None]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_best_of, 
                    val
                )
    
    def test_User(self):
        """
        Test that when a user is entered, the request user correctly changes.
        """
        val = "this is a test"
        self.request.set_user(val)
        
        self.assertEqual(
            self.request.user.value, 
            val
        )
    
    def test_UserTypeError(self):
        """
        Test that when a non-string is entered into the user, it throws an AttributeError.
        """
        vals = [1, 1.0, None, True]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError, 
                    self.request.set_user, 
                    val
                )


class TestEditRequest(unittest.TestCase):
    """
    This class tests the EditRequest class
    """

    def setUp(self):
        model = EditModels().text_davinci_edit_001
        self.request = EditRequest(model)

    def test_Input(self):
        """
        Test that when an input is entered, the request input correctly changes.
        """
        val = "this is a test"
        self.request.set_input(val)
        
        self.assertEqual(self.request.input.value, val)
    
    def test_InputTypeError(self):
        """
        Test that when a non-string is entered into the input, it throws an AttributeError.
        """
        vals = [1, 1.0, None, True]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError, 
                    self.request.set_input, 
                    val
                )

    def test_Instruction(self):
        """
        Test that when an instruction is entered, the request instruction correctly changes.
        """
        val = "this is a test"
        self.request.set_instruction(val)
        
        self.assertEqual(self.request.instruction.value, val)
    
    def test_InstructionTypeError(self):
        """
        Test that when a non-string is entered into the instruction, it throws an AttributeError.
        """
        vals = [1, 1.0, None, True]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError, 
                    self.request.set_instruction, 
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
    
    def test_N(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        model = self.request.model.value
        
        vals = range(1, 10)
        
        for val in vals:
            with self.subTest(val=val):
                self.request.set_n(val)

                self.assertEqual(
                    self.request.n.value, 
                    val
                )
    
    def test_NBoundsError(self):
        """
        Asserts that an AttributeError is raised when an input outside the bounds is used.
        """
        model = self.request.model.value
        
        vals = range(-10, 0)
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_n, 
                    val
                )
    
    def test_NTypeError(self):
        """
        Asserts than an AttributeError is raised when an invalid type is inputted.
        """
        model = self.request.model.value
        
        vals = [1.0, "test", True, None]
        
        for val in vals:
            val = {"val": val}
            with self.subTest(val=val):
                self.assertRaises(
                    AttributeError,
                    self.request.set_n, 
                    val
                )