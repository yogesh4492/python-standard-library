import json 
import csv 
import glob
import typer
import os
from concurrent.futures import ThreadPoolExecutor
from rich.progress import Progress

app=typer.Typer()

def load_json(file):
    with open(file,'r',encoding="utf-8") as j:
        return json.load(j)

# @app.command()
def main(file,field,output):
    # files=glob.glob(f"{inp}/**/*.json",recursive=True)
    # print(files)
    # print(len(files))
    # field=fields.split(",")
    print(file)
    with open(output,"w",newline="") as c:
        csw=csv.DictWriter(c,fieldnames=field)
        csw.writeheader()
        for j in file:
            segment=load_json(j)
            # print(list(segment.keys())[0])
            if list(segment.keys())[0]=='documentId':
                # print(segment['segments'][0]['segmentId'])
                for j in segment['segments']:
                    row={k:j[k] for k in j if k in field}
                    # row1={k:j[k] for k in j if k not in field}
                    row['audioId']=segment['audioId']
                    row['audioFileNamePath']=segment['audioFileNamePath']
                    csw.writerow(row)
                    
            else:
                for j in segment['value']['segments']:
                    row={k:j[k] for k in j if k in field}
                    row['content']=j['transcriptionData'].get('content')
                    row['audioId']="None"
                    row['audioFileNamePath']='None'
                    csw.writerow(row)
                    # row={k:j[k] for k in j if k in field}
                    # # row1={k:j[k] for k in j if k not in field}
                    # row['audioId']=segment['audioId']
                    # row['audioFileNamePath']=segment['audioFileNamePath']
                    # csw.writerow(row)
                
            # print("Not Cut")
@app.command()
def up(input,fields,output):
    files=glob.glob(f"{input}/**/*.json",recursive=True)
    # print(files)
    # print(len(files))
    field=fields.split(",")
    with Progress() as p:
        tab=p.add_task("Proceesing...",total=len(files))
        with ThreadPoolExecutor(max_workers=8) as e:
            e.submit(main,files,field,output),total=len(files)
            
            
            
    

if __name__=="__main__":
    app()
