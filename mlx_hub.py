from typing import List
from huggingface_hub import HfApi, scan_cache_dir, snapshot_download
from enum import Enum

from huggingface_hub.hf_api import ModelInfo

SUGGESTED_MODELS_FILE_PATH = 'suggested_models.txt'

SEARCH_AUTHOR = "mlx-community"
SEARCH_LIBRARY = 'mlx'
SEARCH_FULL = False
SEARCH_LIMIT = 25


class SortBy(Enum):
    LIKES = "likes"
    DOWNLOADS = "downloads"
    CREATED = "created"
    LAST_MODIFIED = "last_modified"


def search(search_term, search_limit=SEARCH_LIMIT, sort_by=SortBy.DOWNLOADS) -> List[str]:
    """Searches for model repositories using a string that contain complete or partial names for models on the Hub."""
    hf_api = HfApi()
    # List all models with the specified filter
    models = hf_api.list_models(
        search=search_term,
        library=SEARCH_LIBRARY,
        sort=sort_by.value,
        full=SEARCH_FULL,
        limit=search_limit
    )
    models_list = list(models)
    return [model.id for model in models_list]


def suggest():
    """Reads and returns suggested models from a file."""
    try:
        with open(SUGGESTED_MODELS_FILE_PATH, 'r') as file:
            lines = file.readlines()
            # Strip newline characters from each line
            lines = [line.strip() for line in lines]
        return lines
    except (FileNotFoundError, IOError):
        print(f"An error occurred while reading the file at path {SUGGESTED_MODELS_FILE_PATH}.")
    return []


def scan():
    """Scans the Hugging Face cache directory and returns a list of repositories."""
    hf_cache_info = scan_cache_dir()
    models_list = list(hf_cache_info.repos)
    return [model.repo_id for model in models_list]


def download(repo_id):
    """Downloads a repository snapshot by its ID."""
    try:
        repo_path = snapshot_download(repo_id)
        return True if repo_path else False
    except Exception as e:
        print(f"An error occurred while downloading the repository {repo_id}: {e}")
        return False


def delete(repo_id):
    """Deletes a repository by its ID."""
    hf_cache_info = scan_cache_dir()
    for repo in hf_cache_info.repos:
        if repo_id == repo.repo_id:
            try:
                hf_cache_info = scan_cache_dir()
                for revision in sorted(repo.revisions, key=lambda revision_hash: revision_hash.commit_hash):
                    strategy = hf_cache_info.delete_revisions(revision.commit_hash)
                    strategy.execute()
                return True
            except Exception as e:
                print(f"An error occurred while deleting the repository {repo_id}: {e}")
                return False
    return False
