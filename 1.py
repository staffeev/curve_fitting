import multiprocessing as mp
import numpy as np
from numpy import log
# from time import time
import time
from pandas import read_excel
from scipy.optimize import curve_fit
from matplotlib import pyplot


def objective(x, a, b):
    return a+b*(x)


def objective2(x, a, b):
    return np.sqrt(a+b*(x))


if __name__ == "__main__":
    dataframe = read_excel("points.xls")
    x, y = dataframe["X"], dataframe["Y"]
    #x = x ** 2
    y = y ** 2
    
    #pool = mp.Pool(mp.cpu_count())
    #start = time.time()
    popt = curve_fit(objective, x, y)
    # ob = [objective_0, objective_1, objective_2, objective_3, objective_4, objective_5, objective_6, objective_7, objective_8, objective_9]
    #results = [pool.apply_async(curve_fit, args=(objective, x, y)) for _ in range(100000)]
    #pool.close()
    #print(time.time() - start)
    print(popt)

    #x = np.sqrt(x)
    y = np.sqrt(y)
    pyplot.scatter(x, y)
    # define a sequence of inputs between the smallest and largest known inputs
    x_line = np.arange(min(x), max(x), 0.001)
    y_line = objective2(x_line, *popt[0])
    # create a line plot for the mapping function
    pyplot.plot(x_line, y_line, '--', color='red')
    pyplot.show()