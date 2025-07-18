# import csv
import os
# import re
from test_utils import is_valid_email, read_users_from_csv


# def read_users_from_csv(file_path):
#     with open(file_path, newline='') as csvfile:
#         return list(csv.DictReader(csvfile))

# def is_valid_email(email):
#     return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email))

def test_user_emails_have_valid_format():
    test_file = os.path.join("data", "sample_users.csv")
    users = read_users_from_csv(test_file)

    for user in users:
        email = user["email"].strip()
        if email:  # Only test non-empty emails
            assert is_valid_email(email), f"Invalid email: {email}"