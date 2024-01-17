from src.datalayer.base import RepositoryInterface
from src.datalayer.repositorys.mock.customer_repository_mock import CustomerRepositoryMock
from src.services.base import ServiceBase
from src.services.customer_service import CustomerService


class CustomerFactory:
    @staticmethod
    def create_mock():
        repository: RepositoryInterface = CustomerRepositoryMock()
        service: ServiceBase = CustomerService(repository=repository)
        return service
