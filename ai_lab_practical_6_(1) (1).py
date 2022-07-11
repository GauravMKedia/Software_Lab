golf_file = "data1.csv"

import pandas as pd
import numpy as np
data = pd.read_csv(golf_file)
arr = np.array(data)
print(data)

verdicts = {"total":0, "type":{}}

cols = arr.shape[1]
for i in arr[:,cols-1]:

  if(str(i) not in verdicts["type"].keys()):
    verdicts["type"][str(i)] = 0
  verdicts["type"][str(i)] += 1
  verdicts["total"] += 1

print(verdicts)
ls = []
features = list(data.columns)
verdictValues = arr[:,cols-1]
for i in range(cols-1):
  temp = {"data":{}}
  temp["feature"] = features[i].lower()

  for j in range(len(arr[:,i])):
    tempType = str(arr[:,i][j]).lower()
    if(tempType not in temp["data"].keys()):
      temp["data"][tempType] = {"count": 0 , "verdict":{}}
    temp["data"][tempType]["count"] += 1

    verdictValue = verdictValues[j]
    if(verdictValue not in temp["data"][tempType]["verdict"]):
      temp["data"][tempType]["verdict"][verdictValue] = 0
    temp["data"][tempType]["verdict"][verdictValue] += 1
  
  ls.append(temp)
print(ls)

def naiveBaye(verdict,param):
  res = verdicts["type"][verdict] / verdicts["total"]
  div = 1
  index = 0
  for i in param:
    res *= (ls[index]["data"][i]["verdict"][verdict]/verdicts["type"][verdict])
    div *= (ls[index]["data"][i]["count"] / verdicts["total"])
    index += 1
  print(verdict + ": ")
  print(round(res,4))
  return (res/div)

def bayesFunc(param = ["sunny","hot","normal","false"]):
  res = []
  for verd in verdicts["type"]:
    temp = naiveBaye(verd,param)
    res.append({verd:temp})
  return res

val = bayesFunc(["sunny","hot","normal","false"])
print(val)


