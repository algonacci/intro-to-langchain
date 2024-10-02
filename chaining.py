import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

input_user = input("Insert any words: \n")

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")


from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()


from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

chain = prompt_template | model | parser

print(chain.invoke({"language": "italian", "text": input_user}))