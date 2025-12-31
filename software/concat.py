# concatenate two CSV files into a single CSV file
import pandas
df = pandas.read_csv("all.csv") # file 1
df2 = pandas.read_csv("all2.csv") # file 2
print(len(df))

df = pandas.concat([df2, df], axis=0, ignore_index=True)
print(len(df))
df.to_csv("all3.csv", index=False)

