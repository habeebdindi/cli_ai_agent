import os
from config import MAX_CHARS

def get_files_info(working_directory, directory="."):
    try:
        full_path_relative = os.path.join(working_directory, directory)
        full_path_absolute = os.path.abspath(full_path_relative)
        directory_check = os.path.isdir(full_path_absolute)
        
        if working_directory not in full_path_absolute:
            print(f"full abs path: {full_path_absolute}")
            raise Exception(f'Cannot list "{directory}" as it is outside the permitted working directory')
        if directory_check is not True:
            raise Exception(f'"{directory}" is not a directory')

        dir_content = os.listdir(full_path_absolute)
        if "__pycache__" in dir_content:
            dir_content.remove("__pycache__")

        print("Result for current directory:")

        all_content = ""
        for content in dir_content:
            try:
                full_abs_path = os.path.join(full_path_absolute, content)
                info = f'- {content}: file_size={os.path.getsize(full_abs_path)} bytes, is_dir={os.path.isdir(full_abs_path)}'
                #print(info)
                all_content += f"{info}\n"
            except Exception as e:
                print(f'Error: {e}')
        return all_content
    except Exception as e:
        print(f'Error: {e}')
