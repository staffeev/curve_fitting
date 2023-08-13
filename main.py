from pandas import read_excel
from scipy.optimize import curve_fit
import numpy as np
from numpy import *
import timeit
import time
import multiprocessing as mp
from objective import FUNCTIONS

if __name__ == "__main__":
    dataframe = read_excel("points.xls", dtype=np.float64)
    x, y = dataframe["X"], dataframe["Y"]
    pool = mp.Pool(mp.cpu_count())
    start = time.time()
    results = [pool.apply_async(curve_fit, args=(f, x, y)) for f in FUNCTIONS]
    pool.close()
    print(time.time() - start)
    print(len(results))