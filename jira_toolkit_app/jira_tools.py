import os
from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.jira.toolkit import JiraToolkit
from langchain_community.utilities.jira import JiraAPIWrapper
from langchain_openai import OpenAI
from pydantic import BaseModel


        
# Setting up the OpenAI language model
llm = OpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

# Initializing JiraAPIWrapper and JiraToolkit
jira = JiraAPIWrapper(
    jira_api_token=os.getenv("JIRA_API_TOKEN"),
    jira_username=os.getenv("JIRA_USERNAME"),
    jira_instance_url=os.getenv("JIRA_INSTANCE_URL"),
    jira_cloud=os.getenv("JIRA_CLOUD")
)
toolkit = JiraToolkit.from_jira_api_wrapper(jira)

# Set up the agent with tools from the toolkit
agent = initialize_agent(
    toolkit.get_tools(),
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Define a function to interact with the agent
def interact_with_jira_agent(query: str):
    return agent.run(query)


