# Function to read the first line of a text file
def read_first_line(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
    return first_line

# Function to modify the first line of a text file
def modify_first_line(file_path, new_first_line):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Modify the first line
    lines[0] = new_first_line + '\n'
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)


