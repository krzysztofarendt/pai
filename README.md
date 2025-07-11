# pipe-pai
pipe-pai is a simple command-line tool that allows you to interact with OpenAI models through Unix pipes.
Use it like this: `... | pai` - hence the name "pipe-pie".

## Installation

Install via pipx (recommended):

```bash
pipx install pipe-pai
```

Or with pip:

```bash
pip install pipe-pai
```

Ensure your OpenAI API key is set in the environment:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

## Usage

Pipe a prompt to `pai` and receive the model's response on stdout:

```bash
echo "Write a haiku about the sea" | pai
```

Specify a different model or API key:

```bash
echo "Tell me a joke" | pai --model gpt-4 --api-key $OPENAI_API_KEY
```
