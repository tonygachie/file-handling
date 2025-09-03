def file_read_write():
    # Open the original file for reading
    with open("input.pdf", "r") as f:
        contents = f.read()

    # Modify the contents (example: convert text to uppercase)
    modified = contents.upper()

    # Write the modified content to a new file
    with open("output.txt", "w") as f:
        f.write(modified)

    print("✅ File read and modified version saved as 'output.txt'.")


# Run the function
file_read_write()



