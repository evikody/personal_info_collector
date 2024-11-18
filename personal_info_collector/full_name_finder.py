# File path where the personal information is stored
file_path = "./personal_information.txt"

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

if not name_found:
    print("No information found for the given name.")
