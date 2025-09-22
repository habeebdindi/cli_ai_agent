# CLI AI Agent

A command-line AI agent powered by Google's Gemini AI that can interact with your local file system through secure function calling. The agent can analyze code, fix bugs, manage files, and execute Python scripts within a constrained working directory.

## Features

- **File System Operations**: List directories, read files, and write content
- **Code Execution**: Run Python scripts with command-line arguments
- **AI-Powered Analysis**: Leverage Gemini 2.0 Flash for intelligent code analysis and bug fixing
- **Security Constraints**: All operations are limited to a designated working directory
- **Verbose Mode**: Optional detailed logging of function calls and token usage

## Prerequisites

- Python 3.13+
- Google Gemini API key
- UV package manager (recommended) or pip

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd cli_ai_agent
```

2. Install dependencies using UV:
```bash
uv sync
```

Or with pip:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
# Create a .env file in the project root
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
```

## Usage

### Basic Usage
```bash
python main.py "your prompt here"
```

### Verbose Mode
```bash
python main.py "your prompt here" --verbose
```

### Example Commands

**Analyze a project:**
```bash
python main.py "Analyze the calculator project and tell me what it does"
```

**Fix a bug:**
```bash
python main.py "There's a bug in the calculator where division by zero isn't handled properly. Please fix it."
```

**Create new functionality:**
```bash
python main.py "Add a new function to calculate the factorial of a number"
```

## Available Functions

The AI agent has access to these functions within the working directory:

### `get_files_info`
Lists files and directories with their sizes.
- **Parameters**: `directory` (optional) - relative path from working directory

### `get_file_content`
Reads and displays file contents.
- **Parameters**: `file_path` (required) - relative path to file

### `write_file`
Creates or overwrites files with new content.
- **Parameters**: 
  - `file_path` (required) - relative path to file
  - `content` (required) - content to write

### `run_python_file`
Executes Python scripts with optional arguments.
- **Parameters**:
  - `file_path` (required) - relative path to Python file
  - `args` (optional) - array of command-line arguments

## Project Structure

```
cli_ai_agent/
├── main.py              # Main CLI application
├── config.py            # Configuration and system prompt
├── functions/           # Function implementations
│   ├── schema.py        # Function schemas for Gemini
│   ├── call_function.py # Function dispatcher
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
├── calculator/          # Example working directory
│   ├── main.py
│   ├── tests.py
│   └── pkg/
└── tests.py            # Function tests
```

## Security Features

- **Directory Constraints**: All file operations are restricted to the configured working directory
- **Path Validation**: Prevents directory traversal attacks
- **Safe Execution**: Python execution is limited to the working directory scope

## Configuration

### Working Directory
The working directory is hardcoded in `functions/call_function.py`:
```python
wd = "calculator"  # Change this to your desired working directory
```

### System Prompt
Modify the AI behavior by editing `SYSTEM_PROMPT` in `config.py`.

### API Settings
- **Model**: Uses `gemini-2.0-flash-001` by default
- **Max Iterations**: Limited to 20 function call loops to prevent infinite loops
- **Token Limits**: Configurable through `MAX_CHARS` in config.py

## Example Use Cases

1. **Code Review**: "Review the calculator code and suggest improvements"
2. **Bug Fixing**: "Fix any bugs you find in the calculator implementation"
3. **Testing**: "Create comprehensive tests for the calculator functions"
4. **Documentation**: "Add docstrings to all functions in the calculator"
5. **Refactoring**: "Refactor the calculator to use better error handling"

## Troubleshooting

### Common Issues

**API Key Error**: Ensure your `GEMINI_API_KEY` is set correctly in the `.env` file.

**Permission Errors**: Check that the working directory exists and is writable.

**Function Call Loops**: The agent stops after 20 iterations to prevent infinite loops.

### Verbose Mode
Use `--verbose` flag to see:
- Function calls with parameters
- Token usage statistics
- Detailed execution logs

## Dependencies

- `google-genai==1.12.1` - Google Gemini AI client
- `python-dotenv==1.1.0` - Environment variable management
- `grpcio==1.67.1` - gRPC communication
- `grpcio-status==1.67.1` - gRPC status handling

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Changelog

### v0.1.0
- Initial release with basic file system operations
- Gemini 2.0 Flash integration
- Security-constrained working directory
- Verbose logging support
