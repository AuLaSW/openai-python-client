from os import environ
import openai
from model.aiModels import getModels

# get API key from usr folder
openai.api_key = environ["OPENAI_API_KEY"]
