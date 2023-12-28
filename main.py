import requests
import json
from flare import Flare  

# Your backend API credentials and URL
parse_app_id = "VBP2GdaFTeWVJeVj18zFVYDzgmbYtWXZ9AEBc3pw"
parse_rest_key = "3CMdswsApRrzG9CzbyhCAMa49LA277lyN99Ji7b3"
base_url = "https://parseapi.back4app.com/classes"

# List of available classes
classes = ["NPC", "Quest", "Item", "Combat", "Inventory"]  # Add more classes as needed

# Headers for API requests
headers = {
    "X-Parse-Application-Id": parse_app_id,
    "X-Parse-REST-API-Key": parse_rest_key,
    "Content-Type": "application/json"
}

class CloudFunctionMenu:
    def __init__(self):
        self.cloud_modules = {
            "LangchainIntegration": ["generateNPCDialogue", "generateNPCDescription", "generateSpecialAbilities"],
            "NPC": ["createNPC", "deleteNPC"],
            "Combat": ["startCombat", "endCombat"],
            "Inventory": ["addItem", "removeItem"]
        }
        self.base_url = "https://parseapi.back4app.com/functions/"
        self.cloud_function_menu()
    def cloud_function_menu(self):
        while True:
            print("Select a Cloud Code Module:")
            modules = list(self.cloud_modules.keys())
            for i, module in enumerate(modules):
                print(f"{i + 1}. {module}")
            print(f"{len(modules) + 1}. Exit")
            choice = int(input("Enter your choice: "))
            
            if choice == len(modules) + 1:
                break
            elif 1 <= choice <= len(modules):
                self.list_functions(modules[choice - 1])
            else:
                print("Invalid choice. Try again.")

    def list_functions(self, module):
        if module == "Flare":
            self.execute_flare_functions()
        else:
            functions = self.cloud_modules[module]
            print(f"Functions in {module}:")
            for i, func in enumerate(functions):
                print(f"{i + 1}. {func}")
            func_choice = int(input("Select a function to execute: "))
            
            if 1 <= func_choice <= len(functions):
                self.execute_function(module, functions[func_choice - 1])
            else:
                print("Invalid choice. Returning to module selection.")

    def execute_flare_functions(self):
        flare = Flare(state="INIT")  # Initialize Flare module
        functions = flare.get_functions()  # Get available functions from Flare module

        while True:
            print("Select a Flare Module function:")
            for i, func in enumerate(functions, start=1):
                print(f"{i}. {func}")
            print(f"{len(functions) + 1}. Exit")
            choice = int(input("Enter your choice: "))
            
            if choice == len(functions) + 1:
                break
            elif 1 <= choice <= len(functions):
                flare.execute_function(functions[choice - 1])  # Execute the chosen Flare function
            else:
                print("Invalid choice. Try again.")

def perform_crud_operation(base_url, selected_class, headers):
    while True:
        print(f"CRUD Menu for {selected_class}")
        print("1. Create")
        print("2. Retrieve")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input(f"Enter {selected_class} name: ")
            description = input(f"Enter {selected_class} description: ")
            payload = json.dumps({"Name": name, "Description": description})
            response = requests.post(f"{base_url}/{selected_class}", headers=headers, data=payload)
            print(f"{selected_class} Created:", response.json())

        elif choice == "2":
            object_id = input(f"Enter {selected_class} object ID: ")
            response = requests.get(f"{base_url}/{selected_class}/{object_id}", headers=headers)
            print(f"{selected_class} Details:", response.json())

        elif choice == "3":
            object_id = input(f"Enter {selected_class} object ID: ")
            name = input(f"Enter new {selected_class} name: ")
            payload = json.dumps({"Name": name})
            response = requests.put(f"{base_url}/{selected_class}/{object_id}", headers=headers, data=payload)
            print(f"{selected_class} Updated:", response.json())

        elif choice == "4":
            object_id = input(f"Enter {selected_class} object ID: ")
            response = requests.delete(f"{base_url}/{selected_class}/{object_id}", headers=headers)
            if response.status_code == 200:
                print(f"{selected_class} Deleted")
            else:
                print("Error:", response.json())

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    while True:
        print("Select an operation:")
        print("1. CRUD Operations")
        print("2. Cloud Function Menu")
        print("3. Flare Module Functions")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Select a class for CRUD operations
            print("Select a class for CRUD operations:")
            for i, cls in enumerate(classes):
                print(f"{i + 1}. {cls}")
            class_choice = int(input("Enter your choice: "))
            selected_class = classes[class_choice - 1]

            # Perform CRUD operations for the selected class
            perform_crud_operation(base_url, selected_class, headers)

        elif choice == "2":
            CloudFunctionMenu()
        elif choice == "3":
            flare_menu = CloudFunctionMenu()
            flare_menu.execute_flare_functions()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
