import random
import string

def get_user_input():
    password_size = int(input("Enter the size of the password (max 30) "))
    if password_size < 1 and password_size > 30:
        return -1
    mix_upper_lower = input("Do you need to mix upper and lower case? (Yes / No) ").strip().lower() in ('yes', 'y')
    include_numbers = input("Do you need that it has numbers? (Yes / No) ").strip().lower() in ('yes', 'y')
    include_special_char = input("Do you need that it has special characters? (Yes / No) ").strip().lower() in ('yes', 'y')

    return password_size, mix_upper_lower, include_numbers, include_special_char

def generate_password(password_size, mix_upper_lower, include_numbers, include_special_char):
    characters = string.ascii_lowercase
    if mix_upper_lower:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_char:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(password_size))
    return password

def main():
    website = input("Where do you want to use the password? ")
    password_size, mix_upper_lower, include_numbers, include_special_char = get_user_input()
    if password_size == -1:
        print("Error: Password size must be between 1 and 30")
    else:
        password = generate_password(password_size, mix_upper_lower, include_numbers, include_special_char)
        print(f"The new generated password for {website} is {password}")

if __name__ == "__main__":
    main()