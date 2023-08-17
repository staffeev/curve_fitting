from pandas import read_excel
from scipy.optimize import curve_fit
import numpy as np
from numpy import *
import timeit
import time
import multiprocessing as mp
from matplotlib import pyplot
from sklearn.metrics import max_error
from inspect import signature
import objective
import objective_square
from tqdm import tqdm
from csv import writer


def metrics_calc(xdata, ydata, y_predicted, func):
    residuals = ydata - y_predicted
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((ydata - np.mean(ydata)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    n = len(xdata)
    k = len(signature(func).parameters) - 1
    adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - k - 1))
    std_derr = np.sqrt(np.sum((ydata - y_predicted) ** 2) / (n - k - 1))
    std_err = np.sqrt(1 - adj_r2) * std_derr
    max_err = max_error(ydata, y_predicted)
    f = np.var(ydata, ddof=1) / np.var(y_predicted, ddof=1)
    return r2, adj_r2, std_err, max_err, f


if __name__ == "__main__":
    dataframe = read_excel("points.xls", dtype=np.float64)
    x, y = dataframe["X"], dataframe["Y"]
    y_square = y ** 2
    pool = mp.Pool(mp.cpu_count())
    start = time.time()
    names = [i for i in dir(objective) if i.startswith("objective_")]
    results = [pool.apply_async(curve_fit, args=(eval(f"objective.{f}"), x, y), kwds={"maxfev": 10000}) for f in names]
    names2 = [i for i in dir(objective_square) if i.startswith("objective_") and not i.endswith("_sqrt")]
    results2 = [pool.apply_async(curve_fit, args=(eval(f"objective_square.{f}"), x, y_square), kwds={"maxfev": 10000}) for f in names2]

    functions = [eval(f"objective.{f}") for f in names] + [eval(f"objective_square.{f}_sqrt") for f in names2]
    results = [i.get()[0] for i in results] + [i.get()[0] for i in results2]
    metrics = [pool.apply_async(metrics_calc, args=(x, y, f(x, *popt), f)) for f, popt in zip(functions, results)]
    pool.close()

    res = [i.get() for i in metrics]

    with open("metrics.csv", "w", newline="", encoding="utf-8") as file:
        w = writer(file, delimiter=";")
        w.writerow(["r2", "adj_r2", "std_err", "max_err", "f_statistics"])
        w.writerows(res)

    print(time.time() - start)


    # pyplot.scatter(x, y)
    # x_line = np.arange(min(x), max(x), 0.001)
    # c = 0
    # for x, i in zip(names, results):
    #     func = eval(f"objective.{x}")
    #     y_line = func(x_line, *i.get()[0])
    #     pyplot.plot(x_line, y_line, '--', color='red', )
    #     c += 1
    # for x, i in zip(names2, results2):
    #     func = eval(f"objective_square.{x}_sqrt")
    #     y_line = func(x_line, *i.get()[0])
    #     pyplot.plot(x_line, y_line, '--', color='red', )
    #     c += 1
    # print(c)
    # pyplot.show()