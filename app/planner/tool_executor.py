from app.planner.tool_registry import TOOLS


def execute_tools(state):

    incident = state["incident"]

    selected_tools = state["planner_result"][
        "selected_tools"
    ]

    results = {}

    print(f"Selected tools: {selected_tools}")

    for tool_name in selected_tools:

        tool = TOOLS.get(tool_name)

        if not tool:

            print(f"Tool not found: {tool_name}")
            continue

        print(f"Executing tool: {tool_name}")

        if tool_name == "rag":

            query = f"""
            Application:
            {incident["application"]}

            Issue:
            {incident["issue"]}

            Severity:
            {incident["severity"]}

            """

            result = tool(query)

        else:

            result = tool(incident)

        results[tool_name] = result

    return results