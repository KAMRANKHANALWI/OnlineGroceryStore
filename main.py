from database.create_tables import create_tables

from services.customer_service import register_customer

from services.product_service import (
    add_product,
    highest_price_product,
    sort_products_by_quantity,
)


def main():

    create_tables()

    while True:
        print("=" * 40)
        print("ONLINE GROCERY STORE")
        print("=" * 40)

        print("1. Register Customer")
        print("2. Add Product")
        print("3. Highest Price Product")
        print("4. Sort Products By Quantity")
        print("5. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            register_customer()
        elif choice == "2":
            add_product()
        elif choice == "3":
            highest_price_product()
        elif choice == "4":
            sort_products_by_quantity()
        elif choice == "5":
            print("Thank You")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
