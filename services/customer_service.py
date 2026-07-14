from models.login import Login
from models.customer import Customer

from dao.login_dao import insert_login, get_login_by_email

from dao.customer_dao import (
    insert_customer,
    update_customer,
    get_customer_by_id,
    get_customer_by_email,
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

    name = input("Enter Name : ")

    if not validate_customer_name(name):
        print("Invalid Name")
        return

    email = input("Enter Email : ")

    if not validate_email(email):
        print("Invalid Email")
        return

    existing = get_login_by_email(email)

    if existing:
        print("Email already exists")
        return

    password = input("Enter Password : ")

    if not validate_password(password):
        print("Password should be 6-12 characters")
        return

    address = input("Enter Address : ")

    contact = input("Enter Contact Number : ")

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


def update_customer_details():

    customer_id = int(input("Enter Customer ID : "))

    customer = get_customer_by_id(customer_id)

    if not customer:
        print("Customer Not Found")
        return

    name = input("New Name : ")
    address = input("New Address : ")
    contact = input("New Contact : ")

    updated_customer = Customer(
        customer_id=customer_id,
        login_id=customer[1],
        customer_name=name,
        address=address,
        contact_number=contact,
    )

    update_customer(updated_customer)
    print("Your Details Updated Successfully")


def search_customer_by_email():
    email = input("Enter Customer Email : ")
    customer = get_customer_by_email(email)

    if customer:
        print("\nCustomer Found")
        print(customer)
    else:
        print("No Such Customer Exist with the Given Email")
