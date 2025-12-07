import json
import os

DATA_FILE = "data.json"

# ----------- Step 1: Load or create the JSON file --------------
def load_data():
    if not os.path.exists(DATA_FILE):   # If file doesn't exist → create empty one
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Save updated data into file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# ----------- Step 2: Add a new password ------------------------
def add_password():
    website = input("Website name: ")
    username = input("Username/Email: ")
    password = input("Password: ")

    data = load_data()
    data[website] = {
        "username": username,
        "password": password
    }

    save_data(data)
    print("\nPassword saved successfully!\n")

# ----------- Step 3: View saved passwords ----------------------
def view_passwords():
    data = load_data()

    if not data:
        print("\nNo passwords saved yet.\n")
        return

    print("\n------ Saved Passwords ------")
    for website, details in data.items():
        print(f"Website: {website}")
        print(f"Username: {details['username']}")
        print(f"Password: {details['password']}")
        print("-----------------------------")
    print()

# ----------- Step 4: Main Menu Loop ----------------------------
def main():
    while True:
        print("==== Password Manager ====")
        print("1. Add new password")
        print("2. View saved passwords")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

main()
