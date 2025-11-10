class BankAccount:
    """
    A simple bank account class with basic operations.
    
    Attributes:
        account_number: Unique identifier for the account
        holder_name: Name of the account holder
        balance: Current balance in the account
        transactions: List of transaction records
    """
    
    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0.0):
        """Initialize a new bank account"""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
            
        self.account_number = str(account_number)
        self.holder_name = str(holder_name)
        self._balance = float(initial_balance)  # private attribute
        self.transactions = []
        
        if initial_balance > 0:
            self.transactions.append(f"Initial deposit: ${initial_balance:.2f}")
    
    def deposit(self, amount: float) -> bool:
        """
        Deposit money into account.
        Returns True if successful, False otherwise.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
                
            self._balance += amount
            self.transactions.append(f"Deposit: ${amount:.2f}")
            return True
            
        except (ValueError, TypeError) as e:
            self.transactions.append(f"Failed deposit: {str(e)}")
            return False
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from account.
        Returns True if successful, False otherwise.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            if amount > self._balance:
                raise ValueError("Insufficient funds")
                
            self._balance -= amount
            self.transactions.append(f"Withdrawal: ${amount:.2f}")
            return True
            
        except (ValueError, TypeError) as e:
            self.transactions.append(f"Failed withdrawal: {str(e)}")
            return False
    
    @property
    def balance(self) -> float:
        """Get current balance"""
        return self._balance
    
    def statement(self) -> str:
        """Generate account statement"""
        statement = f"\nAccount Statement for {self.holder_name}"
        statement += f"\nAccount Number: {self.account_number}"
        statement += f"\nCurrent Balance: ${self.balance:.2f}"
        statement += "\n\nTransaction History:"
        for transaction in self.transactions:
            statement += f"\n- {transaction}"
        return statement

if __name__ == "__main__":
    try:
        # Create new account
        name = input("Enter account holder name: ").strip()
        acc_num = input("Enter account number: ").strip()
        initial = float(input("Enter initial deposit amount: $").strip())
        
        account = BankAccount(acc_num, name, initial)
        print("\nAccount created successfully!")
        
        # Transaction loop
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. View Statement")
            print("5. Exit")
            
            choice = input("\nEnter choice (1-5): ").strip()
            
            if choice == "1":
                amount = float(input("Enter deposit amount: $").strip())
                if account.deposit(amount):
                    print("Deposit successful!")
                else:
                    print("Deposit failed!")
                    
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: $").strip())
                if account.withdraw(amount):
                    print("Withdrawal successful!")
                else:
                    print("Withdrawal failed!")
                    
            elif choice == "3":
                print(f"\nCurrent balance: ${account.balance:.2f}")
                
            elif choice == "4":
                print(account.statement())
                
            elif choice == "5":
                print("\nThank you for using our banking system!")
                break
                
            else:
                print("Invalid choice! Please try again.")
                
    except ValueError as e:
        print(f"\nError: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")