# agent.py

import re
import time
import ollama

from prompts import REACT_PROMPT
from tools import AVAILABLE_TOOLS


class OfficeAgent:

    def __init__(self):
        self.model = "llama3"

    def ask_llm(self, prompt):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    def run(self, query):

        start_time = time.time()

        prompt = f"""
{REACT_PROMPT}

User Question:
{query}
"""

        llm_output = self.ask_llm(prompt)

        print("\n===== REASONING =====\n")
        print(llm_output)

        # Extract Thought
        thought_match = re.search(
            r"Thought:\s*(.*)",
            llm_output
        )

        thought = "No reasoning generated"

        if thought_match:
            thought = thought_match.group(1).strip()

        # Extract Action
        action_match = re.search(
            r"Action:\s*(.*)",
            llm_output
        )

        if not action_match:
            return "Could not determine tool."

        tool_name = action_match.group(1).strip().lower()

        # Extract Action Input
        input_match = re.search(
            r"Action Input:\s*([^\n]*)",
            llm_output
        )

        tool_input = ""

        if input_match:
            tool_input = input_match.group(1).strip()

        if tool_input.upper() == "NONE":
            tool_input = ""

        print("\nSelected Tool:", tool_name)

        if tool_name not in AVAILABLE_TOOLS:
            return f"Tool '{tool_name}' not found."

        tool = AVAILABLE_TOOLS[tool_name]

        # Execute Tool

        if tool_name == "current_time":
            observation = tool()

        elif tool_input:
            observation = tool(tool_input)

        else:
            observation = tool()

        response_time = time.time() - start_time

        return f"""
Thought:
{thought}

Action:
{tool_name}

Observation:
{observation}

Final Answer:
{observation}

Response Time:
{response_time:.2f} seconds
"""