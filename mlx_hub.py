from huggingface_hub import scan_cache_dir, snapshot_download
from mlx_lm import load

SUGGESTED_MODELS_FILE_PATH = 'suggested_models.txt'

def suggest():
    lines = []
    try:
        with open(SUGGESTED_MODELS_FILE_PATH, 'r') as file:
            lines = file.readlines()
            # Strip newline characters from each line
            lines = [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"The file at path {SUGGESTED_MODELS_FILE_PATH} was not found.")
    except IOError:
        print(f"An error occurred while reading the file at path {SUGGESTED_MODELS_FILE_PATH}.")
    return lines

def scan():
    hf_cache_info = scan_cache_dir()
    return hf_cache_info.repos
        
def find(repo_id):
    hf_cache_info = scan_cache_dir()
    for repo in sorted(hf_cache_info.repos, key=lambda repo: repo.repo_path):
        if repo_id == repo.repo_id:
            return repo
    return None

def download(repo_id):
    repo_path = snapshot_download(repo_id)
    return repo_path is not None

def delete(repo_id):
    repo = find(repo_id)
    if repo is not None:
        hf_cache_info = scan_cache_dir()
        for revision in sorted(
            repo.revisions, key=lambda revision: revision.commit_hash
        ):
            strategy = hf_cache_info.delete_revisions(revision.commit_hash)
            strategy.execute()
            return True
    return False