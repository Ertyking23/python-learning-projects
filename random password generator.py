import random
import string

def generate_password():
    length = int(input("how many characters should be in your password enter a whole number (min. 4)? ").strip())
    special_characters = input("does your password need special characters (Y/N)? ").strip().upper()
    upper_characters = input("does your password need uppercase characters (Y/N)? ").strip().upper()
    number_characters = input("does your password need numbers (Y/N)? ").strip().upper()
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if upper_characters == "Y" else ""
    special = string.punctuation if special_characters == "Y" else ""
    numbers = string.digits if number_characters == "Y" else ""
    all_caracters = lower + upper + special + numbers

    if length < 4:
        print("your password is too short")
    else:
        required_characters = []
        if upper_characters == "Y":
            required_characters.append(random.choice(upper))
        if special_characters == "Y":
            required_characters.append(random.choice(special))
        if number_characters == "Y":
            required_characters.append(random.choice(numbers))
            remaining_length = length - len(required_characters)
            password = required_characters
            for _ in range(remaining_length):
                char = random.choice(all_caracters)
                password.append(char)
                random.shuffle(password)
            str_password = "".join(password)
            return str_password


password=generate_password()
print(str(password))