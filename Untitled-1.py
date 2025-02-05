class Contact:
    def init(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def str(self):
        return f"Όνομα: {self.name}, Τηλέφωνο: {self.phone}, Email: {self.email}"


class AddressBook:
    def init(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Η επαφή προστέθηκε επιτυχώς!")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Η επαφή διαγράφηκε!")
                return
        print("Η επαφή δεν βρέθηκε!")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print("Η επαφή δεν βρέθηκε!")

    def view_contacts(self):
        if not self.contacts:
            print("Η λίστα επαφών είναι άδεια!")
        else:
            for contact in self.contacts:
                print(contact)


def main():
    address_book = AddressBook()

    while True:
        print("\n=== Σύστημα Διαχείρισης Επαφών ===")
        print("1. Προσθήκη Επαφής")
        print("2. Διαγραφή Επαφής")
        print("3. Αναζήτηση Επαφής")
        print("4. Προβολή Όλων των Επαφών")
        print("5. Έξοδος")
        choice = input("Διάλεξε μια επιλογή: ")
if choice == "1":
            name = input("Δώσε όνομα: ")
            phone = input("Δώσε τηλέφωνο: ")
            email = input("Δώσε email: ")
            address_book.add_contact(Contact(name, phone, email))
        elif choice == "2":
            name = input("Δώσε όνομα για διαγραφή: ")
            address_book.delete_contact(name)
        elif choice == "3":
            name = input("Δώσε όνομα για αναζήτηση: ")
            address_book.search_contact(name)
        elif choice == "4":
            address_book.view_contacts()
        elif choice == "5":
            print("Έξοδος από το πρόγραμμα...")
            break
        else:
            print("Μη έγκυρη επιλογή! Δοκίμασε ξανά.")


if name == "main":
    main()