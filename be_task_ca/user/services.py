from .model import User
from .schema import CreateUserRequest, CreateUserResponse
import hashlib


class UserExistsException(Exception):
    pass


class UserService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, create_user: CreateUserRequest) -> CreateUserResponse:
        existing_user = self.user_repository.find_user_by_email(create_user.email)
        if existing_user:
            raise UserExistsException("An user with this email adress already exists")

        new_user = User(
            first_name=create_user.first_name,
            last_name=create_user.last_name,
            email=create_user.email,
            hashed_password=hashlib.sha512(
                create_user.password.encode("UTF-8")
            ).hexdigest(),
            shipping_address=create_user.shipping_address,
        )

        self.user_repository.save_user(new_user)

        return CreateUserResponse(
            id=new_user.id,
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            email=new_user.email,
            shipping_address=new_user.shipping_address,
        )
