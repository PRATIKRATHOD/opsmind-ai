from app.planner.tool_registry import TOOLS
from app.agents.retrieval_query_agent import (
    generate_retrieval_query
)


def execute_tools(state):

    incident = state["incident"]

    selected_tools = state["planner_result"]["selected_tools"]

    results = {}

    print(f"Selected tools: {selected_tools}")

    for tool_name in selected_tools:

        tool = TOOLS.get(tool_name)

        if not tool:

            print(f"Tool not found: {tool_name}")
            continue

        print(f"Executing tool: {tool_name}")

        if tool_name == "rag":
            optimized_query = generate_retrieval_query(
                incident
            )

            result = tool(optimized_query)
            

        else:

            result = tool(incident)

        results[tool_name] = result

    return results