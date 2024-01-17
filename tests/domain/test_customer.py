from src.domain.customer import Customer


def test_should_create_customer():
    customer: Customer = Customer(name="Kennedy", email="kennedy@kenys.com")

    assert customer.name == "Kennedy"
    assert customer.email == "kennedy@kenys.com"
