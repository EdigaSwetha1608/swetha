class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        print("\nEnter contact details:")
        name = input("Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")

        self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
        print(f"\nContact {name} added successfully!")

    def view_contacts(self):
        print("\nContact List:")
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")
        print()

    def search_contact(self):
        query = input("Enter name or phone number to search: ").lower()
        results = []

        for name, details in self.contacts.items():
            if query in name.lower() or query in details['phone_number']:
                results.append((name, details))

        return results

    def update_contact(self):
        name = input("Enter name of the contact to update: ")

        if name in self.contacts:
            print("\nEnter updated contact details:")
            phone_number = input("New Phone Number: ")
            email = input("New Email: ")
            address = input("New Address: ")

            self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
            print(f"\nContact {name} updated successfully!")
        else:
            print(f"\nContact {name} not found!")

    def delete_contact(self):
        name = input("Enter name of the contact to delete: ")

        if name in self.contacts:
            del self.contacts[name]
            print(f"\nContact {name} deleted successfully!")
        else:
            print(f"\nContact {name} not found!")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            contact_manager.add_contact()

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            results = contact_manager.search_contact()
            if results:
                print("\nSearch Results:")
                for name, details in results:
                    print(f"Name: {name}, Phone: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")
            else:
                print("\nNo matching contacts found.")

        elif choice == '4':
            contact_manager.update_contact()

        elif choice == '5':
            contact_manager.delete_contact()

        elif choice == '6':
            print("\nExiting Contact Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()