#!/usr/bin/env python3
"""BasicAuth to import"""
from api.v1.auth.auth import Auth
import base64
from base64 import b64decode, binascii
from models.user import User
from typing import TypeVar, List


class BasicAuth(Auth):
    """BasicAuth class"""
    def __init__(self) -> None:
        """init init init"""

    def extract_base64_authorization_header(
                                            self,
                                            authorization_header: str
                                            ) -> str:
        """ returns header in base64 or None"""
        if authorization_header is None\
            or type(authorization_header) != str\
            or not authorization_header.startswith('Basic ')\
                and not authorization_header.endswith(' '):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
                                            self,
                                            base64_authorization_header: str
                                            ) -> str:
        """ decode base 64 header """
        if (not base64_authorization_header or
                type(base64_authorization_header) != str):
            return None
        try:
            base64_b = base64_authorization_header.encode('utf-8')
            string_bytes = base64_b.b64decode(base64_b)
            return string_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ get user """
        if decoded_base64_authorization_header is None or\
            type(decoded_base64_authorization_header) != str or\
                ':' not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(':', 1)
        return (credentials[0], credentials[1])

        def user_object_from_credentials(self,
                                         user_email: str, user_pwd:
                                         str) -> TypeVar('User'):
            """returns instance or None """
            if user_email is None or type(user_email) != str or\
                    user_pwd is None or type(user_pwd) != str:
                return None
            try:
                user = User.search({'email': user_email})
            except Exception:
                return None

            if user and user[0].is_valid_pwd(user_pwd):
                return user[0]
            return None

        def current_user(self, request=None) -> TypeVar('User'):
            """ returns infor on users"""
            header: self.authorization_header(request)
            auth_header = self.extract_base64_authorization_header(data)
            decoded = self.decode_base64_authorization_header(auth_header)
            user, pwd = self.extract_user_credentials(decoded)
            return self.user_object_from_credentials(user,pwd)
            
