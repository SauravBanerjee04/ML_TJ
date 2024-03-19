import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats

def get100(frame, diddefault):
    isdefault = frame['default'] == "Yes"
    if(not diddefault):
        isdefault = frame['default'] == "No"
    newframe = frame[isdefault]
    return newframe.sample(n=100)

def get200(frame):
    return pd.concat([get100(frame,True),get100(frame,False)])