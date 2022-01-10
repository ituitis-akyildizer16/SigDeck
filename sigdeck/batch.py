"""Batch operations over a release directory."""

from pathlib import Path


def collect_release_files(directory, skip=(".sig", ".pub", ".key")):
    files = []
    for p in sorted(Path(directory).iterdir()):
        if p.is_file() and p.suffix not in skip:
            files.append(p)
    return files


def sign_all(directory, seed, out_dir=None):
    from .sign import sign_file, detached_path
