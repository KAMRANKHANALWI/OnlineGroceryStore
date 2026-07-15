class Cart:

    def __init__(self, customer_id, product_id, quantity, cart_id=None):

        self.cart_id = cart_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity

    def __str__(self):

        return (
            f"Cart("
            f"cart_id={self.cart_id}, "
            f"customer_id={self.customer_id}, "
            f"product_id={self.product_id}, "
            f"quantity={self.quantity})"
        )
