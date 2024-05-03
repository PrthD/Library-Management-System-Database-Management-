from datetime import datetime
import re
import getpass

def promptForEmail(prompt):
    """
    Purpose: Prompt the user for an email address and validate it against a standard email pattern.
            The function ensures that the entered email matches the standard format before returning it.
            If the input does not match the pattern, the user is prompted again.

    Parameters:
    - prompt (str): The message displayed to the user when asking for input.

    Returns:
    - str: The validated email address in lowercase.
    """
    emailPattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    while True:
        email = input(prompt)
        if emailPattern.match(email):
            return email.lower()
        else:
            print("Invalid Email. Please enter a valid email address, such as 'example@domain.com'.")
            
def promptForNonEmptyPassword(prompt):
    """
    Purpose: Prompt the user for a password using the getpass module, ensuring it is non-empty.
            The password input will not be visible on the screen. The user will be prompted again if the input is empty.

    Parameters:
    - prompt (str): The message displayed to the user when asking for input.

    Returns:
    - str: The non-empty password entered by the user.
    """
    while True:
        password = getpass.getpass(prompt).strip()
        if password:
            return password
        else:
            print("Password cannot be empty. Please enter a valid password.")
            
def promptForNonEmptyName(prompt):
    """
    Purpose: Prompt the user for a name, ensuring that the input is non-empty.
            If the entered name is empty, the user is prompted again.

    Parameters:
    - prompt (str): The message displayed to the user when asking for input.

    Returns:
    - str: The non-empty name entered by the user.
    """
    while True:
        name = input(prompt).strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Please enter a valid name.")           

def promptForOptionalBirthYear(prompt):
    """
    Purpose: Prompt the user for a birth year, allowing the input to be optional.
            The function expects a 4-digit year and ensures that the year is not in the future.
            If the user does not provide an input, None is returned, treating the input as optional.

    Parameters:
    - prompt (str): The message displayed to the user when asking for input.

    Returns:
    - str or None: The validated 4-digit birth year or None if no input is provided.
    """
    current_year = datetime.now().year  # Get the current year

    while True:
        yearText = input(prompt).strip()
        if not yearText:  # No input provided, treat as NULL
            return None
        if yearText.isdigit() and len(yearText) == 4 and int(yearText) <= current_year:
            return yearText
        elif yearText.isdigit() and int(yearText) > current_year:
            print(f"Invalid year. The year cannot be in the future. Please enter a year up to {current_year} or press Enter to skip.")
        else:
            print("Invalid year format. Please enter a 4-digit year or press Enter to skip.")

def promptForOptionalFaculty(prompt):
    """
    Purpose: Prompt the user for a faculty name, allowing the input to be optional.
            If the user does not provide an input, None is returned.

    Parameters:
    - prompt (str): The message displayed to the user when asking for input.

    Returns:
    - str or None: The faculty name entered by the user or None if no input is provided.
    """
    faculty = input(prompt).strip()
    return faculty if faculty else None