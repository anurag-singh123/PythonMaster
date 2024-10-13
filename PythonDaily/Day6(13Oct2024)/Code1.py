# Write a Python program that reads a JSON file, parses it, and prints specific values based on user input (e.g., finding a particular user's data in a list).

import json

def read_json_file(file_path):
    """
    Reads a JSON file and returns the parsed data
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def find_user_data(data, user_id):
    """
    Finds and returns a user's data in the list based on the user ID
    """
    for user in data['users']:
        if user['id'] == user_id:
            return user
    return None

def main():
    file_path = input("Enter the path to the JSON file: ")
    user_id = input("Enter the user ID to find: ")

    data = read_json_file(file_path)
    user_data = find_user_data(data, user_id)

    if user_data:
        print("User  Data:")
        print("---------")
        print(f"ID: {user_data['id']}")
        print(f"Name: {user_data['name']}")
        print(f"Email: {user_data['email']}")
    else:
        print("User  not found")

if __name__ == "__main__":
    main()