import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        wd_abs = os.path.abspath(working_directory)
        file_abs = os.path.abspath(os.path.join(wd_abs, file_path))

        if not file_abs.startswith(f'{wd_abs}{os.sep}'):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file_abs):
            return f'Error: File "{file_path}" not found.'

        cmd_and_args = ["python3", file_abs]
        cmd_and_args.extend(args)
        run_response = subprocess.run(
            cmd_and_args,
            capture_output=True,
            timeout=30,
            cwd=wd_abs,
            text=True
        )
        stdout_response = f'STDOUT: {run_response.stdout}'
        stderr_response = f'STDERR: {run_response.stderr}'
        exit_code_response = f'Process exited with code {run_response.returncode}'
        empty_out_response = f'No output produced.'

        if not run_response.stdout and not run_response.stderr:
            return empty_out_response
        if run_response.returncode != 0:
            return f'{stdout_response}\n{stderr_response}\n{exit_code_response}'
        return f'{stdout_response}\n{stderr_response}'

        
    except Exception as e:
        return f"Error: executing Python file: {e}"
