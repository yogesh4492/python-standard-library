# import json
# import csv
# import glob
# import typer
# from concurrent.futures import ThreadPoolExecutor,as_completed
# from rich.progress import Progress
# import time

# def load_json(file,field):
#     with open(file,'r') as j:
#         data=json.load(j)
#         rows=[]
#         # print(list(data.keys())[0])
#         # print(list(data.keys()))
#         if list(data.keys())[0]=='documentId':
#             for i in data['segments']:
#                 row={k:i[k] for k in i if k in field}
#                 rows.append(row)
#         else:
#             for i in data['value']['segments']:
#                 row={k:i[k] for k in i if k in field}
#                 rows.append(row)
#     return rows

            
# app=typer.Typer()
# @app.command()
# def main(input,fields,output):
#     field=fields.split(",")
#     files=glob.glob(f"{input}**/*.json",recursive=True)
#     with open(output,'w',newline='',encoding='utf-8') as c:
#         csw=csv.DictWriter(c,fieldnames=field)
#         csw.writeheader()
#         with Progress() as p:
#             task=p.add_task("Processing...",total=len(files))
#             with ThreadPoolExecutor(max_workers=8) as e:
#                 future={e.submit(load_json,f,field)for f in files}
#                 for i in as_completed(future):
#                     p.update(task,advance=1)
#                     res=i.result()
#                     csw.writerows(res)




# if __name__=="__main__":
#     app()































































import json
import csv
import glob
import typer
from concurrent.futures import ThreadPoolExecutor,as_completed
from rich.progress import Progress
import os


app=typer.Typer()
class Main:
    def __init__(self,input,fields,output):
        self.input=input
        self.output=output
        # self.fields=fields
        self.files=glob.glob(f"{input}**/*.json",recursive=True)
        self.field=fields.split(",")
        print(self.field)

    def load_json(self,file):
        with open(file,'r',newline="",encoding='utf-8') as j:
            data=json.load(j)
            res=self.process_data(data)
        return res


            
            
    def  process_data(self,data):

        rows=[]

        if list(data.keys())[0]=='documentId':
            for i in data['segments']:
                row={k:i[k] for k in i if k in self.field}
                row['audioId']=data['audioId']
                row['audioFileNamePath']=data['audioFileNamePath']
                # print(row)
                rows.append(row)
        # return row
                # csw.writerow(row)
        else:
            for i in data['value']['segments']:
                row={k:i[k] for k in i if k in self.field}
                row['content']=i['transcriptionData'].get('content')
                row['audioId']=''
                row['audioFileNamePath']=''
                rows.append(row)
        return rows
                   
                    
                    # row={k:i[k] for k in i if k in self.field}
                    # row['content']=i.get('content')
                    # print(row)




        # print(list(data.keys())[0])
        
    def run(self):

        with open(self.output,'w',encoding='utf-8') as cs:
            csw=csv.DictWriter(cs,fieldnames=self.field)
            csw.writeheader()
            with Progress() as p:
                tab=p.add_task("processing....",total=len(self.files))

                with ThreadPoolExecutor(max_workers=8) as e:
                    future={e.submit(self.load_json,f) for f in self.files}
                    for i in as_completed(future):
                        res=i.result()
                        p.update(tab,advance=1)
                        csw.writerows(res)





@app.command()
def main(input,field,output):
    obj=Main(input,field,output)
    obj.run()

if __name__=="__main__":
    app()