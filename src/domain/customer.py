from src.domain.address import Address
from src.domain.base import DomainBase


class Customer(DomainBase):
    name: str
    email: str
    address: Address

