class Product:

    def __init__(
        self,
        product_id,
        product_name,
        description,
        company_name,
        category,
        price,
        stock_quantity,
    ):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.company_name = company_name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return (
            f"Product("
            f"product_id='{self.product_id}', "
            f"product_name='{self.product_name}',"
            f"price={self.price},"
            f"stock_quantity={self.stock_quantity})"
        )
