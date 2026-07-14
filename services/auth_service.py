from dao.login_dao import validate_login


def login():

    email = input("Enter Email : ")
    password = input("Enter Password : ")

    user = validate_login(email, password)

    if user:
        print(f"\n Welcome {user[3]}")
        return user
    print("\nInvalid Credentials")

    return None
