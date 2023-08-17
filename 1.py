import multiprocessing as mp
import numpy as np
from numpy import log
# from time import time
import time
from pandas import read_excel
from scipy.optimize import curve_fit
from matplotlib import pyplot


def objective(x, a, b, c, d, e, f):
    return np.exp(a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))+f*((x)**(5)))

def objective_2769(x, a, c, e, g, i, k, b, d, f, h, j):
    return (a+c*(x[1])+e*(x[2])+g*(x[3])+i*(x[4])+k*(x[5]))/((1)+b*(x[1])+d*(x[2])+f*(x[3])+h*(x[4])+j*(x[5])) 


if __name__ == "__main__":
    dataframe = read_excel("points.xls", dtype=np.float64)
    x, y = dataframe["X"].to_numpy(), dataframe["Y"].to_numpy()
    x2 = x * x
    x3 = x2 * x
    x4 = x3 * x
    x5 = x4 * x
    xdata = {1: x, 2: x2, 3: x3, 4: x4, 5: x5}
    # pool = mp.Pool(mp.cpu_count())
    start = time.time()
    popt = curve_fit(objective_2769, xdata, y, maxfev=5000)
    # ob = [objective_0, objective_1, objective_2, objective_3, objective_4, objective_5, objective_6, objective_7, objective_8, objective_9]
    #results = [pool.apply_async(curve_fit, args=(objective, x, y)) for _ in range(100000)]
    #pool.close()
    print(time.time() - start)

    # #x = np.sqrt(x)
    # pyplot.scatter(x, y)
    # # define a sequence of inputs between the smallest and largest known inputs
    # x_line = np.arange(min(x), max(x), 0.001)
    # y_line = objective(x_line, *popt[0])
    # # create a line plot for the mapping function
    # pyplot.plot(x_line, y_line, '--', color='red')
    # pyplot.show()