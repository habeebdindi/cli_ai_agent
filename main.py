import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT
from functions.schema import available_functions
from functions.call_function import call_function

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
verbose = False
messages = []

def main():
    model = 'gemini-2.0-flash-001'
    cli_args_len = len(sys.argv)
    cli_args = sys.argv

    if cli_args_len < 2:
        print("Please pass in prompt argument!")
        sys.exit(1)
    if cli_args_len > 2:
        option = cli_args[2]
        if option == "--verbose":
            global verbose
            verbose = True
            

    user_prompt = cli_args[1]
    messages.append(
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    )
    
    loop_counter = 1
    while loop_counter <= 20:
        try:
            response = client.models.generate_content(
                model=model,
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=SYSTEM_PROMPT
                )
            )
            funcs_called = response.function_calls

            if verbose:
                print(f"User prompt: {user_prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        except Exception as e:
            print(f"Error: {e}")

        if response.text:
            print(f"\nresponse: {response.text}")

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)
            
        if funcs_called:
            for function_call_part in funcs_called:
                try:
                    func_call_result = call_function(function_call_part, verbose)
                    messages.append(types.Content(role="user", parts=[types.Part(text=func_call_result.parts[0].function_response.response["result"])]))
                    if not func_call_result.parts[0].function_response.response:
                        raise Exception("Fatal: error in function exection")
                    if verbose:
                        print(f"-> {func_call_result.parts[0].function_response.response}")
                except Exception as e:
                    print(e)

        if "final analysis" in response.text:
            break
        loop_counter += 1


if __name__ == "__main__":
    main()
