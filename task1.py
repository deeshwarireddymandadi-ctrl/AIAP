# ...existing code...

import csv
import os

def calculate_statistics(filename: str) -> dict:
    """Read a CSV file and calculate mean, min, and max of the numeric values in the first column."""
    try:
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            values = [float(row[0]) for row in reader if row]  # Assuming numeric values are in the first column
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found.")
    except ValueError:
        raise ValueError("Non-numeric data found in the file.")
    
    if not values:
        raise ValueError("No data to calculate statistics.")
    
    return {
        'mean': sum(values) / len(values),
        'min': min(values),
        'max': max(values)
    }

if __name__ == "__main__":
    try:
        filename = input("Enter the CSV file path: ").strip()
        stats = calculate_statistics(filename)
        print(f"Mean: {stats['mean']}, Min: {stats['min']}, Max: {stats['max']}")
    except (FileNotFoundError, ValueError) as e:
        print(e)
# ...existing code...