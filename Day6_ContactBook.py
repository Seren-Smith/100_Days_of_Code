def main():
    contacts = {}

    print("🌟 Welcome to the Contact Book! 🌟")

    while True:
        print("\nMain Menu:")
        print("1. Add a Contact")
        print("2. View a Contact")
        print("3. Update a Contact")
        print("4. Delete a Contact")
        print("5. Show All Contacts")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            show_all_contacts(contacts)
        elif choice == "6":
            print("\nThank you for using the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


def add_contact(contacts):
    print("\n➕ Add a New Contact")
    name = input("Enter full name: ").strip()

    if name in contacts:
        print(f"A contact with the name '{name}' already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    notes = input("Enter notes (optional, press Enter to skip): ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "notes": notes if notes else "No notes"
    }
    print(f"\n✅ Contact '{name}' added successfully!")


def view_contact(contacts):
    print("\n👀 View a Contact")
    name = input("Enter the name of the contact to view: ").strip()

    if name in contacts:
        print(f"\n📋 Contact Details for {name}:")
        print(f"  Phone: {contacts[name]['phone']}")
        print(f"  Email: {contacts[name]['email']}")
        print(f"  Notes: {contacts[name]['notes']}")
    else:
        print(f"\n❌ Contact '{name}' not found.")


def update_contact(contacts):
    print("\n🔄 Update a Contact")
    name = input("Enter the name of the contact to update: ").strip()

    if name not in contacts:
        print(f"\n❌ Contact '{name}' not found.")
        return

    print("\nCurrent Contact Information:")
    print(f"1. Phone: {contacts[name]['phone']}")
    print(f"2. Email: {contacts[name]['email']}")
    print(f"3. Notes: {contacts[name]['notes']}")

    field_choice = input("\nWhich field would you like to update? (1-3, or 'cancel' to abort): ").strip().lower()

    if field_choice == "cancel":
        print("Update cancelled.")
        return

    if field_choice == "1":
        new_value = input("Enter new phone number: ").strip()
        contacts[name]['phone'] = new_value
        print("Phone number updated successfully!")
    elif field_choice == "2":
        new_value = input("Enter new email address: ").strip()
        contacts[name]['email'] = new_value
        print("Email address updated successfully!")
    elif field_choice == "3":
        new_value = input("Enter new notes: ").strip()
        contacts[name]['notes'] = new_value if new_value else "No notes"
        print("Notes updated successfully!")
    else:
        print("Invalid choice. Update cancelled.")


def delete_contact(contacts):
    print("\n❌ Delete a Contact")
    name = input("Enter the name of the contact to delete: ").strip()

    if name not in contacts:
        print(f"\n❌ Contact '{name}' not found.")
        return

    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Deletion cancelled.")


def show_all_contacts(contacts):
    print("\n📖 All Contacts")

    if not contacts:
        print("No contacts found.")
        return

    for name, info in contacts.items():
        print(f"\n👤 {name}:")
        print(f"  📞 Phone: {info['phone']}")
        print(f"  ✉️ Email: {info['email']}")
        print(f"  📝 Notes: {info['notes']}")

    print(f"\nTotal contacts: {len(contacts)}")


if __name__ == "__main__":
    main()
