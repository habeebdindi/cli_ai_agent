import os

def write_file(working_directory, file_path, content):
    try:
        full_path_relative = os.path.join(working_directory, file_path)
        full_path_absolute = os.path.abspath(full_path_relative)

        if working_directory not in full_path_absolute:
            raise Exception(f'Cannot write to "{file_path}" as it is outside the permitted working directory')

        with open(full_path_absolute, "w") as f:
            f.write(content)
        print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

    except Exception as e:
        print(f'Error: {e}')
        
