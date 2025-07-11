import sys
import os
import argparse

import openai
from openai import OpenAI


client = OpenAI()


def main():
    parser = argparse.ArgumentParser(
        description="Pipe your prompt to an OpenAI model and receive the response."
    )
    parser.add_argument(
        "-m", "--model",
        help="OpenAI model to use",
        default=os.getenv("PAI_MODEL", "gpt-4o-mini")
    )
    parser.add_argument(
        "-k", "--api-key",
        help="OpenAI API key (or set OPENAI_API_KEY)",
        default=os.getenv("OPENAI_API_KEY")
    )
    args = parser.parse_args()


    if not args.api_key:
        parser.error("OpenAI API key must be provided via --api-key or OPENAI_API_KEY env var")

    prompt = None
    try:
        prompt = sys.stdin.read()
    except KeyboardInterrupt:
        return

    if not prompt:
        return
    try:
        response = client.responses.create(
            model=args.model,
            input=prompt,
        )
        print(response.output_text)
    except openai.APIError as e:
      #Handle API error here, e.g. retry or log
      print(f"OpenAI API returned an API Error: {e}")
      pass

if __name__ == "__main__":
    main()
