from typing import Optional
from mongoengine import connect, disconnect, get_connection
import logging
from .models import (
    BaseDocument,
    RecruiterProfile,
    Company,
    ChatSession,
    Message,
    Candidate
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database:
    _instance: Optional['Database'] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = False
    
    def init_db(self, mongodb_url: str, db_name: str = 'talent_gpt'):
        """Initialize database connection and ensure collections exist."""
        if self.initialized:
            logger.info("Database already initialized")
            return
            
        try:
            # Disconnect any existing connections
            try:
                disconnect()
            except:
                pass

            # Connect to MongoDB with explicit parameters
            logger.info(f"Connecting to MongoDB at {mongodb_url}, database: {db_name}")
            connect(
                db=db_name,
                host=mongodb_url,
                alias='default',
                connect=False  # Don't connect immediately
            )
            
            # Force connection
            get_connection()
            logger.info("MongoDB connection established")
            
            # Create test document first to ensure database is writable
            logger.info("Creating test document...")
            test_company = Company(
                name="Test Company",
                industry="Technology",
                size="1-10",
                location="Test Location",
                description="Test Description",
                tech_stack=["Python", "MongoDB"]
            )
            test_company.save()
            logger.info("Test document created successfully")
            
            # Now create indexes
            logger.info("Creating indexes for collections...")
            try:
                RecruiterProfile.ensure_indexes()
                logger.info("RecruiterProfile indexes created")
            except Exception as e:
                logger.error(f"Error creating RecruiterProfile indexes: {str(e)}")
                
            try:
                Company.ensure_indexes()
                logger.info("Company indexes created")
            except Exception as e:
                logger.error(f"Error creating Company indexes: {str(e)}")
                
            try:
                ChatSession.ensure_indexes()
                logger.info("ChatSession indexes created")
            except Exception as e:
                logger.error(f"Error creating ChatSession indexes: {str(e)}")
                
            try:
                Message.ensure_indexes()
                logger.info("Message indexes created")
            except Exception as e:
                logger.error(f"Error creating Message indexes: {str(e)}")
                
            try:
                Candidate.ensure_indexes()
                logger.info("Candidate indexes created")
            except Exception as e:
                logger.error(f"Error creating Candidate indexes: {str(e)}")
            
            self.initialized = True
            logger.info("Database initialization completed successfully")
            
        except Exception as e:
            logger.error(f"Error initializing database: {str(e)}")
            self.initialized = False
            raise
    
    def close_db(self):
        """Close database connection."""
        if self.initialized:
            try:
                disconnect()
                self.initialized = False
                logger.info("Database connection closed successfully")
            except Exception as e:
                logger.error(f"Error closing database connection: {str(e)}")
                raise

# Create a singleton instance
db = Database() 