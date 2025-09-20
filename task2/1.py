import json 
import csv 
import glob
import typer
import os
from concurrent.futures import ThreadPoolExecutor
from rich.progress import Progress

app=typer.Typer()

def load_json(file):
    with
@app.command()
def main(inp:str,fields:str,output):
    files=glob.glob(f"{input}")
if __name__=="__main__":
    app()
