from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema in input: quando un utente manda un prompt
class QueryRequest(BaseModel):
    query: str

# Schema in output: risposta del modello
class QueryResponse(BaseModel):
    answer: str

# Schema per leggere i log (ad esempio da un endpoint GET)
class PromptLogSchema(BaseModel):
    id: int
    prompt: str
    response: str
    model_name: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

# Schema per creare un nuovo log (inserimento nel DB)
class PromptLogCreate(BaseModel):
    prompt: str
    response: str
    model_name: Optional[str] = None
