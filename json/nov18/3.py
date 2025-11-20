import json
import csv
import typer
import os
import glob
from concurrent.futures import ThreadPoolExecutor,as_completed
from rich.progress import Progress

app=typer.Typer()
def read_json(file):
    with open(file,'r') as jr:
        return json.load(jr)
    


@app.command()
def main(input_folder:str=typer.Argument(...,help="Input Folder that contain original json file")):
    for i in glob.glob(f"{input_folder}/*.json",recursive=True):
            read=read_json(i)
            fields=set(['name'])
            field=['name']
            with open("ou.csv",'w') as cs:
                csw=csv.DictWriter(cs,fieldnames=list(fields))
                csw.writeheader()
                for i in read['records']:
                    if isinstance(i,dict):
                            for k,j in i.items():
                                fields.add(k)
                                if k=="name":
                                     row={}
                                     row['name']=i['name']
                                     csw.writerow(row)
                                     
                                    
        
                        
                          
                      
                     
            # csw=csv.DictWriter()
        

if __name__=="__main__":
    app()