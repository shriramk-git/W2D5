from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load the API key from .env
load_dotenv()

# Initialize the OpenAI chat model
llm = ChatOpenAI(model="gpt-4o-mini")

# Specify the request and formatting rules
prompt = (
    "Provide exactly 5 different healthy South Indian breakfast ideas. "
    "Format as a numbered list from 1 to 5, exactly one line per idea, suggest a fruit and nut "
    "Do not repeat any breakfast idea. "
  
)

# Send the prompt to the model
reply = llm.invoke(prompt)

# Print only the response text
print(reply.content)