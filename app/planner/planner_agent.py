import ollama


def planner_agent(incident):

    prompt = f"""
    You are an AI Operations Planner.

    Analyze this production incident and decide which tools are required.

    Available tools:
    - monitoring
    - logs
    - rag

    Incident:
    Application: {incident["application"]}
    Issue: {incident["issue"]}

    Return ONLY comma-separated tool names.

    Example:
    monitoring,logs,rag
    """

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    print(f"Planner response: {content}")

    tools = [
        tool.strip().lower()
        for tool in content.split(",")
    ]
    if "rag" not in tools:
        tools.append("rag")

    return {
        "selected_tools": tools
    }