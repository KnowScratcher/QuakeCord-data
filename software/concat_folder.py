# concatenate multiple CSV files from a folder structure into a single CSV file
import pandas
import tqdm
import os
# df = pandas.read_csv("8-9.csv")
df = pandas.DataFrame()
folder = "10" # the folder containing the subfolders with CSV files (month #)
print(len(df))
for i in tqdm.tqdm(range(1,32)): # change to 32 for month containing 31 days & 31 for month containing 30 days
    for j in range(24):
        if not os.path.exists(f"{folder}/{i}/{j}.csv"):
            continue
        try:
            df = pandas.concat([df, pandas.read_csv(f"{folder}/{i}/{j}.csv").iloc[::10,:]], axis=0, ignore_index=True)
        except:
            continue
print(len(df))
df.to_csv("10m.csv", index=False)

