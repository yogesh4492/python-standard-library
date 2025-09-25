import typer 
import json
import glob
from concurrent.futures import ThreadPoolExecutor,as_completed
import os
from rich.progress import Progress
app=typer.Typer()
from pydub import AudioSegment
class Main:
    def __init__(self,json,audio,output):
        self.json=json
        self.audio=audio
        self.output=output
        os.makedirs(output,exist_ok=True)
        
        self.files=glob.glob(f"{json}**/*.json",recursive=True)
        self.a_files=glob.glob(f"{audio}/**/*.wav",recursive=True)

    def load_json(self,file):
        with open(file,'r') as j:
            data=json.load(j)
            return data['batch03_20240722']['text_segments']
    def trim_audio(self,wav,start,end,f):
        pa=os.path.join(self.output,f"{f}_{start}_{end}.wav")
        new=wav[start:end]
        new.export(pa,format="wav")
        
        
    def Process_file(self,file):
        read=self.load_json(file)
        f=os.path.splitext(os.path.basename(file))[0]
        # print(self.a_files)
        # for i in self.a_files:
        #     if f in i:
                 # wav=AudioSegment.from_wav(i)
                # for j in read:
                #     start=j['start']*1000
                #     end=j['end']*1000
                #     self.trimmed_audio()
                
        a=[i  for i in self.a_files if f in i]
        wav=AudioSegment.from_wav(a[0])
        for i in read:
            
            start=i['start']*1000
            end=i['end']*1000
            self.trim_audio(wav,start,end,f)


               
    def run(self):
        with Progress() as p:
            task=p.add_task("Processing...",total=len(self.files))
            with ThreadPoolExecutor(max_workers=8) as e:
                future={e.submit(self.Process_file,f)for f in self.files}
                for i in as_completed(future):
                    p.update(task,advance=1)

@app.command()
def main(input_j,input_a,output):
    obj=Main(input_j,input_a,output)
    obj.run()

if __name__=="__main__":
    app()
