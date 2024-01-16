# virtual-store
ordering system in python applying the concepts of OOP, DDD and TDD

- Customer
    name
    email

- Product
    name
    description
    price

- Order
    [OrderStatus]
    [OrderItem]
    total

- OrderStatus
    name (REALIZADO, EM PREPARACAO, ENVIADO, ENTREGUE, FINALIZADO)

- OrderItem
    - product_id
    - price
    - quantity