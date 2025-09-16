import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        full_path_relative = os.path.join(working_directory, file_path)
        full_path_absolute = os.path.abspath(full_path_relative)
        file_check = os.path.isfile(full_path_absolute)

        if working_directory not in full_path_absolute:
            raise Exception(f'Cannot read "{file_path}" as it is outside the permitted working directory')
        if file_check is not True:
            raise Exception(f'File not found or is not a regular file: "{file_path}"')

        with open(full_path_absolute, "r") as f:
            file_content = f.read()
            if len(file_content) > MAX_CHARS:
                file_content = file_content[:MAX_CHARS]
        return file_content
    except Exception as e:
        print(f'Error: {e}')
