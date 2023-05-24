from langchain.agents import load_tools

from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI

import sys

print(sys.version)

import datetime
from langchain.llms import OpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

llm = OpenAI(temperature=0.8)

echo = llm(
    "Today's date is {}. tell me a joke based on today's date.".format(
        datetime.date.today()
    )
)
print(echo)


llm = ChatOpenAI()
tools = load_tools(
    [
        "python_repl",
        "requests",
        "terminal",
        "wolfram-alpha",
        "serpapi",
        "wikipedia",
        "pal-math",
        "pal-colored-objects",
        "human",
    ],
    llm=llm,
)

agent = initialize_agent(
    tools, llm, agent="chat-zero-shot-react-description", verbose=True
)

agent.run("Ask the human what they want to do")
