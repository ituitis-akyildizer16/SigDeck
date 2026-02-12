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
    out = Path(out_dir or directory)
    out.mkdir(parents=True, exist_ok=True)
    signed = []
    for p in collect_release_files(directory):
        sig = sign_file(p, seed)
        dst = out / detached_path(p).name
        dst.write_bytes(sig)
        signed.append(dst)
    return signed

# draft note 876
