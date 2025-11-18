import sys

def safe_read_file(filename):
    """
    Safely reads the content of a file using a context manager.

    Args:
        filename (str): The path to the file to read.

    Returns:
        str: The content of the file, or None if an error occurred.
    """
    print(f"\nAttempting to read file: '{filename}'...")
    file_content = None
    
    # Using 'with open(...) as f:' is the best practice.
    # It automatically handles closing the file (f.close()) even if errors occur.
    try:
        with open(filename, "r", encoding="utf-8") as f:
            file_content = f.read()
        print("✅ File successfully read.")
        
    except FileNotFoundError:
        print(f"❌ ERROR: File not found. The file '{filename}' does not exist.")
        file_content = None  # Explicitly set to None on error
        
    except PermissionError:
        print(f"❌ ERROR: Permission denied. Cannot access '{filename}'.")
        file_content = None
        
    except UnicodeDecodeError:
        print(f"❌ ERROR: Encoding issue. Could not decode '{filename}' using UTF-8. Try a different encoding.")
        file_content = None
        
    except Exception as e:
        # Catch any other unexpected I/O errors
        print(f"❌ An unexpected error occurred while reading the file: {e}")
        file_content = None
        
    return file_content

def main():
    """Handles user input and demonstrates the safe file reading function."""
    print("--- Safe File Content Reader ---")
    print("This tool attempts to read a file path provided by you.")

    while True:
        try:
            filename = input("\nEnter the path/name of the file to read (or type 'exit' to quit): ").strip()
            
            if filename.lower() == 'exit':
                print("Exiting.")
                break
                
            if not filename:
                continue

            data = safe_read_file(filename)
            
            if data is not None:
                # Only display the content if reading was successful
                print("\n--- FILE CONTENT START ---")
                print(data)
                print("--- FILE CONTENT END ---")

        except EOFError:
            print("\nInput cancelled. Exiting.")
            sys.exit(0)
        except Exception as e:
            # Catch errors in the main loop, such as unexpected I/O on input
            print(f"An unexpected application error occurred: {e}")
            break

if __name__ == "__main__":
    main()