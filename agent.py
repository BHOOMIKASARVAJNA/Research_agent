import os
from typing import Literal
from tavily import TavilyClient #Tavily is used as search provider
from deepagents import create_deep_agent
from dotenv import load_env
load_dotenv()

tavily_client=TavilyClient(os.environ["TAVILAY_API_KEY"])
													 
#Create a search tool
def internet_search(
	query: str,
	max_results: int = 5,
	topic: Literal["general","news","finance","entertainment"]="general",
	include_raw_content: bool=False
):
	"""Run a web search"""
	return tavily_client.search(
		query,
		max_results= max_results,
		topic= topic,
		include_raw_content=include_raw_content
	)

#Create a deep agent
# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.
You have access to an internet search tool as your primary means of gathering information.
## `internet_search`
Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""
agent=create_deep_agent(
	model="google_genai:gemini-1.5-pro",
	tools=[internet_search],
	system_prompt=research_instructions
)

#Run the agent
result=agent.invoke({"messages":[{"role":"user", "content":"What are deepAgents??"}]})
#Print the agent's result/response
print(result["messages"][-1].content)
