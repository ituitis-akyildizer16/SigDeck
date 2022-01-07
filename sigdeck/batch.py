"""Batch operations over a release directory."""

from pathlib import Path


def collect_release_files(directory, skip=(".sig", ".pub", ".key")):
