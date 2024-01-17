from src.domain.product import Product


def test_should_create_product():
    product: Product = Product(
        name="Notebook Samsung",
        description="Ryzen 5, 8gb de RAM, SSD de 512gb",
        price=2800.0
    )

    assert product.name == "Notebook Samsung"
    assert product.description == "Ryzen 5, 8gb de RAM, SSD de 512gb"
    assert product.price == 2800.0
