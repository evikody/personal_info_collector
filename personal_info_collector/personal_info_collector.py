# A loop that will continue asking until the user input no
while True:

    # A loop that checks if the full name has at least 2 words
    while True:
        name = input("Please enter you full name: ").strip()
        if len(name.split()) < 2:
            print("Invalid. Please enter both your first and last name.")
        else:
            break

    # A loop that checks if the age is valid
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age > 122:
                print("Invalid. Please enter a reasonable and valid age.")
            else:
                break
        except ValueError:
            print("Only numbers are allowed. Try Again.")

    address = input("Please enter your address: ").strip()

    # A loop that checks if the phone number is valid
    while True:
        number = input("Please enter your phone number: +63")
        if len(number) != 10:
            print("Invalid. Please enter a valid phone number.")
        elif not number.isdigit():
            print("Try Again. Only numbers are allowed.")
        else:
            break

    # A loop for asking a valid email address
    while True:
        email = input("Please enter your email address: ").strip()
        if "@" in email and ".com" in email:
            break
        else:
            print("Invalid. Please enter a valid email address")

    # Variable for all the collected information
    personal_info = (f"Full Name: {name}\n"
                     f"Age: {age}\n"
                     f"Address: {address}\n"
                     f"Number: {number}\n"
                     f"Email Address: {email}\n"
                     f"{'-' * 40}\n")

    # Writing the information to the file using "with open"
    with open("./personal_information.txt", "a") as file_handle:
        file_handle.write(personal_info)

    # Ask the user if they want to input another person's information
    retry = input("Do you want to enter another person's information? (Yes/No): ").lower()

    # If the user input "no", then it the program will stop
    if retry != "yes":
        print("Thank you! Have a nice day!")
        break
