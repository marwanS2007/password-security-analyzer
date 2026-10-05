import random
import string


# List of common passwords that should automatically be considered weak
COMMON_PASSWORDS = [
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "letmein",
    "admin123"
]


# This function analyzes the password and gives it a security score
def analyze_password(password):

    # Start the password score at 0
    score = 0

    # This list will store recommendations for the user
    feedback = []


    # Check the length of the password
    if len(password) >= 12:
        score += 2

    elif len(password) >= 8:
        score += 1

    else:
        feedback.append("Use at least 8 characters.")


    # Check if the password contains an uppercase letter
    if any(char.isupper() for char in password):
        score += 1

    else:
        feedback.append("Add an uppercase letter.")


    # Check if the password contains a lowercase letter
    if any(char.islower() for char in password):
        score += 1

    else:
        feedback.append("Add a lowercase letter.")


    # Check if the password contains a number
    if any(char.isdigit() for char in password):
        score += 1

    else:
        feedback.append("Add a number.")


    # Check if the password contains a special character
    if any(char in string.punctuation for char in password):
        score += 1

    else:
        feedback.append("Add a special character.")


    # Check if the password is in our common-password list
    if password.lower() in COMMON_PASSWORDS:

        # Set the score to 0 because common passwords are unsafe
        score = 0

        feedback.append(
            "This password is commonly used and should be avoided."
        )


    # Check if the password contains ONLY letters or ONLY numbers
    if password.isalpha() or password.isdigit():

        score -= 1

        feedback.append(
            "Avoid passwords containing only letters or numbers."
        )


    # Prevent the score from becoming negative
    score = max(score, 0)


    # Determine password strength based on the final score
    if score <= 2:
        strength = "WEAK"

    elif score <= 4:
        strength = "MODERATE"

    else:
        strength = "STRONG"


    # Send the results back
    return score, strength, feedback


# This function creates a random strong password
def generate_password(length=16):

    # Combine letters, numbers, and special characters
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    # Start with an empty password
    password = ""


    # Repeat based on the requested password length
    for i in range(length):

        # Pick a random character and add it to the password
        password += random.choice(characters)


    # Return the completed password
    return password


# Program title
print("============================")
print("PASSWORD SECURITY ANALYZER")
print("============================")


# Keep the program running until the user chooses Exit
while True:

    # Display the menu
    print("\n1. Analyze Password")
    print("2. Generate Strong Password")
    print("3. Exit")


    # Ask the user what they want to do
    choice = input("\nChoose an option: ")


    # OPTION 1 - Analyze a password
    if choice == "1":

        password = input("\nEnter password: ")


        # Run the password through our analyzer
        score, strength, feedback = analyze_password(password)


        # Display the results
        print("\n----------------------------")
        print("PASSWORD ANALYSIS")
        print("----------------------------")

        print(f"Security Rating: {strength}")
        print(f"Score: {score}/6")


        # If there are security recommendations, display them
        if feedback:

            print("\nRecommendations:")

            for recommendation in feedback:
                print(f"- {recommendation}")

        else:
            print("\nNo major weaknesses detected.")


    # OPTION 2 - Generate a password
    elif choice == "2":

        print("\nGenerated Password:")
        print(generate_password())


    # OPTION 3 - Exit the program
    elif choice == "3":

        print("\nProgram closed.")
        break


    # Handles invalid menu choices
    else:

        print("\nInvalid option. Please choose 1, 2, or 3.")
