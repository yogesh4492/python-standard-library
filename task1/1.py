import json
import csv
import typer
import os
app=typer.Typer()

def load_json(file):
    with open(file,'r',encoding="utf-8") as j:
        data=json.load(j)
        segments=data['value']['segments']
    return segments
@app.command()
def process_file(input_file,fields_list:str,output_file):
    field=fields_list.split(",")
        
    row=load_json(input_file)
    with open(output_file,'w') as c:
        csw=csv.DictWriter(c,fieldnames=field)
        csw.writeheader()
        for i in row:
            row={k:i[k] for k in i if k in field}
            row['Duration']=i['end']-i['start']
            row['filename']=os.path.basename(input_file)
            csw.writerow(row)
            
if __name__=="__main__":
    app()
        
    
    