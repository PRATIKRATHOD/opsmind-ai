from app.agents.incident_memory_agent import (
    search_similar_incidents
)


query = """
Database connection pool exhaustion
causing payment failures
"""

result = search_similar_incidents(query)

print(result)