# Contact Book Program

contacts = []  # To store contact information

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return
    
    print("Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

# Function to search for a contact by name or phone
def search_contact():
    query = input("Enter name or phone number to search: ").lower()
    
    found_contacts = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    
    if found_contacts:
        print("Search Results:")
        for contact in found_contacts:
            print(f"{contact['name']} - {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
    else:
        print("No contacts found.\n")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    
    for contact in contacts:
        if contact['name'].lower() == name:
            print(f"Updating contact: {contact['name']}")
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            print("Contact updated successfully!\n")
            return
    
    print("Contact not found.\n")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    
    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully!\n")
            return
    
    print("Contact not found.\n")

# Main menu for the Contact Book
def menu():
    while True:
        print("Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()
