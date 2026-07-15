from database.create_tables import create_tables

from services.auth_service import login

from services.customer_service import (
    register_customer,
    update_customer_details,
    search_customer_by_email,
    view_profile,
    view_all_customers,
)

from services.product_service import (
    add_product,
    update_product_details,
    highest_price_product,
    sort_products_by_quantity,
    view_all_products,
)

from services.cart_service import (
    view_products_for_customer,
    add_product_to_cart,
    display_cart,
    remove_product_from_cart,
)

from services.transaction_service import checkout


def admin_menu():

    while True:

        print("\n")
        print("=" * 40)
        print("ADMIN MENU")
        print("=" * 40)

        print("1. Add Product")
        print("2. Update Product")
        print("3. Search Customer")
        print("4. View All Customers")
        print("5. Highest Price Product")
        print("6. Sort Products By Quantity")
        print("7. View All Products")
        print("8. Logout")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            add_product()

        elif choice == "2":

            update_product_details()

        elif choice == "3":

            search_customer_by_email()

        elif choice == "4":

            view_all_customers()

        elif choice == "5":

            highest_price_product()

        elif choice == "6":

            sort_products_by_quantity()

        elif choice == "7":

            view_all_products()

        elif choice == "8":

            print("\nAdmin Logged Out")
            break

        else:

            print("\nInvalid Choice")


def customer_menu(user):

    while True:

        print("\n")
        print("=" * 40)
        print("CUSTOMER MENU")
        print("=" * 40)

        print("1. View Profile")
        print("2. Update Profile")
        print("3. View Products")
        print("4. Add Product To Cart")
        print("5. View Cart")
        print("6. Remove Product From Cart")
        print("7. Checkout")
        print("8. Logout")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            view_profile(user)

        elif choice == "2":

            update_customer_details(user)

        elif choice == "3":

            view_products_for_customer()

        elif choice == "4":

            add_product_to_cart(user)

        elif choice == "5":

            display_cart(user)

        elif choice == "6":

            remove_product_from_cart(user)

        elif choice == "7":

            checkout(user)

        elif choice == "8":

            print("\nCustomer Logged Out")
            break

        else:

            print("\nInvalid Choice")


def main():

    create_tables()

    while True:

        print("\n")
        print("=" * 40)
        print("ONLINE GROCERY STORE")
        print("=" * 40)

        print("1. Customer Registration")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            register_customer()

        elif choice == "2":

            user = login()

            if user:

                role = user[3]

                if role == "ADMIN":

                    admin_menu()

                elif role == "CUSTOMER":

                    customer_menu(user)

                else:

                    print("Unknown Role")

        elif choice == "3":

            print("\nThank You!")
            break

        else:

            print("\nInvalid Choice")


if __name__ == "__main__":
    main()
