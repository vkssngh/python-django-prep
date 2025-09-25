users = {
    "alice": "password123",
    "bob": "mypassword",
    "charlie": "hello123"
}

def login(username, password):
    if username in users and users[username] == password:
        print(f"welcome {username}")
    else:
        print("Invalid username or password.")
    
#test
login("alice", "password123")  # Login successful!`
login("bob", "wrongpassword") # Invalid username or password.`