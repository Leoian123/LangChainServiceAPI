import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Carica variabili d’ambiente
from dotenv import load_dotenv
load_dotenv()

# URL di connessione
DATABASE_URL = (
    f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# Crea l'engine asincrono
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Crea la factory per la sessione
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base per i modelli
Base = declarative_base()

# Dependency da usare nei router (es: Depends(get_db))
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
