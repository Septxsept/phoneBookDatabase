




import sqlite3






def create_table():
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()

    # Create Entries table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def add_entry():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")

    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()

    # Insert a new entry
    cursor.execute('''
        INSERT INTO Entries (name, phone_number)
        VALUES (?, ?)
    ''', (name, phone_number))

    conn.commit()
    conn.close()

def lookup_entry():
    name = input("Enter name to lookup: ")

    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()

    # Lookup entry by name
    cursor.execute('''
        SELECT name, phone_number FROM Entries
        WHERE name = ?
    ''', (name,))

    result = cursor.fetchone()
    conn.close()

    if result:
        print(f"Phone number for {result[0]}: {result[1]}")
    else:
        print(f"No entry found for {name}")

def update_entry():
    name = input("Enter name to update: ")
    new_phone_number = input("Enter new phone number: ")

    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()

    # Update entry's phone number
    cursor.execute('''
        UPDATE Entries
        SET phone_number = ?
        WHERE name = ?
    ''', (new_phone_number, name))

    conn.commit()
    conn.close()

def delete_entry():
    name = input("Enter name to delete: ")

    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()

    # Delete entry by name
    cursor.execute('''
        DELETE FROM Entries
        WHERE name = ?
    ''', (name,))

    conn.commit()
    conn.close()

# Create the table if it doesn't exist
create_table()

while True:
    print("\nPhonebook Menu:")
    print("1. Add Entry")
    print("2. Lookup Entry")
    print("3. Update Entry")
    print("4. Delete Entry")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_entry()
    elif choice == '2':
        lookup_entry()
    elif choice == '3':
        update_entry()
    elif choice == '4':
        delete_entry()
    elif choice == '5':
        print("Exiting Phonebook. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
