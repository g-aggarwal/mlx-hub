# Copyright (c) 2024 Gaurav Aggarwal

from enum import Enum
from typing import List
from huggingface_hub import HfApi, get_token, scan_cache_dir, snapshot_download, CacheNotFound
from huggingface_hub.errors import LocalTokenNotFoundError
import mlx_hub.utils as utils

SUGGESTED_MODELS_FILE = 'suggested_models.txt'

SEARCH_LIBRARY = 'mlx'
SEARCH_FULL = False
SEARCH_LIMIT = 25


class SortBy(Enum):
    LIKES = "likes"
    DOWNLOADS = "downloads"
    CREATED = "created"
    LAST_MODIFIED = "last_modified"


def has_token() -> bool:
    """Checks if there is an active Hugging Face token."""
    try:
        return get_token() is not None
    except LocalTokenNotFoundError:
        return False


def search(search_phrase, search_limit=SEARCH_LIMIT, sort_by=SortBy.DOWNLOADS) -> List[str]:
    """Searches for models using a string that contain complete or partial names on the Hub."""
    hf_api = HfApi()
    models = hf_api.list_models(
        search=search_phrase,
        library=SEARCH_LIBRARY,
        sort=sort_by.value,
        full=SEARCH_FULL,
        limit=search_limit
    )
    return [model.id for model in models]


def suggest() -> List[str]:
    """Reads and returns suggested models from a file."""
    return utils.read_packaged_file(SUGGESTED_MODELS_FILE)


def scan() -> List[str]:
    """Scans the Hugging Face cache directory and returns a list of Models."""
    try:
        hf_cache_info = scan_cache_dir()
        return [model.repo_id for model in hf_cache_info.repos]
    except CacheNotFound:
        return []


def download(model_id: str) -> bool:
    """Downloads a model snapshot by its ID."""
    try:
        return bool(snapshot_download(model_id))
    except Exception as e:
        print(f"An error occurred while downloading the model {model_id}: {e}")
        return False


def delete(model_id: str) -> bool:
    """Deletes a model from the Hugging Face cache by its ID."""
    hf_cache_info = scan_cache_dir()
    for repo in hf_cache_info.repos:
        if model_id == repo.repo_id:
            try:
                for revision in sorted(repo.revisions, key=lambda rev: rev.commit_hash):
                    strategy = hf_cache_info.delete_revisions(revision.commit_hash)
                    strategy.execute()
                return True
            except Exception as e:
                print(f"An error occurred while deleting the model {model_id}: {e}")
                return False
    return False
