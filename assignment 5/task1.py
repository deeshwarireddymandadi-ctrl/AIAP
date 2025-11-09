import hashlib
import json
import os
from getpass import getpass

class LoginSystem:
    def __init__(self, credentials_file="credentials.json"):
        self.credentials_file = credentials_file
        self._ensure_credentials_file()

    def _ensure_credentials_file(self):
        """Create credentials file if it doesn't exist"""
        if not os.path.exists(self.credentials_file):
            with open(self.credentials_file, 'w') as f:
                json.dump({}, f)

    def _hash_password(self, password: str) -> str:
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username: str, password: str) -> bool:
        """Register a new user"""
        with open(self.credentials_file, 'r') as f:
            credentials = json.load(f)
        
        if username in credentials:
            return False
        
        credentials[username] = self._hash_password(password)
        
        with open(self.credentials_file, 'w') as f:
            json.dump(credentials, f)
        return True

    def login(self, username: str, password: str) -> bool:
        """Verify login credentials"""
        with open(self.credentials_file, 'r') as f:
            credentials = json.load(f)
        
        if username not in credentials:
            return False
        
        return credentials[username] == self._hash_password(password)

def main():
    login_system = LoginSystem()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            username = input("Enter username: ").strip()
            password = getpass("Enter password: ")
            
            if login_system.register(username, password):
                print("Registration successful!")
            else:
                print("Username already exists!")
                
        elif choice == "2":
            username = input("Enter username: ").strip()
            password = getpass("Enter password: ")
            
            if login_system.login(username, password):
                print("Login successful!")
            else:
                print("Invalid credentials!")
                
        elif choice == "3":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()