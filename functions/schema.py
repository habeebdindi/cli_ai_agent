from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_write_to_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a file by providing the working driectory, file path and content to be written to the file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file whose content is to be shown, relative to the working directory. Must be provided."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file."
            )
        }
    )
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Shows the content of the file specified, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file whose content is to be shown, relative to the working directory. Must be provided."
            )
        },
        required=["file_path"]
    )
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the python script specified",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file whose content is to be shown, relative to the working directory. Must be provided."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="array element"
                ),
                description="A list of arguments to be passed to the file that's to be executed(file_path)"
            )
        },
        required=["file_path"]
    )
)


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_write_to_file,
        schema_get_file_content,
        schema_run_python_file
    ]
)
