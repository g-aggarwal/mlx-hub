from enum import Enum
from typing import List
from importlib.resources import files, as_file
from huggingface_hub import HfApi, scan_cache_dir, snapshot_download, CacheNotFound

SUGGESTED_MODELS_FILE = 'suggested_models.txt'
PACKAGE_PATH = 'mlx_hub'
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
    models = hf_api.list_models(
        search=search_term,
        library=SEARCH_LIBRARY,
        author=SEARCH_AUTHOR,
        sort=sort_by.value,
        full=SEARCH_FULL,
        limit=search_limit
    )
    return [model.id for model in models]


def suggest() -> List[str]:
    """Reads and returns suggested models from a file."""
    try:
        with files(PACKAGE_PATH).joinpath(SUGGESTED_MODELS_FILE).open() as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except (FileNotFoundError, IOError):
        print(f"An error occurred while reading the file at path {SUGGESTED_MODELS_FILE}.")
        return []


def scan() -> List[str]:
    """Scans the Hugging Face cache directory and returns a list of repositories."""
    try:
        hf_cache_info = scan_cache_dir()
        return [model.repo_id for model in hf_cache_info.repos]
    except CacheNotFound as e:
        print(f"An error occurred while scanning the cache: {e}")
        return []


def download(repo_id: str) -> bool:
    """Downloads a repository snapshot by its ID."""
    try:
        repo_path = snapshot_download(repo_id)
        return bool(repo_path)
    except Exception as e:
        print(f"An error occurred while downloading the repository {repo_id}: {e}")
        return False


def delete(repo_id: str) -> bool:
    """Deletes a repository by its ID."""
    hf_cache_info = scan_cache_dir()
    for repo in hf_cache_info.repos:
        if repo_id == repo.repo_id:
            try:
                for revision in sorted(repo.revisions, key=lambda revision: revision.commit_hash):
                    strategy = hf_cache_info.delete_revisions(revision.commit_hash)
                    strategy.execute()
                return True
            except Exception as e:
                print(f"An error occurred while deleting the repository {repo_id}: {e}")
                return False
    return False
