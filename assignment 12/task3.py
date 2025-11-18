import sys

def get_user_input(prompt):
    """Safely gets numerical input from the user."""
    while True:
        try:
            # Use float for all coefficients/limits to handle general cases
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except EOFError:
            print("\nInput cancelled. Exiting.")
            sys.exit(1)

def check_feasibility(xa, xb, A1, B1, M1, A2, B2, M2):
    """
    Checks if a given point (XA, XB) satisfies all non-negativity
    and resource constraints (Constraint 1 and Constraint 2).
    """
    if xa < 0 or xb < 0:
        return False

    # Constraint 1 Check (Milk: A1*XA + B1*XB <= M1)
    if (A1 * xa + B1 * xb) > (M1 + 1e-9): # Add tolerance for floating point math
        return False

    # Constraint 2 Check (Choco: A2*XA + B2*XB <= M2)
    if (A2 * xa + B2 * xb) > (M2 + 1e-9): # Add tolerance for floating point math
        return False

    return True

def solve_lp_corner_point_method():
    """
    Solves a 2-variable, 2-constraint Linear Programming problem
    by manually calculating and checking the corner points.
    """
    print("\n--- Manual 2-Variable Linear Optimization Solver ---")
    print("Maximize P = (Profit_A * X_A) + (Profit_B * X_B)")
    print("Subject to two <= constraints.")

    # --- 1. Get Objective Function (Profit) ---
    print("\n[Objective Function: P = P_A * X_A + P_B * X_B]")
    pa = get_user_input("Enter profit per unit of Chocolate A (P_A): ")
    pb = get_user_input("Enter profit per unit of Chocolate B (P_B): ")

    # --- 2. Get Constraint 1 (Milk in the case study) ---
    print("\n[Constraint 1: Milk Resource - A1*XA + B1*XB <= M1]")
    a1 = get_user_input("Coefficient for X_A in Constraint 1 (A1): ")
    b1 = get_user_input("Coefficient for X_B in Constraint 1 (B1): ")
    m1 = get_user_input("Maximum available resource M1: ")

    # --- 3. Get Constraint 2 (Choco in the case study) ---
    print("\n[Constraint 2: Choco Resource - A2*XA + B2*XB <= M2]")
    a2 = get_user_input("Coefficient for X_A in Constraint 2 (A2): ")
    b2 = get_user_input("Coefficient for X_B in Constraint 2 (B2): ")
    m2 = get_user_input("Maximum available resource M2: ")

    # List of candidate corner points to check
    candidate_points = [(0.0, 0.0)] # Start with the Origin

    # --- 4. Calculate Intercepts (Points where XA=0 or XB=0) ---

    # Intercepts on XA-axis (where XB = 0)
    if a1 != 0:
        candidate_points.append((m1 / a1, 0.0))
    if a2 != 0:
        candidate_points.append((m2 / a2, 0.0))

    # Intercepts on XB-axis (where XA = 0)
    if b1 != 0:
        candidate_points.append((0.0, m1 / b1))
    if b2 != 0:
        candidate_points.append((0.0, m2 / b2))

    # --- 5. Calculate Intersection of the Two Constraints ---

    # We use elimination/substitution to solve the system of linear equations:
    # A1*XA + B1*XB = M1
    # A2*XA + B2*XB = M2

    # Denominator (Determinant D): D = A1*B2 - A2*B1
    determinant = a1 * b2 - a2 * b1

    if abs(determinant) > 1e-9: # Check if lines are not parallel
        try:
            # Formula derived from substitution/elimination:
            xa_intersect = (m1 * b2 - m2 * b1) / determinant
            xb_intersect = (m2 * a1 - m1 * a2) / (-determinant) # Equivalent to (M1*A2 - M2*A1) / D

            # Let's use the simpler substitution after XA is found to avoid potential division by -D
            xb_intersect_check = (m1 - a1 * xa_intersect) / b1
            # We add the point to candidates list
            candidate_points.append((xa_intersect, xb_intersect_check))
        except ZeroDivisionError:
            print("\nWarning: Attempted to divide by zero when calculating the second variable. Skipping intersection point.")
        except Exception as e:
            print(f"\nWarning: An error occurred during intersection calculation: {e}. Skipping intersection point.")
    # If determinant is close to zero, lines are parallel or coincident, so no unique intersection is added.

    # --- 6. Check Feasibility and Maximize Profit ---
    max_profit = -1.0
    optimal_point = None
    feasible_points = []

    for xa, xb in candidate_points:
        if check_feasibility(xa, xb, a1, b1, m1, a2, b2, m2):
            profit = pa * xa + pb * xb
            feasible_points.append({
                'xa': xa,
                'xb': xb,
                'profit': profit
            })
            if profit > max_profit:
                max_profit = profit
                optimal_point = (xa, xb)

    # --- 7. Display Results ---
    print("\n==============================================")
    if optimal_point:
        opt_xa, opt_xb = optimal_point
        print("✅ Optimization Successful! (Maximum Profit Found)")
        print("==============================================")
        print(f"Profit Maximized: Rs {max_profit:.2f}")
        print(f"Optimal Units of Chocolate A (X_A): {opt_xa:.2f}")
        print(f"Optimal Units of Chocolate B (X_B): {opt_xb:.2f}")
        print("\n[Feasible Corner Points Evaluated]:")
        for p in feasible_points:
            print(f"  - XA={p['xa']:.2f}, XB={p['xb']:.2f}, Profit=Rs {p['profit']:.2f}")
    else:
        print("❌ Optimization Failed. No feasible solution found (perhaps due to negative intercepts or parallel lines).")
    print("==============================================")


if __name__ == "__main__":
    # To solve the case study from the image, enter these values:
    # P_A: 6, P_B: 5
    # C1 (Milk): A1: 1, B1: 1, M1: 5
    # C2 (Choco): A2: 3, B2: 2, M2: 12
    solve_lp_corner_point_method()