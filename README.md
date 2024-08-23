<h1 align="center">MLX Hub</h1>

MLX-Hub is a command line tool for managing [MLX](https://opensource.apple.com/projects/mlx/) AI models  on macOS. 

Search, scan and download [MLX models](https://huggingface.co/models?library=mlx&sort=downloads) from Hugging Face, right from your terminal. 

### What is MLX?

[MLX](https://github.com/ml-explore/mlx) is a model training and serving framework for Apple silicon, made by [Machine Learning Research](https://machinelearning.apple.com/) at Apple.

## Features

- [Scan](#scan) for downloaded Models in your local Hugging Face cache.
- [Search](#search) for MLX Models from Hugging Face Hub.
- [Suggest](#suggest) MLX models to download.
- [Download](#download) MLX models by model ID.
- [Delete](#delete) MLX models as needed.
- [Interactive Mode](#interactive-mode) for an app like interface.

## Installation

Install [`mlx-hub`](https://pypi.org/project/mlx-hub/)  from PyPI using pip:

```bash
pip install mlx-hub
```

## Components

- `mlx-hub-cli` : CLI Tool

- `mlx_hub`     : Python Module


### Hugging Face: User Access Token

MLX-Hub uses [huggingface_hub](https://github.com/huggingface/huggingface_hub) to interact with MLX models on Hugging Face.
Please create and add an access token from Hugging Face to huggingface_hub.

Hugging Face Hub documentation:
> https://huggingface.co/docs/hub/security-tokens

To create an access token, go to you Hugging Face settings:
> https://huggingface.co/settings/tokens

To add the access token to `huggingface_hub`:
> huggingface-cli login

## Quick start

### Command line arguments

MLX-Hub CLI accepts the following command line argument:

```bash
usage: mlx-hub-cli [-h] [--start] [--scan] [--search phrase] [--suggest] [--download model_id] [--delete model_id]

MLX-Hub CLI

options:
  -h, --help           show this help message and exit
  --start              Start Interactive Mode
  --scan               Scan for downloaded models in the Hugging Face cache
  --search phrase      Search for MLX models using a search phrase
  --suggest            Suggest MLX models to download
  --download model_id  Download a specific model
  --delete model_id    Delete a specific model
```

### Interactive Mode

Interactive mode allows you to execute various [Action](#Actions) in a user-friendly environment.

To start the interactive mode, use the `start` action:

```bash
mlx-hub-cli --start
```

```bash
Starting interactive mode.

Available Actions:
    scan                  Scan for downloaded models in the Hugging Face cache
    search     phrase     Search for MLX models using a search phrase
    suggest               Suggest MLX models to download
    download   model_id   Download a specific model
    delete     model_id   Delete a specific model
    exit                  Exit Interactive Mode
    help                  Show this help message

Enter Action > scan

1 downloaded models: 
mlx-community/TinyDolphin-2.8-1.1b-4bit-mlx

Enter Action > exit

Goodbye!
```

In interactive mode, the following actions are available:

- `help`: Show the help message with available actions.
- `scan`: Scan for downloaded MLX models.
- `suggest`: Suggest MLX models to download.
- `search <phrase>`: Search for MLX models using a search phrase.
- `download <model_id>`: Download a specific model.
- `delete <model_id>`: Delete a specific model.
- `exit`: Exit the interactive mode.

To exit the interactive mode, use the `exit` action:

```bash
Enter Action > exit

Goodbye!
```

## Actions

### Scan

The `scan` action scans the Hugging Face cache directory and lists all the MLX models that are currently downloaded on your device.

Example:

```bash
mlx-hub-cli --search bert
```

### Search

The `search` action searches for MLX models on the Hugging Face Hub using a specified search phrase. 
The search phrase should be substrings that will be contained in the model id of the model.

Example:

```bash
> mlx-hub-cli --search bert

3 models found:
mlx-community/bert-base-uncased-mlx
mlx-community/bert-large-uncased-mlx
mlx-community/bert-base-multilingual-uncased
```

Use quotes around the search phrase if it contains multiple substrings

```bash
 mlx-hub-cli --search "whisper v2"

3 models found:
mlx-community/whisper-large-v2-mlx
mlx-community/whisper-large-v2-mlx-8bit
mlx-community/whisper-large-v2-mlx-4bit
```

In Interactive Mode, you don't need the quotes

```bash
 mlx-hub-cli --start              

Starting interactive mode.

Available Actions:
    scan                  Scan for downloaded models in the Hugging Face cache
    search     phrase     Search for MLX models using a search phrase
    suggest               Suggest MLX models to download
    download   model_id   Download a specific model
    delete     model_id   Delete a specific model
    exit                  Exit Interactive Mode
    help                  Show this help message

Enter Action > search whisper v2

3 models found:
mlx-community/whisper-large-v2-mlx
mlx-community/whisper-large-v2-mlx-8bit
mlx-community/whisper-large-v2-mlx-4bit
```

### Suggest

The `suggest` action suggests MLX models to download. It reads from a predefined list of suggested models.

### Download

The `download` action downloads a specific MLX model by its model ID.

Example:

```bash
mlx-hub-cli --download mlx-community/bert-base-uncased-mlx
```

### Delete

The `delete` action deletes a specific MLX model by its model ID.

Example:

```bash
mlx-hub-cli --delete mlx-community/bert-base-uncased-mlx
```

### Acknowledgements
Thanks to:
- Apple's machine learning research team @ml-explore for [MLX](https://github.com/ml-explore/mlx) 
- The Hugging Face team @huggingface for [huggingface_hub](https://github.com/huggingface/huggingface_hub)
- The [MLX Community](https://huggingface.co/mlx-community)
