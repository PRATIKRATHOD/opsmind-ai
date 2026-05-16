from app.agents.monitoring_agent import monitoring_agent
from app.agents.log_analysis_agent import log_analysis_agent
from app.agents.vector_knowledge_agent import vector_knowledge_agent


TOOLS = {

    "monitoring": monitoring_agent,

    "logs": log_analysis_agent,

    "rag": vector_knowledge_agent
}