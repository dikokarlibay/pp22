import csv
import psycopg2
from connect import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id         SERIAL PRIMARY KEY,
            first_name VARCHAR(50)  NOT NULL,
            phone      VARCHAR(20)  NOT NULL UNIQUE
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created.")


def insert_from_csv(filename="contacts.csv"):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO phonebook (first_name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO NOTHING;
            """, (row["first_name"], row["phone"]))

    conn.commit()
    cur.close()
    conn.close()
    print("Contacts imported from CSV.")


def insert_from_console():
    name  = input("Enter first name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO phonebook (first_name, phone)
        VALUES (%s, %s)
        ON CONFLICT (phone) DO NOTHING;
    """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print(f"Contact {name} added.")


def show_all():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, first_name, phone FROM phonebook ORDER BY id;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    if not rows:
        print("No contacts found.")
    else:
        print(f"{'ID':<5} {'Name':<20} {'Phone':<20}")
        print("-" * 45)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<20}")


def search_by_name():
    name = input("Enter name to search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, first_name, phone FROM phonebook
        WHERE first_name ILIKE %s;
    """, (f"%{name}%",))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    if not rows:
        print("No contacts found.")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")



def search_by_phone():
    prefix = input("Enter phone prefix to search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, first_name, phone FROM phonebook
        WHERE phone LIKE %s;
    """, (f"{prefix}%",))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    if not rows:
        print("No contacts found.")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")



def update_contact():
    name = input("Enter the name of contact to update: ")
    print("What do you want to update?")
    print("1 - Name")
    print("2 - Phone")
    choice = input("Choice: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        new_name = input("Enter new name: ")
        cur.execute("""
            UPDATE phonebook SET first_name = %s
            WHERE first_name ILIKE %s;
        """, (new_name, name))

    elif choice == "2":
        new_phone = input("Enter new phone: ")
        cur.execute("""
            UPDATE phonebook SET phone = %s
            WHERE first_name ILIKE %s;
        """, (new_phone, name))

    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated.")



def delete_by_name():
    name = input("Enter name to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE first_name ILIKE %s;", (name,))

    conn.commit()
    cur.close()
    conn.close()
    print(f"Contact '{name}' deleted.")


def delete_by_phone():
    phone = input("Enter phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print(f"Contact with phone '{phone}' deleted.")



def menu():
    create_table()

    while True:
        print("\n--- PhoneBook ---")
        print("1. Show all contacts")
        print("2. Add contact (console)")
        print("3. Import contacts from CSV")
        print("4. Search by name")
        print("5. Search by phone prefix")
        print("6. Update contact")
        print("7. Delete by name")
        print("8. Delete by phone")
        print("0. Exit")

        choice = input("Choose: ")

        if   choice == "1": show_all()
        elif choice == "2": insert_from_console()
        elif choice == "3": insert_from_csv()
        elif choice == "4": search_by_name()
        elif choice == "5": search_by_phone()
        elif choice == "6": update_contact()
        elif choice == "7": delete_by_name()
        elif choice == "8": delete_by_phone()
        elif choice == "0": break
        else: print("Invalid choice.")


if __name__ == "__main__":
    menu()
