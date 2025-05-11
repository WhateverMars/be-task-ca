from uuid import UUID
from sqlalchemy.orm import Session
from .model import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        return user

    def find_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def find_user_by_id(self, user_id: UUID):
        return self.db.query(User).filter(User.id == user_id).first()
