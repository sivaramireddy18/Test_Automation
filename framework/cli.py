"""Command-line entry point."""
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(prog="valgen")
    parser.add_argument("--version", action="version", version="0.1.0")
    parser.parse_args()
