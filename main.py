import csv
users = {}
def start():
    while True:
        main_menu = input("""
Welcome to the crew!
Would you like to register (R) or log in (L)?
Press Q to quit.
> """)

        main_menu = main_menu.strip().upper()

        if main_menu == "R":
            register()
        elif main_menu == "L":
            print("Welcome to the login page!")
            login()
        elif main_menu == "Q":
            print("Thank you for using our app!")
            break
        else:
            print("Invalid option. Please enter R, L, or Q.")


def register():
    username = input("Please enter a username for your account: ").strip().lower()
    if username in users:
        print("Username already exists. Please choose another username.")
        return
    email = input("Please enter your email address: ").strip().lower()
    if "@" not in email or "." not in email:
        print("Invalid email address.")
        return
    password = input("Please enter a password for your account: ")
    users[username] = {
        "email": email,
        "password": password
    }
    save_users(username, email, password)
    print(f"User {username} registered successfully!")

def save_users(username, email, password):
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, email, password])

def load_users():
    try:
        with open("users.csv", mode="r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                username = row[0]
                email = row[1]
                password = row[2]

                users[username] = {
                    "email": email,
                    "password": password
                }
    except FileNotFoundError:
        pass

def login():
    username = input("Please enter your username: ").strip().lower()

    if username in users:
        password = input("Please enter your password: ").strip()

        if password == users[username]["password"]:
            print(f"User {username} logged in successfully!")
            print(f"Email: {users[username]['email']}")
            logged_in(username)
        else:
            print("Wrong password.")
    else:
        print("User not found.")

def logged_in(username):
    hub = input("""
          Welcome to the logged-in area! You can now access your account features.
          (1) Display account information
          (2) Log out
          """)
    if hub == "1":
        print("Account Information:")
        print(f"Username: {username}")
        print(f"Email: {users[username]['email']}")
    elif hub == "2":
        print("Logging out...")
        return
    else:
        print("Invalid option. Please enter 1 or 2.")
        logged_in(username)

if __name__ == "__main__":
    try:
        load_users()
        start()
    except KeyboardInterrupt:
        print("Goodbye!")
