import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib


def create_embedding(text_list):

    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "bge-m3",
            "input": text_list
        }
    )

    if r.status_code != 200:
        print("HTTP Error:", r.status_code)
        print(r.text)
        return []

    data = r.json()

    if "embeddings" not in data:
        print("No embeddings found!")
        print(data)
        return []

    return data["embeddings"]


jsons = os.listdir("newjsons")

my_dicts = []
chunk_id = 0

for json_file in jsons:

    with open(f"newjsons/{json_file}", "r", encoding="utf-8") as f:
        content = json.load(f)

    print(f"Creating Embeddings for {json_file}")

    texts = [c['text'] for c in content['chunks']]

    embeddings = create_embedding(texts)

    if len(embeddings) == 0:
        print(f"Skipping {json_file}")
        continue

    for i, chunk in enumerate(content['chunks']):

        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]

        chunk_id += 1

        my_dicts.append(chunk)
     
df = pd.DataFrame.from_records(my_dicts)
#print(df)
joblib.dump(df,'embeddings.joblib')
