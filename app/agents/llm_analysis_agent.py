import ollama


def llm_analysis_agent(
    incident,
    monitoring_result,
    log_result,
    knowledge_result,
     memory_result
):

    prompt = f"""
    You are an AI Operations Engineer.

    Analyze this production incident.

    Ticket ID: {incident["ticket_id"]}
    Severity: {incident["severity"]}
    Application: {incident["application"]}
    Issue: {incident["issue"]}

    Monitoring Result:
    {monitoring_result}

    Log Analysis Result:
    {log_result}

    Knowledge Base Recommendation:
    {knowledge_result}

    Historical Similar Incidents:
    {memory_result}

    Provide:
    1. Root cause summary
    2. Recommended remediation
    3. Operational impact
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

    return response["message"]["content"]