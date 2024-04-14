import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
LANGUAGE = os.getenv('LANGUAGE')
OPENAI_MODEL = os.getenv('OPENAI_MODEL')

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
