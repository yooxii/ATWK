import numpy as np
import pandas as pd

gap = 0.3

df = pd.read_csv(
    r"D:\Desktop\temp\Overview.csv",
    header=None,
    skiprows=2,
    usecols=[1, 4, 7],
)
df_pk = df.sort_values(by=4, ascending=True)
df_avg = df.sort_values(by=7, ascending=True)

tmp = df_pk if df_pk.iloc[0, 1] < df_avg.iloc[0, 2] else df_avg

res = []
num = 6
while num > 0:
    for i in range(len(tmp)):
        if num <= 0:
            break
        if res == []:
            res.append(tmp.iloc[i, 0])
            num -= 1
            continue
        flag = True
        for r in res:
            t = tmp.iloc[i, 0]
            if np.abs(np.log10(t) - np.log10(r)) < gap:
                flag = False
                break
        if flag:
            res.append(tmp.iloc[i, 0])
            num -= 1
    if num > 0:
        gap -= 0.1

print(res)
