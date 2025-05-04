import os
#from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage
from sqlalchemy.ext.asyncio import AsyncSession

from .models import PromptLog
from .schemas import PromptLogCreate

# Inizializza il modello LLM
"""
llm = ChatOpenAI(
    temperature=0.7,
    model_name=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
"""
llm = ChatOllama(
    temperature=0.7,
    model="mistral",  # o "llama3", "gemma", ecc.
)

async def query_model(prompt: str, db: AsyncSession) -> str:
    # 1. Interroga il modello
    response = await llm.ainvoke([HumanMessage(content=prompt)])
    responseText = response.content

    # 2. Crea log da salvare
    log_entry = PromptLog(
        prompt=prompt,
        response=responseText,
        model_name="mistral"
    )

    # 3. Salva nel database
    db.add(log_entry)
    await db.commit()

    # 4. Restituisci la risposta
    return responseText