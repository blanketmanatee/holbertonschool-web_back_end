#!/usr/bin/env python3
"""auth module"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """auth class"""

    def __init__(self) -> None:
        """init init init"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """return true if auth"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] is not '/':
            path += '/'
        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
                elif path == paths:
                    return False
        return False

    def authorization_header(self, request=None) -> str:
        """return auth head or none"""
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns user"""
        return None

    def session_cookie(self, request=None):
        """ returns a cookie"""
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
