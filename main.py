from src.domains.customer import CustomerRegistration
from src.factories.customer_factory import CustomerFactory

service = CustomerFactory.create_mock()

customer = CustomerRegistration(
    name="Felipe",
    email="felipe@felip",
    password="123456",
    confirm_password="123456"
)

response = service.register(customer_registration=customer)

print(response)
