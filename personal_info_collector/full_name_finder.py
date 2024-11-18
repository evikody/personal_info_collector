# File path where the personal information is stored
file_path = "./personal_information.txt"

# A loop for searching another name
while True:

    # Ask the user for the full name that they want to search
    search_name = input("Please enter the full name you want to search for: ").strip()

    # Open the file and read its contents
    with open(file_path, "r") as file_handle:
        info = file_handle.readlines()

    # Assume that the name is not found
    name_found = False

    # A loop for searching the name
    for line in info:
        if line.startswith(f"Full Name: {search_name}"):
            name_found = True
            print("\nInformation Found:")

            # Display the searched name
            print(line.strip())

            # Finds the index or position of the variable "line" in the list "info"
            index = info.index(line)

            # Prints the additional information
            print(info[index + 1].strip()) # Age
            print(info[index + 2].strip()) # Address
            print(info[index + 3].strip())  # Phone Number
            print(info[index + 4].strip())  # Email

    if not name_found:
        print("No information found for the given name.")

    # Ask the user if they want to search for another person
    search_again = input("\nDo you want to search for another person? (yes/no): ").lower()
    if search_again != 'yes':
        print("Goodbye!")
        break # If not, the program stops
