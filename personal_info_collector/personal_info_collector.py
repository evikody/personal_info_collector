# A loop that will continue asking until the user input no
while True:
    # A loop that checks if the full name has at least 2 words
    while True:
        # Ask the user for personal information
        name = input("Please enter you full name: ").strip()
        if len(name.split()) < 2:
            print("Invalid. Please enter both your first and last name.")
        else:
            break

    # A loop that checks if the age is valid
    while True:
        age = input("Please enter your age: ")
        if not age.isdigit():
            print("Invalid. Please enter only numbers.")
        else:
            break

    address = input("Please enter your address: ")
    number = input("Please enter your phone number: +63")
    email = input("Please enter your email address: ")

    # Variable for all the collected information
    personal_info = f"Full Name: {name}\nAge: {age}\nAddress: {address}\nNumber: {number}\nEmail Address: {email}"

    # Ask the user if they want to input another person's information
    retry = input("Do you want to enter another person's information? (Yes/No): ").lower()

    # If the user input "no", then it the program will stop
    if retry != "yes":
        print("Exiting the program...")
        break

    # Prints the personal information
    print(personal_info)