from app.planner.planner_agent import planner_agent
from app.planner.tool_executor import execute_tools


incident = {
    "ticket_id": "INC7002",
    "severity": "P1",
    "application": "payment-service",
    "issue": "Database connection pool exhaustion causing payment failures"
}


planner_result = planner_agent(incident)


state = {
    "incident": incident,
    "planner_result": planner_result
}


results = execute_tools(state)

print(results)