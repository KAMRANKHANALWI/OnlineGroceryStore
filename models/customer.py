class Customer:
    def __init__(
        self,
        customer_id,
        login_id,
        customer_name,
        address,
        contact_number,
    ):
        self.customer_id = customer_id
        self.login_id = login_id
        self.customer_name = customer_name
        self.address = address
        self.contact_number = contact_number

    def __str__(self):
        return (
            f"Customer("
            f"customer_id={self.customer_id}, "
            f"login_id={self.login_id}, "
            f"customer_name='{self.customer_name}', "
            f"address='{self.address}', "
            f"contact_number='{self.contact_number}')"
        )
