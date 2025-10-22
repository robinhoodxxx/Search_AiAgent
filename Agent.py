from http.client import responses
import os
from  dotenv import load_dotenv
from openai import api_key
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()
claude_api_key = os.getenv("CLAUDE_API_KEY")

llm =ChatAnthropic(model="claude-3-5-sonnet-20241022",api_key=claude_api_key)
response = llm.invoke("Hello, my name is dave. What's yours?")
print(response)