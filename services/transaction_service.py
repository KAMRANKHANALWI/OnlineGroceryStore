from dao.customer_dao import get_customer_by_login_id

from dao.cart_dao import view_cart, clear_cart

from dao.product_dao import get_product_by_id, update_product_stock

from datetime import datetime

from dao.transaction_dao import save_transaction, save_transaction_item


def checkout(user):

    customer = get_customer_by_login_id(user[0])

    cart_items = view_cart(customer[0])

    if not cart_items:

        print("Your Cart Is Empty")
        return

    total_amount = 0
    total_items = 0

    print("\n")
    print("=" * 50)
    print("ORDER SUMMARY")
    print("=" * 50)

    for item in cart_items:
        product = get_product_by_id(item[2])

        quantity = item[3]

        # if quantity > product[6]:
        #     print(f"Insufficient Stock " f"for {product[1]}")
        #     return

        price = product[5]

        subtotal = price * quantity

        total_amount += subtotal
        total_items += quantity

        print(f"{product[1]} " f"x {quantity} " f"= Rs. {subtotal}")

    print("-" * 50)

    print(f"Total Items : {total_items}")
    print(f"Total Amount : Rs. {total_amount}")

    print("\nSelect Payment Method")

    print("1. COD")
    print("2. UPI")
    print("3. Credit Card")
    print("4. Debit Card")
    print("5. Net Banking")

    choice = input("Enter Choice: ")

    payment_methods = {
        "1": "COD",
        "2": "UPI",
        "3": "Credit Card",
        "4": "Debit Card",
        "5": "Net Banking",
    }

    payment_method = payment_methods.get(choice)

    if not payment_method:
        print("Invalid Payment Method")
        return

    confirm = input("Proceed To Buy? (Y/N): ")

    if confirm.upper() != "Y":
        print("Order Cancelled")
        return

    transaction_id = save_transaction(
        customer_id=customer[0],
        payment_method=payment_method,
        total_amount=total_amount,
        no_of_items=total_items,
        transaction_date=str(datetime.now()),
    )

    for item in cart_items:

        product = get_product_by_id(item[2])

        quantity = item[3]

        price = product[5]

        save_transaction_item(transaction_id, product[0], quantity, price)

        remaining_stock = product[6] - quantity

        update_product_stock(product[0], remaining_stock)

    print("\n")
    print("=" * 50)
    print("INVOICE")
    print("=" * 50)

    print(f"Transaction ID : " f"{transaction_id}")

    print(f"Customer ID : " f"{customer[0]}")

    print(f"Payment Mode : " f"{payment_method}")

    print(f"Total Items : " f"{total_items}")

    print(f"Total Amount : " f"₹{total_amount}")

    print("=" * 50)

    clear_cart(customer[0])

    print("\nTransaction Completed Successfully")
