import json 
import csv 
import glob
import typer
import os
from concurrent.futures import ThreadPoolExecutor,as_completed
from rich.progress import Progress

app=typer.Typer()

def load_json(file):
    with open(file,'r',encoding="utf-8") as j:
        # data=json.load(j)
        # for i in data:
        #     print(i)
        return json.load(j)
        

# @app.command()
def main(file,field):
    # files=glob.glob(f"{inp}/**/*.json",recursive=True)
    # print(files)
    # print(len(files))
    # field=fields.split(",")
    print(file)
    rows=[]
    segment=load_json(file)
    # print(list(segment.keys())[0])
    if list(segment.keys())[0]=='documentId':
        # print(segment['segments'][0]['segmentId'])
        for j in segment['segments']:
            row={k:j[k] for k in j if k in field}
            # row1={k:j[k] for k in j if k not in field}
            row['audioId']=segment['audioId']
            row['audioFileNamePath']=segment['audioFileNamePath']
            rows.append(row)
            
    else:
        for j in segment['value']['segments']:
            row={k:j[k] for k in j if k in field}
            row['content']=j['transcriptionData'].get('content')
            row['audioId']="None"
            row['audioFileNamePath']='None'
            rows.append(row)
            # row={k:j[k] for k in j if k in field}
            # # row1={k:j[k] for k in j if k not in field}
            # row['audioId']=segment['audioId']
            # row['audioFileNamePath']=segment['audioFileNamePath']
            # csw.writerow(row)
    return rows    
        # print("Not Cut")
@app.command()
def up(input,fields,output):
    files=glob.glob(f"{input}/**/*.json",recursive=True)
    # print(files)
    # print(len(files))

    field=fields.split(",")
    with open(output,"w",newline="") as c:
        csw=csv.DictWriter(c,fieldnames=field)
        csw.writeheader()
    
        with Progress() as p:
            tab=p.add_task("Proceesing...",total=len(files))
            with ThreadPoolExecutor(max_workers=8) as e:
                future= {e.submit(main,f,field):f for f in files}
                for i in as_completed(future):
                 rows=i.result()
                 csw.writerows(rows)
                 p.update(tab,advance=1)
            
            
    

if __name__=="__main__":
    app()
