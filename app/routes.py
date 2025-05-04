from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from .schemas import QueryRequest, QueryResponse, PromptLogSchema
from .langChainService import query_model
from .models import PromptLog
from .db import get_db

router = APIRouter()

@router.post("/ask", response_model=QueryResponse)
async def ask_model(request: QueryRequest, db: AsyncSession = Depends(get_db)):
    answer = await query_model(request.query, db)
    return QueryResponse(answer=answer)

@router.get("/logs", response_model=List[PromptLogSchema])
async def get_logs(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PromptLog).order_by(PromptLog.created_at.desc()))
    logs = result.scalars().all()
    return logs