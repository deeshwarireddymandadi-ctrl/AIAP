import sys
import math

def get_user_input(prompt, default_value):
    """Safely gets float input from the user with a default."""
    while True:
        try:
            # Display default value in the prompt
            user_input = input(f"{prompt} (Default: {default_value}): ")
            if not user_input:
                return default_value
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except EOFError:
            print("\nInput cancelled. Exiting.")
            sys.exit(1)

def get_cubic_coeffs():
    """Asks user for the coefficients of the cubic function."""
    print("\n--- Enter Coefficients for f(x) = A*x^3 + B*x^2 + C*x + D ---")
    print("For the requested function f(x) = 2x^3 + 4x + 5, press Enter for all defaults.")

    # Using the specific function's coefficients as defaults (A=2, B=0, C=4, D=5)
    A = get_user_input("Enter Coefficient A (x^3 term): ", 2.0)
    B = get_user_input("Enter Coefficient B (x^2 term): ", 0.0)
    C = get_user_input("Enter Coefficient C (x term): ", 4.0)
    D = get_user_input("Enter Coefficient D (constant term): ", 5.0)

    return A, B, C, D

def solve_quadratic(a, b, c):
    """Solves a quadratic equation ax^2 + bx + c = 0 for its real roots."""
    # Discriminant: delta = b^2 - 4ac
    delta = b**2 - 4 * a * c

    if delta >= 0:
        # Real roots exist
        # Use math.sqrt since delta >= 0
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        # Return unique roots only
        return [root1] if abs(root1 - root2) < 1e-9 else [root1, root2]
    else:
        # No real roots (complex roots)
        return []

def analyze_critical_points(A, B, C, D):
    """
    Finds critical points using the first derivative and classifies them
    using the second derivative test.
    """
    # Critical points occur when f'(x) = 3Ax^2 + 2Bx + C = 0
    a_quad = 3 * A
    b_quad = 2 * B
    c_quad = C

    print(f"\n--- Analyzing f(x) = {A}x^3 + {B}x^2 + {C}x + {D} ---")
    print(f"[Step 1: First Derivative] f'(x) = {a_quad}x^2 + {b_quad}x + {c_quad}")

    # Handle the degenerate case where A is zero (not a cubic)
    if A == 0:
        print("\nNote: A=0. This is a Quadratic or Linear function. Cubic analysis is inappropriate.")
        return

    # Solve f'(x) = 0 for critical points
    critical_points = solve_quadratic(a_quad, b_quad, c_quad)

    if not critical_points:
        print("\n[Step 2: Critical Points (f'(x)=0)]")
        # If no real roots, the derivative is either always > 0 or always < 0.
        if a_quad > 0 and c_quad > 0: # Like 6x^2 + 4
            print(f"f'(x) has no real roots and is always positive (since {a_quad} > 0 and f'(0) = {c_quad} > 0).")
            print("Conclusion: The function is STRICTLY INCREASING and has NO local minimum or maximum.")
        else:
             print("No real critical points found. Function is strictly monotonic.")
        return

    print(f"\n[Step 2: Critical Points] Found {len(critical_points)} real critical point(s).")

    # Second Derivative Test: f''(x) = 6Ax + 2B
    print(f"[Step 3: Second Derivative Test] f''(x) = {6 * A}x + {2 * B}")

    results = []

    for x_c in critical_points:
        f_double_prime = (6 * A) * x_c + (2 * B)
        f_val = A * x_c**3 + B * x_c**2 + C * x_c + D

        type_of_point = ""

        # Using a small tolerance for comparison to zero
        if abs(f_double_prime) < 1e-9:
            type_of_point = "Inconclusive (Likely Inflection Point)"
        elif f_double_prime > 0:
            type_of_point = "LOCAL MINIMUM"
        else: # f_double_prime < 0
            type_of_point = "LOCAL MAXIMUM"

        results.append({
            'x': x_c,
            'f_x': f_val,
            'type': type_of_point
        })

    # --- FINAL RESULT CLASSIFICATION ---
    local_minimums = [r for r in results if r['type'] == 'LOCAL MINIMUM']

    print("\n--- FINAL CLASSIFICATION ---")
    if local_minimums:
        # Find the point with the lowest function value among all local minimums
        optimal_result = min(local_minimums, key=lambda r: r['f_x'])
        print(f"✅ The function has a local minimum at:")
        print(f"   X value: {optimal_result['x']:.4f}")
        print(f"   Minimum f(X) value: {optimal_result['f_x']:.4f}")
    else:
        print("Conclusion: No local minimum was found.")

    print("\n[All Critical Points Found]:")
    for r in results:
        print(f"  - X = {r['x']:.4f}, f(X) = {r['f_x']:.4f} -> {r['type']}")


if __name__ == "__main__":
    A, B, C, D = get_cubic_coeffs()

    # Run the analysis
    analyze_critical_points(A, B, C, D)

    # Note specifically for the user's fixed function
    if A == 2.0 and B == 0.0 and C == 4.0 and D == 5.0:
        print("\n--- Specific Note for f(x) = 2x^3 + 4x + 5 ---")
        print("As concluded by the general analysis, this specific function has a derivative (6x^2 + 4) that is always positive.")
        print("It is strictly increasing and therefore has NO local minimum value over the entire real number line.")