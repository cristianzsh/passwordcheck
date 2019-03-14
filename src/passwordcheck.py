# -*- coding: utf-8 -*-

import getpass
import hashlib
import requests
import sys

def ask_for_password():
    password = getpass.getpass(prompt = "Please type your password: ", stream = None)
    if password == "" or password.isspace():
        print("Please type a password!")
        sys.exit(1)

    password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return password
    

def check_password(password):
    first_characters = password[0:5]
    response = requests.get("https://api.pwnedpasswords.com/range/{}".format(first_characters))
    response = response.text.splitlines()
    for h in response:
        if password[6:] in h:
            return h.split(":")[1]

    return 0

if __name__ == "__main__":
    result = check_password(ask_for_password())
    if result != 0:
        print("Your password has appeared {} times in the database.".format(result))
        print("Source: https://haveibeenpwned.com/")
    else:
        print("No occurrence of the password in the database.")
