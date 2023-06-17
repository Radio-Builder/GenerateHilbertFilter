import sys

# Prompt the user to enter the input file path and output file path
input_file_path = input("Enter the input file path: ")
output_file_path = input("Enter the output file path: ")

# Read the input text file
with open(input_file_path, 'r') as input_file:
    # Read the contents of the input file
    contents = input_file.readlines()



# Remove the newline from the last line, if present
if contents[-1].endswith('\n'):
    contents.pop()

print(contents)

# Process the contents and format them
formatted_contents = [line.rstrip() + ',\n' for line in contents]

# Remove the comma from the last line
formatted_contents[-1] = formatted_contents[-1].rstrip(',\n')

# Add the line "float filter[] = {" at the beginning
formatted_contents.insert(0, "float filter[] = {\n")

# Remove the last comma before the closing curly brace
formatted_contents[-1] = formatted_contents[-1].rstrip(',')

# Add the closing curly brace "}" at the end
formatted_contents.append("}\n")

# Write the formatted contents to the output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(formatted_contents)

print("File conversion completed.")



