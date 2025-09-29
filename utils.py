import numpy as np
import pandas as pd
import os

gap = 0.3


def findmin(path, gap):
    if not os.path.exists(os.path.join(path, "Overview.csv")):
        return ""
    df = pd.read_csv(
        os.path.join(path, "Overview.csv"),
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
        if num > 0 and gap >= 0:
            gap -= 0.1
    ret = ""
    for r in res:
        ret += f"{r:.3f}\n"
    return ret


def checkTestPass(path):
    if not os.path.exists(os.path.join(path, "CriticalPoint.csv")):
        return False
    df = pd.read_csv(
        os.path.join(path, "CriticalPoint.csv"),
        header=None,
        usecols=[1, 4, 7],
    )
    if len(df) == 2:
        return True
    else:
        return False


def delete_csv(path):
    """删除该路径下所有的csv文件"""
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                os.remove(os.path.join(root, file))
