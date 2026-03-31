"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent

from my_agent.tools.calculator import calculator
from my_agent.tools.pdf_reader import read_pdf

INSTRUCTION = """
You are a helpful assistant. Answer questions accurately and concisely.

Always use tools when they help:
- If the message contains a file path ending in .pdf, call read_pdf with that exact path before answering.
- Use calculator for any non-trivial arithmetic.

Return only the answer — no extra explanation unless asked.
"""

root_agent = llm_agent.Agent(
    model="gemini-2.5-flash",
    name="agent",
    description="A helpful assistant that answers questions accurately using reasoning and tools.",
    instruction=INSTRUCTION,
    tools=[
        calculator,
        read_pdf,
        # web_search,     <- uncomment after Milestone 4
        # fetch_webpage,  <- uncomment after Milestone 4
        # read_image,     <- uncomment after Milestone 5
    ],
    sub_agents=[],
)
