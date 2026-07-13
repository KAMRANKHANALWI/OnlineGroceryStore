from models.product import Product

from dao.product_dao import (
    insert_product,
    get_all_products,
    update_product,
    get_product_by_id,
)

from utils.generators import generate_product_id


def add_product():
    print("\nADD PRODUCT")

    name = input("Product Name : ")
    description = input("Description : ")
    company = input("Company Name : ")
    category = input("Category : ")
    price = float(input("Price : "))
    quantity = int(input("Stock Quantity : "))

    product = Product(
        product_id=generate_product_id(),
        product_name=name,
        description=description,
        company_name=company,
        category=category,
        price=price,
        stock_quantity=quantity,
    )

    insert_product(product)

    print("\nProduct Added Successfully")


def highest_price_product():
    products = get_all_products()

    if not products:
        print("Product List is Empty")
        return

    highest = max(products, key=lambda x: x[5])

    print("\nCostliest Product")

    print(highest)


def sort_products_by_quantity():
    products = get_all_products()

    if not products:
        print("Product List is Empty")
        return

    sorted_products = sorted(products, key=lambda x: x[6], reverse=True)

    print("\nProducts by Quantity")

    for product in sorted_products:
        print(product)


def update_product_details():
    product_id = input("Enter Product ID : ")

    product = get_product_by_id(product_id)

    if not product:
        print("Product Not Found")
        return

    name = input("Name : ")
    description = input("Description : ")
    company = input("Company : ")
    category = input("Category : ")
    price = float(input("Price : "))
    quantity = int(input("Quantity : "))

    update_product = Product(
        product_id, name, description, company, category, price, quantity
    )

    update_product(update_product)

    print("Product Updated Successfully")
