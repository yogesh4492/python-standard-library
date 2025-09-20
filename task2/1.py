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

@app.command()
def main(inp:str,fields:str,output):
    files=glob.glob(f"{inp}/**/*.json",recursive=True)
    print(files)
    print(len(files))
    field=fields.split(",")
    with open(output,"w",newline="") as c:
        csw=csv.DictWriter(c,fieldnames=field)
        csw.writeheader()
        for i in files:
            segment=load_json(i)
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
            
  

if __name__=="__main__":
    app()
