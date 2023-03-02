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
        Test that the
        """