from subprocess import run, CalledProcessError
from mlx_lm import load, manage
from huggingface_hub import scan_cache_dir

FILE_PATH = 'models.txt'

def list_models():
    try:
        with open(FILE_PATH, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file at {FILE_PATH} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def scan_models():
    hf_cache_info = scan_cache_dir()
    for repo in sorted(hf_cache_info.repos, key=lambda repo: repo.repo_path):
        # model_name = repo.repo_id.split('/')[-1]
        print(repo.repo_id)

def download_model(model_name):
    model, tokenizer = load(model_name)

def delete_model(model_name):
    run(['mlx_lm.manage', '--delete', '--pattern', model_name], check=True)