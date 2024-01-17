from pydantic import BaseModel, Field

from src.domains.address import Address
from src.domains.base import DomainBase


class Customer(DomainBase):
    name: str
    email: str
    address: Address = Field(default=None)


class CustomerRegistration(BaseModel):
    name: str
    email: str
    password: str
    confirm_password: str
