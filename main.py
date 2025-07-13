# Matthew Paul Mangus
# Jun. 21, 2025
# Password Generator
# Short Script That Generates Password with Length (Integer) Input
# In-Line comments
# Updated last: July 13, 2025

# Import Statements:

import secrets
import string


def generate_password(length: int) -> string:
    """
    Generates a random password.

    Args:
        length (int): Length of the password.

    Returns:
        str: The generated password.
    """

    password = ''.join(secrets.choice
                       (string.ascii_letters + string.digits)
                       for i in range(length))
    return password


if __name__ == '__main__':
    length = int(input("Length of password: "))
    print("Password: " + generate_password(length))
