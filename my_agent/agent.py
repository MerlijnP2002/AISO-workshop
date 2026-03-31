"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent

from my_agent.tools.calculator import calculator
from my_agent.tools.pdf_reader import read_pdf
from my_agent.tools.web_search import fetch_webpage, web_search

INSTRUCTION = """
You are a helpful assistant. Answer questions accurately and as succinctly as possible

Reason about your answers, but only return the FINAL answer.

Give only what is asked and use tools when necessary.

Your tools:

- calculator: for everything arithmetic
- pdf_reader: when the file is a .pdf file
- web_search: find current facts, changelogs, statistics, or anything you're unsure about
- fetch_webpage: read the full content of a URL (use after web_search, or when a URL is given in the question)

Check your own answers for correctness but *only* return your final answer.
"""

root_agent = llm_agent.Agent(
    model="gemini-2.5-flash",
    name="agent",
    description="A helpful assistant that answers questions accurately using reasoning and tools.",
    instruction=INSTRUCTION,
    tools=[
        calculator,
        read_pdf,
        web_search,
        fetch_webpage,
    ],
    sub_agents=[],
)
