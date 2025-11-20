import json
import typer
import glob
import os
import re
import csv
import time
from collection import *
from concurrent.futures import ThreadPoolExecutor,as_completed
from rich.progress import Progress

def read_json(file):
    with open(file,'r') as jr:
        return json.load(jr)

def dump_json(file):
    pass

def read_string(obj):
    if isinstance(obj,dict):
       return {k: read_string(v) for k,v in obj.items()}
    
    elif isinstance(obj,list):
        return [read_json(i) for i in obj]
    elif isinstance(obj,str):
        print("hello")
    else:
        print("hello")
        

app=typer.Typer()

@app.command()
def run(input_folder:str=typer.Argument(...,help="name of folder that contain json")):
    for i in glob.glob(f"{input_folder}/*json",recursive=True):
        read=read_json(i)
        print(read_string(read))
        # print(read)
        # time.sleep(9)

if __name__=="__main__":
    app()
    
