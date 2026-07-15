from models.login import Login
from models.customer import Customer

from dao.login_dao import insert_login, get_login_by_email

from dao.customer_dao import (
    insert_customer,
    update_customer,
    get_customer_by_email,
    get_customer_by_login_id,
    get_all_customers,
)

from utils.constants import CUSTOMER, ACTIVE
from utils.generators import generate_customer_id

from utils.validations import (
    validate_email,
    validate_password,
    validate_contact,
    validate_customer_name,
)


def register_customer():
    print("\nCUSTOMER REGISTRATION")

    name = input("Enter Name (0 to go back) : ")

    if name == "0":
        return

    if not validate_customer_name(name):
        print("Invalid Name")
        return

    email = input("Enter Email (0 to go back): ")

    if email == "0":
        return

    if not validate_email(email):
        print("Invalid Email")
        return

    existing = get_login_by_email(email)

    if existing:
        print("Email already exists")
        return

    password = input("Enter Password (0 to go back): ")

    if password == "0":
        return

    if not validate_password(password):
        print("Password should be 6-12 characters")
        return

    address = input("Enter Address (0 to go back): ")

    if address == "0":
        return

    contact = input("Enter Contact Number (0 to go back): ")

    if contact == "0":
        return

    if not validate_contact(contact):
        print("Contact must be 10 digits")
        return

    login = Login(email=email, password=password, user_type=CUSTOMER, status=ACTIVE)

    login_id = insert_login(login)

    customer = Customer(
        customer_id=generate_customer_id(),
        login_id=login_id,
        customer_name=name,
        address=address,
        contact_number=contact,
    )

    insert_customer(customer)

    print(f"\nCustomer Registration Successful " f"for {customer.customer_id}")


def update_customer_details(user):

    # customer_id = int(input("Enter Customer ID : "))

    customer = get_customer_by_login_id(user[0])

    if not customer:
        print("Customer Not Found")
        return

    print("\nUpdate profile")
    print("Enter 0 anytime to go back")
    name = input("New Name : ")
    if name == "0":
        return
    address = input("New Address : ")
    if address == "0":
        return
    contact = input("New Contact : ")
    if contact == "0":
        return

    updated_customer = Customer(
        customer_id=customer[0],
        login_id=customer[1],
        customer_name=name,
        address=address,
        contact_number=contact,
    )

    update_customer(updated_customer)
    print("Your Details Updated Successfully")


def search_customer_by_email():
    email = input("Enter Customer Email (0 to go back): ")
    if email == "0":
        return
    
    customer = get_customer_by_email(email)

    if customer:
        print("\nCustomer Found")
        print(customer)
    else:
        print("No Such Customer Exist with the Given Email")


def view_profile(user):

    customer = get_customer_by_login_id(user[0])

    if not customer:
        print("Customer Not Found")
        return

    print("\n")
    print("=" * 40)
    print("MY PROFILE")
    print("=" * 40)

    print(f"Customer ID : {customer[0]}")
    print(f"Name : {customer[2]}")
    print(f"Email : {user[1]}")
    print(f"Address : {customer[3]}")
    print(f"Contact : {customer[4]}")
    print(f"Status : {user[4]}")


def view_all_customers():
    customers = get_all_customers()

    if not customers:
        print("No Customers Found")
        return

    print("\nALL CUSTOMERS")

    for customer in customers:
        print(customer)
