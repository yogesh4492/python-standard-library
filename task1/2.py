import json
import csv
import typer
import os
import glob
app=typer.Typer()

def load_json(file):
    with open(file,'r',encoding="utf-8") as j:
        data=json.load(j)
        # return list(data['value']['segments'])
        s=data['value']['segments']
    return s


@app.command()
def process_file(input_file,fields_list:str,output_file):
    field=fields_list.split(",")
    files=glob.glob(f"{input_file}/**/*.json",recursive=True)
    print(files)
    print(len(files))
    
    with open(output_file,'w',newline="") as c:
        csw=csv.DictWriter(c,fieldnames=field)
        csw.writeheader()
        for i in files:

            segments=load_json(i)

            for j in segments:
                row={k:j[k] for k in j if k in field}
                row['Duration']=j['end']-j['start']
                row['filename']=os.path.basename(i)
                csw.writerow(row)
                
if __name__=="__main__":
    app()
        
    
    