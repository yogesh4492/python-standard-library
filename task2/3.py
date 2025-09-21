import json
import csv
import glob
import typer
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import Progress

app = typer.Typer()

def load_json(file):
    with open(file, 'r', encoding="utf-8") as j:
        return json.load(j)

def process_file(file, field):
    rows = []
    segment = load_json(file)

    if list(segment.keys())[0] == 'documentId':
        for seg in segment['segments']:
            row = {k: seg[k] for k in seg if k in field}
            row['audioId'] = segment['audioId']
            row['audioFileNamePath'] = segment['audioFileNamePath']
            rows.append(row)
    else:
        for seg in segment['value']['segments']:
            row = {k: seg[k] for k in seg if k in field}
            row['content'] = seg['transcriptionData'].get('content')
            row['audioId'] = "None"
            row['audioFileNamePath'] = "None"
            rows.append(row)

    return rows

@app.command()
def up(input: str, fields: str, output: str):
    files = glob.glob(f"{input}/**/*.json", recursive=True)
    field = fields.split(",")

    with open(output, "w", newline="", encoding="utf-8") as c:
        csw = csv.DictWriter(c, fieldnames=field)
        csw.writeheader()

        with Progress() as p:
            task = p.add_task("Processing...", total=len(files))

            with ThreadPoolExecutor(max_workers=8) as executor:
                futures = {executor.submit(process_file, f, field): f for f in files}
                for future in as_completed(futures):
                    rows = future.result()
                    csw.writerows(rows)
                    p.update(task, advance=1)

if __name__ == "__main__":
    app()
