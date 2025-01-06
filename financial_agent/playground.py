from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi.api
import phi
import openai
import os
from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app

load_dotenv()
phi.api = os.getenv("PHI_API_KEY")

# AGENT1 - websearch agent will search the web 

web_search_agent = Agent(

    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions=["Always include source"],
    show_tool_calls=True,
    markdown=True

)

## AGENT2 - Financial Agent
Finance_agent = Agent(
    name="Finace AI Agent",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

    
)

app =Playground(agents=[Finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)