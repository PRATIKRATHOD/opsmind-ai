from app.planner.planner_agent import planner_agent


incident = {
    "ticket_id": "INC7001",
    "severity": "P1",
    "application": "payment-service",
    "issue": "Database connection pool exhaustion causing payment failures"
}


result = planner_agent(incident)

print(result)