import sys
import os

import openai
from openai import OpenAI

import typer


client = OpenAI()
app = typer.Typer()


@app.command()
def pipe(
    model: str = os.getenv("PAI_MODEL", "gpt-4o-mini"),
    api_key: str | None = os.getenv("OPENAI_API_KEY"),
):
    """Pipe your prompt to an OpenAI model and receive the response.

    Args:
        model (str): OpenAI model to use
        api_key (str): OpenAI API key (or set OPENAI_API_KEY)
    """
    if not api_key:
        print("OpenAI API key must be provided via --api-key or OPENAI_API_KEY env var")
        return

    prompt = None
    try:
        prompt = sys.stdin.read()
    except KeyboardInterrupt:
        return

    if not prompt:
        return
    try:
        response = client.responses.create(
            model=model,
            input=prompt,
        )
        print(response.output_text)
    except openai.APIError as e:
      #Handle API error here, e.g. retry or log
      print(f"OpenAI API returned an API Error: {e}")
      pass

if __name__ == "__main__":
    app()
