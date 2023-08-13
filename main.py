from pandas import read_excel
from scipy.optimize import curve_fit
import numpy as np
from numpy import log
import timeit
import asyncio 


def objective(x, a, b, c, d, e, f):
	return a + b / log(x) + c / (log(x) ** 2) + d / (log(x) ** 3) + e / (log(x) ** 4) + f / (log(x) ** 5)


if __name__ == "__main__":
    dataframe = read_excel("points.xls", dtype=np.float64)
    x, y = dataframe["X"], dataframe["Y"]
    # popt, _ = curve_fit(objective, x, y)
    # print(popt)
    result = timeit.timeit(lambda: curve_fit(objective, x, y), number=1000)
    print(result)