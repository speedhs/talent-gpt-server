from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, Dict, Any
import os

class Database:
    client: Optional[AsyncIOMotorClient] = None
    db = None

    @classmethod
    async def connect_db(cls):
        """Create database connection."""
        cls.client = AsyncIOMotorClient(os.getenv("MONGODB_URL", "mongodb://localhost:27017"))
        cls.db = cls.client.talent_gpt_db

    @classmethod
    async def close_db(cls):
        """Close database connection."""
        if cls.client:
            cls.client.close()

    @classmethod
    async def get_collection(cls, collection_name: str):
        """Get a collection from the database."""
        if not cls.db:
            await cls.connect_db()
        return cls.db[collection_name]

    @classmethod
    async def insert_one(cls, collection_name: str, document: Dict[str, Any]):
        """Insert a single document into a collection."""
        collection = await cls.get_collection(collection_name)
        result = await collection.insert_one(document)
        return result.inserted_id

    @classmethod
    async def find_one(cls, collection_name: str, query: Dict[str, Any]):
        """Find a single document in a collection."""
        collection = await cls.get_collection(collection_name)
        return await collection.find_one(query)

    @classmethod
    async def find_many(cls, collection_name: str, query: Dict[str, Any], limit: int = 10):
        """Find multiple documents in a collection."""
        collection = await cls.get_collection(collection_name)
        cursor = collection.find(query).limit(limit)
        return await cursor.to_list(length=limit) 