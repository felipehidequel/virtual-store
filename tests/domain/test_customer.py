from src.domains.address import Address
from src.domains.customer import Customer


def test_should_create_customer():
    address: Address = Address(
        street="Rua Manoel Joaquim",
        neighborhood="Belos Campos",
        number=132,
        postal_zone="59988-000",
        city="Natal",
        state="RN",
        country="Brasil"
    )

    customer: Customer = Customer(name="Kennedy", email="kennedy@kenys.com", address=address)

    assert customer.name == "Kennedy"
    assert customer.email == "kennedy@kenys.com"
    assert customer.address.street == "Rua Manoel Joaquim"
    assert customer.address.neighborhood == "Belos Campos"
    assert customer.address.number == 132
    assert customer.address.postal_zone == "59988-000"
    assert customer.address.city == "Natal"
    assert customer.address.state == "RN"
    assert customer.address.country == "Brasil"
    assert customer.address.complement is None
