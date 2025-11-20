import json
import typer
import glob
import os
import re
import csv
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import Progress


def read_json(file):
    with open(file, 'r', encoding='utf-8') as jr:
        return json.load(jr)


def read_string(obj):
    """
    Recursively prints or handles strings in nested JSON objects
    """
    if isinstance(obj, dict):
        return {k: read_string(v) for k, v in obj.items()}

    elif isinstance(obj, list):
        return [read_string(i) for i in obj]

    elif isinstance(obj, str):
        return obj  # return the string

    else:
        return obj   # number, bool, None


app = typer.Typer()


@app.command()
def run(input_folder: str = typer.Argument(..., help="Folder containing JSON files")):
    for i in glob.glob(f"{input_folder}/*.json", recursive=True):
        data = read_json(i)
        extracted = read_string(data)
        # print(f"\n----- {i} -----")
        # print(extracted)
        # time.sleep(1)


if __name__ == "__main__":
    app()
