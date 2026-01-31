# this password generator will generate 3 combinations

import random
def password_generator():
    charts = str(input("enter symbols for your password:"))
    comb = int(input("how many passwords do you want to generate?"))
    len = int(input("how long your password? should be?"))
    print("your password:")
    print(charts)
    for i in range (comb - 1):
        password = ""
        for x in range(len):
            password += random.choice(charts)
        print(password)

password_generator()
