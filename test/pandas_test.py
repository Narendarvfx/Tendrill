# import time
#
# import api
#
# s = time.time()
# all_shots_Data = api.allShotsData()
#
# for data in all_shots_Data:
#     print(data['name'])
# e = time.time()
# print(e-s)
#
# import pandas as pd
#
# ps = time.time()
# api_data = api.allShotsData()
# df = pd.json_normalize(api_data)
# print(df)
# for ind in df.index:
#     print(df['sequence.name'][ind])
# pe = time.time()
# print(pe-ps)
import subprocess
import os
import glob
# path =  glob.glob('J:/out/*.exr')[0]
# print (path)
# a = 'J:/KIS/BOO_GKB/BOO_GKB_0080_fg01_v002/paint/denoise'
# os.makedirs(a)
# a = os.environ.get('NUKE_PATH', 'notset')
nuke_ver = r"C:\Program files\Nuke13.0v1\Nuke13.0.exe"
# os.system (r'C:\KIS\BOO_GKB\BOO_GKB_0080_fg01_v002\paint\scripts\nuke\\')
import subprocess
subprocess.Popen(r'explorer /select,"C:\KIS\BOO_GKB\BOO_GKB_0080_fg01_v002\paint\scripts\nuke\"')