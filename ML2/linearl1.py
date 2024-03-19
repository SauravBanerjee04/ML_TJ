import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import matplotlib.pyplot as plt

df = pd.read_csv ('Default.csv')
print(df)

def get100(frame, diddefault):
    isdefault = frame['default'] == "Yes"
    if(not diddefault):
        isdefault = frame['default'] == "No"
    newframe = df[isdefault]
    return newframe.sample(n=100)

def get200(frame):
    return pd.concat([get100(frame,True),get100(frame,False)])

all = df

isstudent = df['student'] == "Yes"
students = df[isstudent]
students

notstudent = df['student'] == "No"
notstudents = df[notstudent]
notstudents

print(students)

get100(students,False)