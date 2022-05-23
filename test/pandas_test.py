import time

import api

s = time.time()
all_shots_Data = api.allShotsData()

for data in all_shots_Data:
    print(data['name'])
e = time.time()
print(e-s)

import pandas as pd

ps = time.time()
api_data = api.allShotsData()
df = pd.json_normalize(api_data)
print(df)
for ind in df.index:
    print(df['sequence.name'][ind])
pe = time.time()
print(pe-ps)
