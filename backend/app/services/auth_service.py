import os
from typing import Optional
import supabase
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserResponse, AuthResponse
from datetime import timedelta


class AuthService:
    """Service for handling authentication operations"""
    
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_KEY")
        
        if self.supabase_url and self.supabase_key:
            self.supabase_client = supabase.create_client(
                self.supabase_url,
                self.supabase_key
            )
        else:
            self.supabase_client = None
    
    def signup(self, email: str, password: str, full_name: str = None) -> AuthResponse:
        """Sign up a new user"""
        if not self.supabase_client:
            raise ValueError("Supabase not configured")
        
        try:
            # Create user in Supabase
            auth_response = self.supabase_client.auth.sign_up({
                "email": email,
                "password": password
            })
            
            # Create user in database
            user = self.user_repo.create_user(
                supabase_id=auth_response.user.id,
                email=email,
                full_name=full_name
            )
            
            # Get access token from Supabase
            access_token = auth_response.session.access_token
            
            return AuthResponse(
                user=UserResponse.from_orm(user),
                access_token=access_token,
                expires_in=3600
            )
        except Exception as e:
            raise ValueError(f"Signup failed: {str(e)}")
    
    def login(self, email: str, password: str) -> AuthResponse:
        """Login user"""
        if not self.supabase_client:
            raise ValueError("Supabase not configured")
        
        try:
            # Authenticate with Supabase
            auth_response = self.supabase_client.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            
            # Get or create user in database
            user = self.user_repo.get_user_by_supabase_id(auth_response.user.id)
            if not user:
                user = self.user_repo.create_user(
                    supabase_id=auth_response.user.id,
                    email=email
                )
            
            access_token = auth_response.session.access_token
            
            return AuthResponse(
                user=UserResponse.from_orm(user),
                access_token=access_token,
                expires_in=3600
            )
        except Exception as e:
            raise ValueError(f"Login failed: {str(e)}")
    
    def logout(self, user_id: str) -> bool:
        """Logout user"""
        return True
    
    def get_user(self, user_id: str) -> Optional[UserResponse]:
        """Get current user"""
        user = self.user_repo.get_user_by_id(user_id)
        if user:
            return UserResponse.from_orm(user)
        return None
