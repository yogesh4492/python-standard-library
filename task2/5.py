# import json
# import csv
# import glob
# import typer
# from concurrent.futures import ThreadPoolExecutor,as_completed
# from rich.progress import Progress
# import os


# app=typer.Typer()
# class Main:
#     def __init__(self,input,fields,output):
#         self.input=input
#         self.output=output
#         # self.fields=fields
#         self.files=glob.glob(f"{input}**/*.json",recursive=True)
#         self.field=fields.split(",")
#         print(self.field)

#     def load_json(self,file):
#         with open(file,'r',newline="",encoding='utf-8') as j:
#             data=json.load(j)
#             # for i in data:
#             #     print(i)
#             self.process_data(data)
            
            
#     def  process_data(self,data):
#         with open(self.output,'w',encoding='utf-8') as cs:
#             csw=csv.DictWriter(cs,fieldnames=self.field)
#             csw.writeheader()
#             rows=[]

#             if list(data.keys())[0]=='documentId':
#                 for i in data['segments']:
#                     row={k:i[k] for k in i if k in self.field}
#                     row['audioId']=data['audioId']
#                     row['audioFileNamePath']=data['audioFileNamePath']
#                     # print(row)
#                     rows.append(row)
#             return row
#                     # csw.writerow(row)
#             else:
#                 for i in data['value']['segments']:
#                     row={k:i[k] for k in i if k in self.field}
#                     row['content']=i['transcriptionData'].get('content')
                    
                    
#                     # row={k:i[k] for k in i if k in self.field}
#                     # row['content']=i.get('content')
#                     # print(row)




#         # print(list(data.keys())[0])
        
#     def run(self):
#         with Progress() as p:
#             tab=p.add_task("processing....",total=len(self.files))

#             with ThreadPoolExecutor(max_workers=8) as e:
#                 future={e.submit(self.load_json(f)):f for f in self.files}
#                 for i in as_completed(future):
#                     # res=i.result()
#                     p.update(tab,advance=1)




# @app.command()
# def main(input,field,output):
#     obj=Main(input,field,output)
#     obj.run()

# if __name__=="__main__":
#     app()