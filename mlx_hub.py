from huggingface_hub import scan_cache_dir, snapshot_download, HfApi, ModelFilter
from collections import deque

SUGGESTED_MODELS_FILE_PATH = 'suggested_models.txt'
SEARCH_LIMIT = 50
SEARCH_LIBRARY = 'mlx'
SEARCH_TASK = "text-generation"
SEARCH_AUTHOR = "mlx-community"
SEARCH_FULL = False

def search(search_term):
    """Searches for model repositories using a string that contain complete or partial names for models on the Hub."""
    hf_api = HfApi()
    
    # List all models with a specific filter
    models = hf_api.list_models(
        search=search_term, 
        library=SEARCH_LIBRARY, 
        # limit=SEARCH_LIMIT,
        # task=SEARCH_TASK,
        full=SEARCH_FULL,
        author=SEARCH_AUTHOR
    )
    
    return list(models)

def suggest():
    """Reads and returns suggested models from a file."""
    try:
        with open(SUGGESTED_MODELS_FILE_PATH, 'r') as file:
            lines = file.readlines()
            # Strip newline characters from each line
            lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"The file at path {SUGGESTED_MODELS_FILE_PATH} was not found.")
    except IOError:
        print(f"An error occurred while reading the file at path {SUGGESTED_MODELS_FILE_PATH}.")
    return []

def scan():
    """Scans the Hugging Face cache directory and returns a list of repositories."""
    hf_cache_info = scan_cache_dir()
    return hf_cache_info.repos
        
def find(repo_id):
    """Finds and returns a repository by its ID."""
    hf_cache_info = scan_cache_dir()
    for repo in sorted(hf_cache_info.repos, key=lambda repo: repo.repo_path):
        if repo_id == repo.repo_id:
            return repo
    return None

def download(repo_id):
    """Downloads a repository snapshot by its ID."""
    try:
        repo_path = snapshot_download(repo_id)
        return repo_path is not None
    except Exception as e:
        print(f"An error occurred while downloading the repository {repo_id}: {e}")
        return False

def delete(repo_id):
    """Deletes a repository by its ID."""
    repo = find(repo_id)
    if repo is not None:
        try:
            hf_cache_info = scan_cache_dir()
            for revision in sorted(repo.revisions, key=lambda revision: revision.commit_hash):
                strategy = hf_cache_info.delete_revisions(revision.commit_hash)
                strategy.execute()
            return True
        except Exception as e:
            print(f"An error occurred while deleting the repository {repo_id}: {e}")
            return False
    return False