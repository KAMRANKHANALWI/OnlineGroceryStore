from database.create_tables import create_tables

from services.auth_service import login

from services.customer_service import (
    register_customer,
    update_customer_details,
    search_customer_by_email,
)

from services.product_service import (
    add_product,
    highest_price_product,
    sort_products_by_quantity,
)


def admin_menu():

    while True:
        print("\n")
        print("=" * 40)
        print("ADMIN MENU")
        print("=" * 40)

        print("1. Add Product")
        print("2. Update Product")
        print("3. Search Customer")
        print("4. Highest Price Product")
        print("5. Sort Products By Quantity")
        print("6. Logout")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            update_customer_details()
        elif choice == "3":
            search_customer_by_email()
        elif choice == "4":
            highest_price_product()
        elif choice == "5":
            sort_products_by_quantity()
        elif choice == "6":
            print("\nAdmin Logged Out")
            break
        else:
            print("Invalid Choice")


def customer_menu():

    while True:
        print("\n")
        print("=" * 40)
        print("CUSTOMER MENU")
        print("=" * 40)

        print("1. Update Profile")
        print("2. Logout")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            update_customer_details()
        elif choice == "2":
            print("\nCustomer Logged Out")
            break
        else:
            print("Invalid Choice")


def main():

    create_tables()

    while True:
        print("=" * 40)
        print("ONLINE GROCERY STORE")
        print("=" * 40)

        print("1. Customer Registration")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            register_customer()
        elif choice == "2":
            user = login()

            if user:
                role = user[3]

                if role == "ADMIN":
                    admin_menu()
                elif role == "CUSTOMER":
                    customer_menu()
                else:
                    print("Unknown Role")
        elif choice == "3":
            print("\nThank You")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
