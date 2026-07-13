import random


def generate_customer_id():
    return random.randint(10000, 99999)


def generate_product_id():

    part1 = random.randint(1, 9)
    part2 = random.randint(1000, 9999)
    part3 = random.randint(1000, 9999)
    part4 = random.randint(1, 9)
    
    return f"{part1}-{part2}-{part3}-{part4}"
