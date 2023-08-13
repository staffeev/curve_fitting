from pandas import read_excel
from scipy.optimize import curve_fit
import numpy as np
from numpy import *
import timeit
import time
import multiprocessing as mp
from matplotlib import pyplot
import objective


# def objective(x, a, b, c, d, e, f):
# 	return a + b / log(x) + c / (log(x) ** 2) + d / (log(x) ** 3) + e / (log(x) ** 4) + f / (log(x) ** 5)

if __name__ == "__main__":
    dataframe = read_excel("points.xls", dtype=np.float64)
    x, y = dataframe["X"], dataframe["Y"]
    pool = mp.Pool(mp.cpu_count())
    start = time.time()
    names = [i for i in dir(objective) if i.startswith("objective_")]
    results = [pool.apply_async(curve_fit, args=(eval(f"objective.{f}"), x, y)) for f in names]
    pool.close()
    print(time.time() - start)


    pyplot.scatter(x, y)
    # define a sequence of inputs between the smallest and largest known inputs
    x_line = np.arange(min(x), max(x), 1)
    # calculate the output for the range
    c = 0
    for x, i in zip(names, results):
        c += 1
        try:
            func = eval(f"objective.{x}")
            y_line = func(x_line, *i.get()[0])
            # create a line plot for the mapping function
            pyplot.plot(x_line, y_line, '--', color='red')
        except:
            pass
    pyplot.show()