# ...existing code...
def sum_even_odd_from_input():
    s = input("Enter integers separated by space or comma: ").replace(',', ' ')
    parts = [p for p in s.split() if p.strip()]
    nums = []
    for p in parts:
        try:
            nums.append(int(p))
        except ValueError:
            print(f"Skipping invalid token: {p!r}")
    even_sum = sum(x for x in nums if x % 2 == 0)
    odd_sum = sum(x for x in nums if x % 2 != 0)
    print(f"Even sum: {even_sum}")
    print(f"Odd sum: {odd_sum}")

if __name__ == "__main__":
    sum_even_odd_from_input()
# ...existing code...