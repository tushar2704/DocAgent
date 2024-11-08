import os
from typing import List, Optional
import hashlib
import json
from datetime import datetime

class FileHandler:
    """Handles file operations and caching"""
    
    def __init__(self, cache_dir: str = ".cache"):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def get_file_hash(self, file_obj) -> str:
        """
        Generates hash for file content
        
        Args:
            file_obj: File object
        Returns:
            str: File hash
        """
        hasher = hashlib.md5()
        for chunk in iter(lambda: file_obj.read(4096), b""):
            hasher.update(chunk)
        file_obj.seek(0)  # Reset file pointer
        return hasher.hexdigest()
    
    def cache_exists(self, file_hash: str) -> bool:
        """
        Checks if cache exists for file
        
        Args:
            file_hash: File hash
        Returns:
            bool: True if cache exists
        """
        cache_path = os.path.join(self.cache_dir, f"{file_hash}.json")
        return os.path.exists(cache_path)
    
    def save_to_cache(self, file_hash: str, data: dict):
        """
        Saves processed data to cache
        
        Args:
            file_hash: File hash
            data: Data to cache
        """
        cache_path = os.path.join(self.cache_dir, f"{file_hash}.json")
        with open(cache_path, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'data': data
            }, f)
    
    def load_from_cache(self, file_hash: str) -> Optional[dict]:
        """
        Loads data from cache
        
        Args:
            file_hash: File hash
        Returns:
            Optional[dict]: Cached data if exists
        """
        cache_path = os.path.join(self.cache_dir, f"{file_hash}.json")
        if os.path.exists(cache_path):
            with open(cache_path, 'r') as f:
                return json.load(f)
        return None