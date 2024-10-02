import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]



from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

# result = model.invoke(messages)

# print(parser.invoke(result))


chain = model | parser

print(chain.invoke(messages))