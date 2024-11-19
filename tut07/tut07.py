import re

def validate_password(password, criteria):
    if len(password) < 8:
        return False, f"Password '{password}' is invalid. Less than 8 characters."

    checks = {
        'uppercase': r'[A-Z]',
        'lowercase': r'[a-z]',
        'numbers': r'[0-9]',
        'special': r'[!@#]'
    }

    for i in criteria:
        if i == '1' and not re.search(checks['uppercase'], password):
            return False, f"Password '{password}' is invalid. Missing uppercase letters."
        elif i == '2' and not re.search(checks['lowercase'], password):
            return False, f"Password '{password}' is invalid. Missing lowercase letters."
        elif i == '3' and not re.search(checks['numbers'], password):
            return False, f"Password '{password}' is invalid. Missing numbers."
        elif i == '4' and not re.search(checks['special'], password):
            return False, f"Password '{password}' is invalid. Missing special characters."

    return True, ""

def main():
    criteria_input = input("Enter criteria to check (1: Uppercase, 2: Lowercase, 3: Numbers, 4: Special characters) separated by commas: ")
    criteria = criteria_input.split(',')

    valid_count = 0
    invalid_count = 0
    messages = []

    # Read from input.txt
    try:
        with open('input.txt', 'r') as file:
            password_list = file.readlines()

        for password in password_list:
            password = password.strip()  # Remove any extra whitespace/newlines
            is_valid, message = validate_password(password, criteria)
            if is_valid:
                valid_count += 1
            else:
                invalid_count += 1
                messages.append(message)

    except FileNotFoundError:
        print("The file input.txt was not found.")
        return

    print(f"Total valid passwords: {valid_count}")
    print(f"Total invalid passwords: {invalid_count}")
    for msg in messages:
        print(msg)

if _name_ == "_main_":
    main()