# File path where the personal information is stored
file_path = "./personal_information.txt"

# Open the file and read its contents
with open(file_path, "r") as file_handle:
    names = file_handle.readlines()
