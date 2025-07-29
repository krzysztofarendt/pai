import sys
import os

import openai
from openai import OpenAI
import typer

from pai.spinner import Spinner


client = OpenAI()
app = typer.Typer()


def line_up(clear: bool = False):
    sys.stdout.write("\x1b[F")
    if clear:
        print("\r", end="", flush=True)


@app.command()
def pipe(
    model: str = os.getenv("PAI_MODEL", "gpt-4o-mini"),
    api_key: str | None = os.getenv("OPENAI_API_KEY"),
    chat: bool = False,
):
    """Pipe your prompt to an OpenAI model and receive the response.

    Args:
        model (str): OpenAI model to use
        api_key (str): OpenAI API key (or set OPENAI_API_KEY)
    """
    if not api_key:
        print("OpenAI API key must be provided via --api-key or OPENAI_API_KEY env var")
        return

    chatting = True
    prompt = ""
    this_prompt = ""

    if chat:
        prompt += """
        This will be a multi-turn chat. Each new prompt will be prepended with previous prompts and your answers.

        Prompt:
        """

    while chatting:
        if chat:
            print("> ", end="", flush=True)

        try:
            if chat:
                newline = sys.stdin.readline()
                if newline == "\n":
                    line_up(clear=True)
                else:
                    this_prompt += newline
                    continue
            else:
                this_prompt = sys.stdin.read()
        except KeyboardInterrupt:
            if chat:
                print("\nBye!")
            return

        exit_codes = ["", "q", "exit", "quit"]
        if not this_prompt or this_prompt.strip() in exit_codes:
            if chat:
                line_up(clear=True)
                print("\nBye!")
            return

        prompt += this_prompt

        response = None
        try:
            if chat:
                with Spinner():
                    response = client.responses.create(
                        model=model,
                        input=prompt,
                    )
            else:
                response = client.responses.create(
                    model=model,
                    input=prompt,
                )
            if chat:
                print("--------------------")
                this_prompt = ""
            print(response.output_text)
        except openai.APIError as e:
          #Handle API error here, e.g. retry or log
          print(f"OpenAI API returned an API Error: {e}")
          pass

        if chat:
            assert response is not None
            prompt += "Answer:\n" + response.output_text
            prompt += "Prompt:\n"
            print()
            continue
        else:
            chatting = False

if __name__ == "__main__":
    app()
