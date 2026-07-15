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

    name = input("Product Name (0 to go back): ")
    if name == "0":
        return
    description = input("Description (0 to go back): ")
    if description == "0":
        return
    company = input("Company Name (0 to go back): ")
    if company == "0":
        return
    category = input("Category (0 to go back): ")
    if category == "0":
        return
    price = float(input("Price (0 to go back): "))
    if price == "0":
        return
    quantity = int(input("Stock Quantity (0 to go back): "))
    if quantity == "0":
        return

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
    product_id = input("Enter Product ID (0 to go back): ")
    if product_id == "0":
        return

    product = get_product_by_id(product_id)

    if not product:
        print("Product Not Found")
        return

    name = input("Name (0 to go back): ")
    if name == "0":
        return

    description = input("Description (0 to go back): ")
    if description == "0":
        return

    company = input("Company (0 to go back): ")
    if company == "0":
        return

    category = input("Category (0 to go back): ")
    if category == "0":
        return

    price = float(input("Price (0 to go back): "))
    if price == "0":
        return

    quantity = int(input("Quantity (0 to go back): "))
    if quantity == "0":
        return

    update_product = Product(
        product_id, name, description, company, category, price, quantity
    )

    update_product(update_product)

    print("Product Updated Successfully")


def view_all_products():
    products = get_all_products()

    if not products:
        print("No Products Found")
        return

    print("\nALL PRODUCTS")

    for product in products:
        print(product)
