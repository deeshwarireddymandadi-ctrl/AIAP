def discount(price, category):
    """Apply discount based on category and price."""
    discount_rates = {
        "student": {
            "threshold": 1000,
            "high_rate": 0.9,      # price > 1000: 10% discount
            "low_rate": 0.95       # price <= 1000: 5% discount
        },
        "regular": {
            "threshold": 2000,
            "high_rate": 0.85,     # price > 2000: 15% discount
            "low_rate": 1.0        # price <= 2000: no discount
        }
    } 
    rules = discount_rates.get(category, discount_rates["regular"])
    rate = rules["high_rate"] if price > rules["threshold"] else rules["low_rate"]
    return price * rate
def main():
    """Get user input and calculate discount."""
    print("=== Discount Calculator ===\n")
    try:
        price = float(input("Enter price ($): "))
        if price < 0:
            print("Error: Price cannot be negative.")
            return
        category = input("Enter category (student/regular): ").lower().strip()
        if category not in ["student", "regular"]:
            print("Error: Category must be 'student' or 'regular'.")
            return
        final_price = discount(price, category)
        savings = price - final_price
        print(f"\nOriginal Price: ${price:.2f}")
        print(f"Category: {category}")
        print(f"Discounted Price: ${final_price:.2f}")
        print(f"You saved: ${savings:.2f}")     
    except ValueError:
        print("Error: Please enter a valid number for price.")
if __name__ == "__main__":
    main()