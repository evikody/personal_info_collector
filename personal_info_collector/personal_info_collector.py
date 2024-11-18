while True:
    # Ask the user for personal information
    name = input("Please enter you full name: ")
    age = input("Please enter your age: ")
    address = input("Please enter your address: ")
    number = input("Please enter your phone number: +63")
    email = input("Please enter your email address: ")

    # Variable for all the collected information
    personal_info = f"Full Name: {name}\nAge: {age}\nAddress: {address}\nNumber: {number}\nEmail Address: {email}"

    retry = input("Do you want to enter another person's information? (Yes/No): ").lower()
    if retry != "yes":
        print("Exiting the program...")
        break

    # Prints the personal information
    print(personal_info)