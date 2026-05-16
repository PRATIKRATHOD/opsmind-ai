from pydantic import BaseModel


class Incident(BaseModel):
    ticket_id: str
    severity: str
    application: str
    issue: str