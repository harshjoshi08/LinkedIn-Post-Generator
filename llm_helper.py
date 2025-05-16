from langchain_groq import ChatGroq
import os

# Directly assign your API key here
GROQ_API_KEY = "Your_GROQ_API_Key_Here"  # Replace with your actual API key

# Create the LLM client
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model="llama3-70b-8192")

if __name__ == "__main__":
    response = llm.invoke("What is the capital of France?")
    print(response.content)
