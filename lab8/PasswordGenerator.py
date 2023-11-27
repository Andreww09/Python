import random


def generate_password(length, numbers=True, mixed_case=True, special_characters=True):
    """ generates a random password of a given length

        :param int length the length of the password

        :param bool numbers True if the password should include numbers

        :param bool mixed_case True if the password should include both uppercase and lowercase letters

        :param bool special_characters True if the password should include special characters
    """
    assert (length > 0), "Length should be a positive number"

    data = []  # character pool from which the password is created
    password = ""
    special = "!@#$%^&*()_+-={}|:\"<>?,./;\'[]\\"

    # add letters
    for i in range(0, 26):
        data.append(chr(ord('a') + i))
        # add uppercase letters
        if mixed_case:
            data.append(chr(ord('A') + i))
    # add numbers
    if numbers:
        for i in range(0, 10):
            data.append(str(i))
    # add special characters
    if special_characters:
        for el in special:
            data.append(el)
    # generate password
    for i in range(0, length):
        poz = random.randrange(0, len(data))
        password += data[poz]
    return password
