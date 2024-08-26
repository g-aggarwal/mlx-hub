<h1 align="center">MLX Hub</h1>

MLX-Hub is an open-sourced command line tool for managing [MLX](https://opensource.apple.com/projects/mlx/) AI models on Macs with [Apple silicon](https://support.apple.com/en-us/116943). 

Search, download & manage [MLX models](https://huggingface.co/models?library=mlx&sort=downloads) from Hugging Face, right from your terminal.

The CLI accepts command line arguments and provides an app interface with `Interactive Mode`.

### What is MLX?

[MLX](https://github.com/ml-explore/mlx) is a model training and serving framework for Apple silicon, made by [Machine Learning Research](https://machinelearning.apple.com/) at Apple.

## Features

- [Scan](#scan) for downloaded Models in your local Hugging Face cache.
- [Search](#search) for MLX Models from Hugging Face Hub.
- [Suggest](#suggest) MLX models to download.
- [Download](#download) MLX models by model ID.
- [Delete](#delete) MLX models as needed.
- [Interactive Mode](#interactive-mode) for an better UX.

## Documentation
[MLX Hub - v1.0.0](https://gaurav-aggarwal.com/mlx-hub/)

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

## Acknowledgements
Thanks to:
- Apple's machine learning research team for [MLX](https://github.com/ml-explore/mlx) 
- The Hugging Face team for [huggingface_hub](https://github.com/huggingface/huggingface_hub)
- The [MLX Community](https://huggingface.co/mlx-community)
