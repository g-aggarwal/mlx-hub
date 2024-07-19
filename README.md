Sure, here's the updated README.md with the detailed information about the commands included in the interactive mode:

### README.md

```markdown
<h1 align="center">MLX Hub</h1>

<p align="center">
    Framework: Python<br>
    Platform: macOS<br>
    Hardware: Apple Silicon<br>
</p>

MLX-Hub is a tool for downloading and managing [MLX](https://github.com/ml-explore/mlx) models from [Hugging Face Hub](https://huggingface.co) on [Apple Silicon Devices](https://support.apple.com/en-us/116943). 
It provides a command line interface (CLI) and a Python library to make it easy to search, download, and manage models without leaving your development environment. 
The built-in CLI tool called `mlx-hub-cli` accepts command line arguments and can also run in [Interactive Mode](#interactive-mode), directly from the terminal.

## Features

- [Scan](#scan) for MLX Models on your device
- [Search](#search) for MLX Models from Hugging Face Hub 
- [Suggest](#suggest) MLX models to download
- [Download](#download) MLX models by repository ID
- [Delete](#delete) MLX models as needed
- An [Interactive Mode](#interactive-mode) to run the tool like an application 

## Installation

You can install MLX-Hub using pip. To install the CLI and Python library, run:

```bash
pip install mlx-hub
```

## Command line arguments

```bash
> mlx-hub-cli --help 

options:
  -h, --help          Show this help message
  --start             Start Interactive Mode
  --scan              Scan for downloaded MLX models
  --search phrase     Search for MLX models using a search phrase
  --suggest           Suggest MLX models to download
  --download repo_id  Download a specific model
  --delete repo_id    Delete a specific model
```

## Interactive Mode

MLX-Hub provides an interactive mode that allows you to execute various commands in a user-friendly environment.

To start the interactive mode, use the following command:

```bash
mlx-hub-cli --start
```

In interactive mode, you will be prompted to enter commands. The available commands are:

- `help`: Show the help message with available commands.
- `scan`: Scan for downloaded MLX models.
- `suggest`: Suggest MLX models to download.
- `search <term>`: Search for MLX models using a search term.
- `download <model_id>`: Download a specific model.
- `delete <model_id>`: Delete a specific model.
- `exit`: Exit the interactive mode.

To exit the interactive mode, simply type `exit` and press Enter:

```bash
Enter Action > exit
Goodbye!
```

### Example

```bash
> mlx-hub-cli --start    

Starting interactive mode.

Available Actions:
    scan                  Scan for downloaded MLX models
    search     phrase     Search for MLX models using a search phrase
    suggest               Suggest MLX models to download
    download   repo_id    Download a specific model
    delete     repo_id    Delete a specific model
    exit                  Exit Interactive Mode
    help                  Show this help message

Enter Action > scan

1 downloaded models: 
mlx-community/TinyDolphin-2.8-1.1b-4bit-mlx

Enter Action > exit

Goodbye!
```

## Actions

### Scan

The `scan` action scans the Hugging Face cache directory and lists all the MLX models that are currently downloaded on your device.

### Search

The `search` action searches for MLX models on the Hugging Face Hub using a specified search term.

Example:

```bash
mlx-hub-cli --search bert
```

### Suggest

The `suggest` action suggests MLX models to download. It reads from a predefined list of suggested models.

### Download

The `download` action downloads a specific MLX model by its repository ID.

Example:

```bash
mlx-hub-cli --download mlx-community/bert-base-uncased-mlx
```

### Delete

The `delete` action deletes a specific MLX model by its repository ID.

Example:

```bash
mlx-hub-cli --delete mlx-community/bert-base-uncased-mlx
```

