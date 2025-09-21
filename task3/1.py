import os
import csv
import json
from concurrent.futures import ThreadPoolExecutor,as_completed
import glob
from collections import defaultdict
import typer
from rich.progress import Progress
import time
app=typer.Typer()
def load_csv(file):
    # print(file)
    with open(file,'r') as c:
        # pass
        return list(csv.DictReader(c,skipinitialspace=True))
def load_json(file):
    with open(file,'r') as rj:
        data=json.load(rj)
        return data['value']['segments']
def json_dump(file,data):
    with open(file,'w') as j:
        json.dump(data,j,indent=4)

def main(csv,json,output):
    # print(csv)
    read=load_csv(csv)

    csf=defaultdict(dict)
    for i in read:
        csf[i['FilePath']][i['SegmentId']]=i['Updated_Start_Time']
    

        # fil=os.path.basename(csf)
        # print(fil)
        count=1
    for filepath,segments in csf.items():
        read_json=load_json(filepath)
        for i in read_json:
            if i['segmentId'] in segments:
                i['start']=segments[i['segmentId']]
                i['start']=float(i['start'])

    
        os.makedirs(output,exist_ok=True)
        file=os.path.join(output,os.path.basename(filepath))
            
        json_dump(file,read_json)
            # print(count)
    



@app.command()
def getdata(input,csvfile:str,output):
    files=glob.glob(f"{input}**/*.json",recursive=True)
    print(len(files))
    with Progress() as p:
        task=p.add_task("Processing... ",total=len(files))
        with ThreadPoolExecutor(max_workers=8) as e:
            futures={e.submit(main,csvfile,f,output) for f in files}
            for  i in as_completed(futures):
                p.update(task,advance=1)
                time.sleep(0.05)
if __name__=="__main__":
    app()

