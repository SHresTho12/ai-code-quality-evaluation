import os

def create_files(file_prefix, num_files, directory_path='.'):
    for i in range(num_files):
        file_name = f"{file_prefix}_{i}.py"
        file_path = os.path.join(directory_path, file_name)
        try:
            # Create an empty file
            with open(file_path, 'w') as file:
                pass
            print(f"File '{file_name}' created successfully.")
        except Exception as e:
            print(f"Error creating file '{file_name}': {e}")

# Example: Create 126 files with names like 'generated_code_deepSeek_0.py', 'generated_code_deepSeek_1.py', etc.
file_prefix = 'generated_code_deepSeek'
num_files = 126

# Specify the directory where you want to create the files
# If not specified, files will be created in the current working directory
directory_path = 'DeepSeekCodes\Python\WithPrompt'

# Create the files
create_files(file_prefix, num_files, directory_path)
