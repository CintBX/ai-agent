import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    client = genai.Client(api_key=api_key)
    messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]
    has_prompt = len(sys.argv) > 1
    has_verbose_flag = "--verbose" in sys.argv

    if has_prompt:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages
        )
        if has_verbose_flag:
            print(f"User prompt: {response.text}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            return
        print(response.text)
    else:
        print("Please provide a prompt.")
        sys.exit(1)


if __name__ == "__main__":
    main()
