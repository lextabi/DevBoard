from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:
    """Repository for User model database operations"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_by_id(self, user_id: str) -> User:
        """Get user by ID"""
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_email(self, email: str) -> User:
        """Get user by email"""
        return self.db.query(User).filter(User.email == email).first()
    
    def get_user_by_supabase_id(self, supabase_id: str) -> User:
        """Get user by Supabase ID"""
        return self.db.query(User).filter(User.supabase_id == supabase_id).first()
    
    def create_user(self, supabase_id: str, email: str, full_name: str = None, avatar_url: str = None) -> User:
        """Create a new user"""
        user = User(
            supabase_id=supabase_id,
            email=email,
            full_name=full_name,
            avatar_url=avatar_url
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def update_user(self, user_id: str, **kwargs) -> User:
        """Update user information"""
        user = self.get_user_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key) and key != "id":
                    setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
        return user
    
    def delete_user(self, user_id: str) -> bool:
        """Delete a user"""
        user = self.get_user_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False
