# TGNPDCL Electricity Bill Generator
# Author: GPT-5 Assistant
# Description: AI-assisted electricity bill calculator

def ai_tariff_prediction(customer_type, units):
    """
    Simple AI-like decision logic for determining tariff slab.
    This can later be replaced with an ML model if data is available.
    """
    if customer_type.lower() == 'domestic':
        if units <= 100:
            return 1.5  # ₹1.50/unit
        elif units <= 200:
            return 2.5
        elif units <= 500:
            return 3.5
        else:
            return 5.0
    elif customer_type.lower() == 'commercial':
        if units <= 100:
            return 4.0
        elif units <= 300:
            return 5.5
        else:
            return 7.0
    elif customer_type.lower() == 'industrial':
        if units <= 500:
            return 6.5
        else:
            return 8.0
    else:
        print("⚠ Unknown customer type. Using default rate ₹5/unit.")
        return 5.0


def calculate_bill(pu, cu, customer_type):
    units = cu - pu
    if units < 0:
        raise ValueError("Current units must be greater than previous units.")

    # AI-based tariff prediction
    rate = ai_tariff_prediction(customer_type, units)

    # Charges
    EC = units * rate  # Energy Charges
    FC = 50 if customer_type.lower() == 'domestic' else 100  # Fixed Charges
    CC = 10  # Customer Charges (flat)
    ED = 0.05 * EC  # Electricity Duty 5%

    # Total Bill
    total = EC + FC + CC + ED

    # Output
    print("\n--- TGNPDCL Electricity Bill ---")
    print(f"Customer Type      : {customer_type.capitalize()}")
    print(f"Previous Reading   : {pu} units")
    print(f"Current Reading    : {cu} units")
    print(f"Units Consumed     : {units} units")
    print(f"Energy Charges(EC) : ₹{EC:.2f}")
    print(f"Fixed Charges(FC)  : ₹{FC:.2f}")
    print(f"Customer Charges(CC): ₹{CC:.2f}")
    print(f"Electricity Duty(ED): ₹{ED:.2f}")
    print("---------------------------------")
    print(f"Total Bill Amount  : ₹{total:.2f}")
    print("---------------------------------")

    return {
        "EC": EC,
        "FC": FC,
        "CC": CC,
        "ED": ED,
        "Total": total
    }


# --- Main Program ---
if __name__ == "__main__":
    print("Welcome to TGNPDCL Bill Generator\n")
    try:
        pu = float(input("Enter Previous Unit Reading (PU): "))
        cu = float(input("Enter Current Unit Reading (CU): "))
        customer_type = input("Enter Customer Type (Domestic/Commercial/Industrial): ").strip()

        calculate_bill(pu, cu, customer_type)

    except ValueError as e:
        print(f"Error: {e}")
