### A script I use to make inserting HTML code into Arduino faster - outputs a file that encases each line with (")
input_file_path = 'path/to/file'  # Replace with the path to your HTML file
output_file_path = 'path/to/destination'  # Replace with the desired output file path
def add_quotes(input_file_path,output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
            for line in input_file:
                # Enclosing each line in double quotation marks and writing to the output file
                modified_line = f'"{line.strip()}"\n'
                output_file.write(modified_line)
        print("HTML lines enclosed in quotation marks in the output file.")
    except FileNotFoundError:
        print("File not found or path is incorrect.")
    except Exception as e:
        print("An error occurred:", e)

def remove_quotes(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
            for line in input_file:
                # Removing leading and trailing quotes and writing to the output file
                modified_line = line.strip().strip('"') + '\n'
                output_file.write(modified_line)
        print("Quotes removed from each line in the output file.")
    except FileNotFoundError:
        print("File not found or path is incorrect.")
    except Exception as e:
        print("An error occurred:", e)


#remove_quotes(input_file_path, output_file_path)
add_quotes(input_file_path, output_file_path)
