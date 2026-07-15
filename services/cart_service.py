from dao.product_dao import get_all_products

from models.cart import Cart

from dao.cart_dao import add_to_cart, view_cart, remove_from_cart

from dao.customer_dao import get_customer_by_login_id

from dao.product_dao import get_product_by_id


def view_products_for_customer():

    products = get_all_products()

    if not products:

        print("No Products Available")
        return

    print("\n")
    print("=" * 70)
    print("PRODUCT CATALOG")
    print("=" * 70)

    for product in products:

        availability = "Available" if product[6] > 0 else "Out Of Stock"

        print(
            f"ID: {product[0]} | "
            f"{product[1]} | "
            f"₹{product[5]} | "
            f"{availability}"
        )


def add_product_to_cart(user):

    customer = get_customer_by_login_id(user[0])

    product_id = input("Enter Product ID (0 to return): ")

    if product_id == "0":
        return

    product = get_product_by_id(product_id)

    if not product:

        print("Product Not Found")
        return

    quantity = int(input("Enter Quantity: "))

    if quantity > product[6]:
        print("Insufficient Stock")
        return

    cart = Cart(customer_id=customer[0], product_id=product_id, quantity=quantity)

    add_to_cart(cart)

    print("Product Added To Cart")


def display_cart(user):

    # Get customer details using login ID
    customer = get_customer_by_login_id(user[0])

    # Get all cart items of the customer
    cart_items = view_cart(customer[0])

    # If cart is empty
    if not cart_items:

        print("\nYour Cart Is Empty")
        return

    print("\n")
    print("=" * 50)
    print("MY CART")
    print("=" * 50)

    cart_total = 0

    # Loop through every cart item
    for item in cart_items:

        # Cart table structure:
        # item[0] -> cart_id
        # item[1] -> customer_id
        # item[2] -> product_id
        # item[3] -> quantity

        cart_id = item[0]
        product_id = item[2]
        quantity = item[3]

        # Get complete product details
        product = get_product_by_id(product_id)

        # Product table structure:
        # product[0] -> product_id
        # product[1] -> product_name
        # product[2] -> description
        # product[3] -> company_name
        # product[4] -> category
        # product[5] -> price
        # product[6] -> stock_quantity

        product_name = product[1]
        company_name = product[3]
        price = product[5]

        # Calculate total price of this cart item
        item_total = price * quantity

        # Add item total to complete cart total
        cart_total += item_total

        print()
        print(f"Cart ID      : {cart_id}")
        print(f"Product      : {product_name}")
        print(f"Company      : {company_name}")
        print(f"Price        : ₹{price}")
        print(f"Quantity     : {quantity}")
        print(f"Item Total   : ₹{item_total}")
        print("-" * 50)

    print()
    print(f"CART TOTAL   : ₹{cart_total}")
    print("=" * 50)


def remove_product_from_cart(user):

    # Get customer details using login ID
    customer = get_customer_by_login_id(user[0])

    # Get all cart items of the customer
    cart_items = view_cart(customer[0])

    # Check if cart is empty
    if not cart_items:

        print("\nYour Cart Is Empty")
        return

    print("\n")
    print("=" * 50)
    print("REMOVE PRODUCT FROM CART")
    print("=" * 50)

    # Loop through every cart item
    for item in cart_items:

        # Cart table structure:
        # item[0] -> cart_id
        # item[1] -> customer_id
        # item[2] -> product_id
        # item[3] -> quantity

        cart_id = item[0]
        product_id = item[2]
        quantity = item[3]

        # Get complete product details
        product = get_product_by_id(product_id)

        # Get product name and price
        product_name = product[1]
        price = product[5]

        # Calculate item total
        item_total = price * quantity

        print(
            f"Cart ID: {cart_id} | "
            f"Product: {product_name} | "
            f"Qty: {quantity} | "
            f"Total: ₹{item_total}"
        )

    print("=" * 50)

    # Ask customer which cart item to remove
    cart_id = input("\nEnter Cart ID To Remove (0 to return): ")

    # Return to customer menu
    if cart_id == "0":
        return

    # Remove only if the cart item belongs
    # to the currently logged-in customer
    deleted_rows = remove_from_cart(int(cart_id), customer[0])

    if deleted_rows == 0:

        print("\nInvalid Cart ID")

        return

    print("\nItem Removed Successfully")
