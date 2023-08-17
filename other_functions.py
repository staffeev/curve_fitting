from pandas import read_excel
from scipy.optimize import curve_fit
import numpy as np
from csv import writer
import objective
import objective_square
import time
from inspect import signature


def get(func, x, y, fname):
    start = time.time()
    res = curve_fit(func, x, y, maxfev=10000)
    return fname, len(signature(func).parameters) - 1, time.time() - start


dataframe = read_excel("points.xls", dtype=np.float64)
x, y = dataframe["X"].to_numpy(), dataframe["Y"].to_numpy()
y_square = y ** 2
names = [i for i in dir(objective) if i.startswith("objective_")]
#names2 = [i for i in dir(objective_square) if i.startswith("objective_") and not i.endswith("_sqrt")]
res1 = [get(eval(f"objective.{f}"), x, y, f"objective.{f}") for f in names]
print(*sorted(res1, key=lambda x: x[2], reverse=True)[:10], sep='\n')
