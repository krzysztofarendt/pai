# pipe-pai
**pipe-pai** is a simple command-line tool that allows you to interact with OpenAI models through Unix pipes.
Use it like this: `... | pai` - hence the name "pipe-pie".

## Installation

Install via pipx (recommended):

```bash
pipx install pipe-pai-tool
```

Or with pip:

```bash
pip install pipe-pai-tool
```

Or locally:
```
git clone git@github.com:krzysztofarendt/pai.git
cd pai
pipx install .
```

Ensure your OpenAI API key is set in the environment:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Optionally, set a default model using the PAI_MODEL environment variable:

```bash
export PAI_MODEL="gpt-4"
```

## Usage

Pipe a prompt to `pai` and receive the model's response on stdout:

```bash
echo "Write a haiku about the sea" | pai
```

Alternatively, specify a different model or API key:

```bash
echo "Tell me a joke" | pai --model gpt-4 --api-key $OPENAI_API_KEY
```

## Chat mode

By default, `pai` runs in the pipe mode with no chat history.
You can enter an interactive multi-turn chat by:
```bash
pai --chat
> Write a poem about the moon

--------------------
<AI response displayed here>
```

To exit chat mode, send an empty prompt press ctrl+c or type `q`, `exit`, or `quit`.
