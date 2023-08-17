from pandas import read_excel
from scipy.optimize import curve_fit
import numpy as np
from numpy import *
import timeit
import time
import multiprocessing as mp
from matplotlib import pyplot
import objective
import objective_square


if __name__ == "__main__":
    dataframe = read_excel("points.xls", dtype=np.float64)
    x, y = dataframe["X"], dataframe["Y"]
    y_square = y ** 2
    pool = mp.Pool(mp.cpu_count())
    start = time.time()
    names = [i for i in dir(objective) if i.startswith("objective_")]
    results = [pool.apply_async(curve_fit, args=(eval(f"objective.{f}"), x, y)) for f in names]
    names2 = [i for i in dir(objective_square) if i.startswith("objective_") and not i.endswith("_sqrt")]
    results2 = [pool.apply_async(curve_fit, args=(eval(f"objective_square.{f}"), x, y_square)) for f in names2]
    pool.close()
    print(time.time() - start)


    pyplot.scatter(x, y)
    # define a sequence of inputs between the smallest and largest known inputs
    x_line = np.arange(min(x), max(x), 0.001)
    # calculate the output for the range
    c = 0
    for x, i in zip(names, results):
        func = eval(f"objective.{x}")
        y_line = func(x_line, *i.get()[0])
        pyplot.plot(x_line, y_line, '--', color='red', )
    for x, i in zip(names2, results2):
        func = eval(f"objective_square.{x}_sqrt")
        y_line = func(x_line, *i.get()[0])
        pyplot.plot(x_line, y_line, '--', color='red', )
    pyplot.show()