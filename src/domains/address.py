from src.domains.base import DomainBase
from pydantic import Field


class Address(DomainBase):
    street: str
    neighborhood: str
    number: int
    complement: str = Field(default=None)
    postal_zone: str
    city: str
    state: str
    country: str