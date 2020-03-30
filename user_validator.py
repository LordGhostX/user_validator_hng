from random import sample
import string


def capture_user_data():
    # ask for the user details
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")

    # generate password
    random_token = "".join(sample(string.ascii_letters, 5))
    password = first_name[:2] + random_token + last_name[len(last_name) - 2:]

    # show the user the password and ask if they are satisfied
    print("Your password is", password)
    if input("Are you satisfied with your password (y/n)? ").lower() == "n":
        # if the user is not satisfied ask them for a password
        while True:
            password = input("Enter any password you wish to have: ")
            if len(password) > 7:
                break
            print("Enter a password that is longer than 7 characters")

    return first_name, last_name, email, password


# all users on the platform
users = []

# capture new user data
first_name, last_name, email, password = capture_user_data()

# save the user data in the container
users.append({
    "first_name": first_name,
    "last_name": last_name,
    "email": email,
    "password": password
})

# display user data
for user in users:
    print()
    for data in user:
        print("{}: {}".format(data, user[data]))
