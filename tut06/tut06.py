def is_valid_pass(password, criteria):
    if len(password) < 8:
        print(f"'{password}' is invalid. Less than 8 characters.")
        return False

    checks = {
        1: any(c.isupper() for c in password),  # Uppercase letters
        2: any(c.islower() for c in password),  # Lowercase letters
        3: any(c.isdigit() for c in password),  # Numbers
        4: any(c in '!@#' for c in password)    # Special characters
    }

    # Check if all selected criteria are met
    return all(checks[c] for c in criteria)

def main():
    # Get user input for criteria
    criteria_input = input("Select criteria (1: Uppercase, 2: Lowercase, 3: Numbers, 4: Special characters) separated by commas: ")
    criteria = list(map(int, criteria_input.split(',')))

    # Get the list of passwords from user input
    password_input = input("Enter passwords separated by commas: ")
    password_list = [password.strip() for password in password_input.split(',')]

    # Validate each password
    for password in password_list:
        if is_valid_pass(password, criteria):
            print(f"'{password}' is a valid password.")
        else:
            print(f"'{password}' is invalid.")
main()