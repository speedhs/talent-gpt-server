"""
MongoDB models package.
"""

from mongoengine import connect
from .base import BaseDocument
from .profile import RecruiterProfile
from .company import Company
from .chat import ChatSession, Message
from .candidate import Candidate, Skill

__all__ = [
    'BaseDocument',
    'RecruiterProfile',
    'Company',
    'ChatSession',
    'Message',
    'Candidate',
    'Skill'
]

def init_models(mongodb_url: str):
    """Initialize MongoDB connection and ensure all collections are created."""
    connect(host=mongodb_url) 