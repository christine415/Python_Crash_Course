current_users = ["admin", "Chris", "Bob", "Joe", "David"]
new_users = ["ChRIS", "Bob", "Katy", "Adele", "Linda"]
for user in new_users:
    if user.lower() in [users.lower() for users in current_users]:
        print("You need to enter a new username.")
    else:
        print("The username is available.")

