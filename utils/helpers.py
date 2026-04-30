import os
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_email():
    random_email = generate_random_string(7) + '@gmail.com'
    return random_email


def generate_user_data():
    first_name = generate_random_string(6)
    last_name = generate_random_string(7)
    user_name = generate_random_string(15)
    email = generate_random_email()
    password = generate_random_string(10)

    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "user_name": user_name,
        "email": email,
        "password": password,
    }
    return user_data


def get_upload_file_path(filename):
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(current_dir, "tests", "resources", filename)
