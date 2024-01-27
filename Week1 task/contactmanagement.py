class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name not in self.contacts:
            self.contacts[name] = {'Phone': phone, 'Email': email}
            print(f"Contact '{name}' added successfully.")
        else:
            print(f"Contact '{name}' already exists.")

    def view_contact(self, name):
        if name in self.contacts:
            contact_info = self.contacts[name]
            print(f"Name: {name}\nPhone: {contact_info['Phone']}\nEmail: {contact_info['Email']}")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            contact_info = self.contacts[name]
            if phone:
                contact_info['Phone'] = phone
            if email:
                contact_info['Email'] = email
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def list_contacts(self):
        print("Contacts:")
        for name, contact_info in self.contacts.items():
            print(f"Name: {name}\nPhone: {contact_info['Phone']}\nEmail: {contact_info['Email']}\n---")


def main():
    contact_manager = ContactManager()

    while True:
        print("\n1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_manager.add_contact(name, phone, email)

        elif choice == '2':
            name = input("Enter name: ")
            contact_manager.view_contact(name)

        elif choice == '3':
            name = input("Enter name: ")
            phone = input("Enter new phone (press Enter to keep the existing one): ")
            email = input("Enter new email (press Enter to keep the existing one): ")
            contact_manager.update_contact(name, phone, email)

        elif choice == '4':
            name = input("Enter name: ")
            contact_manager.delete_contact(name)

        elif choice == '5':
            contact_manager.list_contacts()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()