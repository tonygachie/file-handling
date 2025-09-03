def error_handling_lab():
    filename = input("Enter the filename to read: ")

    try:
        # Try reading with UTF-8 encoding
        with open(filename, "r", encoding="utf-8") as f:
            contents = f.read()
        print(" File read successfully!")
        
        print(contents[:200])  # Show only first 200 characters

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print(" Error: You don’t have permission to read this file.")
    except UnicodeDecodeError:
        print(" Error: Could not decode the file (wrong encoding). Try opening it with 'latin-1'.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")


# Run the function
error_handling_lab()