#!/usr/bin/env python3
"""Session Auth"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import Dict, TypeVar
from uuid import uuid4, UUID


class SessionAuth(Auth):
    """Auth class"""
    user_id_by_session_id: Dict = {}

    def create_session(self, user_id: str = None) -> str:
        """ create a session and register in class"""
        if user_id is None or type(User) is not str:
            return None
        
        session_id: str = str(uuid4())
        self.user_id_by_session_id[session_id] = User

        return session_id
    
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Create user id based on session id"""
        if session_id is None or type(session_id) is not str:
            return None
        user_id: str = self.user_id_by_session_id.get(session_id)

        return user_id
    
    def current_user(self, request=None):
        """show the current user"""
        session_id: str = self.session_cookie(request)
        user_id: str = self.user_id_for_session_id(session_id)
        user: TypeVar('User') = User.get(user_id)

        return user

    def destroy_session(self, request=None):
        """destroys the session"""
        if request is None:
            return False
        session_id: str = self.session_cookie(request)

        if session_id is None:
            return False
        
        user_id: str = self.user_id_for_session_id(session_id)

        if user_id is None:
            return False
        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            pass
        return True