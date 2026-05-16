def validate_ai_recommendation(llm_response):

    restricted_actions = [
        "restart",
        "delete",
        "shutdown",
        "kill",
        "terminate"
    ]

    detected_actions = []

    response_lower = llm_response.lower()

    for action in restricted_actions:

        if action in response_lower:
            detected_actions.append(action)

    if detected_actions:
        return {
            "approved": False,
            "requires_human_approval": True,
            "detected_actions": detected_actions,
            "message": "Sensitive operational action detected"
        }

    return {
        "approved": True,
        "requires_human_approval": False,
        "detected_actions": [],
        "message": "Response passed safety validation"
    }