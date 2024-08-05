from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
engine = create_async_engine(url=DATABASE_URL, echo=True)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with sessionmaker() as session:
        yield session

