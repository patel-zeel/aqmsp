import os


def get_repo_root(file):
    current_dir = os.path.abspath(os.path.dirname(file))
    while True:
        if os.path.exists(os.path.join(current_dir, ".git")):
            return current_dir
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        if parent_dir == current_dir:
            raise ValueError("Could not find repo root")
        current_dir = parent_dir
