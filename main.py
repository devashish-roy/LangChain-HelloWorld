
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello world")
    print(os.environ.get("OPENAI_API_KEY"))



if __name__ ==  "__main__":

    main()
    
