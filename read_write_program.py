# Ask the user for the input filename
input_filename = input("Enter the name of the file to read: ").strip()
    
try:
    # Try to open and read the file
    with open(input_filename, 'r') as infile:
        content = infile.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Ask for an output filename
        output_filename = input("Enter the name of the file to write to: ").strip()
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File has been read from '{input_filename}' and written to '{output_filename}'.")
    
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied while accessing the file '{input_filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


