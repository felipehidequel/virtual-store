from src.domain.customer import Customer
from src.domain.product import Product
from src.domain.order import Order, OrderItem, OrderStatus, OrderStatusName


def test_should_create_order():
    customer: Customer = Customer(name="Felipe", email="felipe@felipe.com")
    status: OrderStatus = OrderStatus()

    assert status.name == OrderStatusName.ACCOMPLISHED

    product1: Product = Product(
        name="PS5",
        description="Produto massa",
        price=3800
    )

    assert product1.name == "PS5"
    assert product1.description == "Produto massa"
    assert product1.price == 3800.0

    product2: Product = Product(
        name="PS4",
        description="Produto top",
        price=2700
    )

    assert product2.name == "PS4"
    assert product2.description == "Produto top"
    assert product2.price == 2700.0

    item1: OrderItem = OrderItem(
        product_id=product1.id, price=product1.price, quantity=1
    )
    item2: OrderItem = OrderItem(
        product_id=product2.id, price=product2.price, quantity=1
    )

    order: Order = Order(customer=customer)
    order.add_status(status=status)
    order.add_item(item=item1)
    order.add_item(item=item2)

    assert len(order.status) == 1
    assert order.status[0].name == OrderStatusName.ACCOMPLISHED
    assert len(order.items) == 2

    # novo status: em preparacao
    status2 = OrderStatus(name=OrderStatusName.IN_PREPARATION)
    order.add_status(status=status2)

    assert len(order.status) == 2

    # novo status: enviado
    status3 = OrderStatus(name=OrderStatusName.SENT)
    order.add_status(status=status3)

    assert len(order.status) == 3

    # novo status: entregue
    status4 = OrderStatus(name=OrderStatusName.DELIVERED)
    order.add_status(status=status4)

    assert len(order.status) == 4

    # novo status: finalizado
    status5 = OrderStatus(name=OrderStatusName.FINISHED)
    order.add_status(status=status5)

    assert len(order.status) == 5

    # verificando total
    assert order.total() == 6500.0
