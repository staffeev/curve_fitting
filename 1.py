import multiprocessing as mp
import numpy as np
from numpy import log
# from time import time
import time
from pandas import read_excel
from scipy.optimize import curve_fit
from sklearn.metrics import max_error, r2_score
from matplotlib import pyplot
from scipy.special import erf
from inspect import signature


def metrics_calc(xdata, ydata, y_predicted, func):
    # residuals = ydata - y_predicted
    # ss_res = np.sum(residuals ** 2)
    # ss_tot = np.sum((ydata - np.mean(ydata)) ** 2)
    # r2 = 1 - (ss_res / ss_tot)
    r2 = r2_score(ydata, y_predicted)
    n = len(xdata)
    k = len(signature(func).parameters) - 1
    adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - k - 1))
    std_derr = np.sqrt(np.sum((ydata - y_predicted) ** 2) / (n - k - 1))
    std_err = np.sqrt(1 - adj_r2) * std_derr
    max_err = max_error(ydata, y_predicted)
    f = np.var(ydata, ddof=1) / np.var(y_predicted, ddof=1)
    return r2, adj_r2, std_err, max_err, f


def objective(x, a, b, c, d, e, f, g, h, i, j):
    return a+b/(x)+c/((x)**(2))+d/((x)**(3))+e/((x)**(4))+f/((x)**(5))+g/((x)**(6))+h/((x)**(7))+i/((x)**(8))+j/((x)**(9))


# def objective(x, a, b, c, d, e):
#     n= (x - c) / (np.sqrt(2) * d);
#     return a + 0.5 * (b) * (1.0 + erf(n)-(e / abs(e)+erf(n-d / (np.sqrt(2) * e))) * np.exp(d * d / (2.0 * e * e) + (c-x)/e));


def get_r2(y, *popt):
    residuals = y - objective(x, *popt)
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    return r2

if __name__ == "__main__":
    dataframe = read_excel("points.xls", dtype=np.float64)
    x, y = dataframe["X"].to_numpy(), dataframe["Y"].to_numpy()
    start = time.time()
    popt, _ = curve_fit(objective, x, y, maxfev=10000, method="dogbox")
    print(popt)

#    r2=0.3789190610316712 
#    r2adj=0.373398341574175 
#    StdErr=0.04208074166485599 
#    Fstat=76.32980143554007 
#    a= 86829.92657820386 
#    b= -1394348.374608006 
#    c= 9291917.141806583 
#    d= -32084296.51834343 
#    e= 54216579.05445311 
#    f= -7313272.312338508 
#    g= -148276675.6527885 
#    h= 282478430.3803547 
#    i= -228731606.3556824 
#    j= 72370727.73126141 
    print(metrics_calc(x, y, objective(x, *popt), objective))

    # pyplot.scatter(x, y)
    # x_line = np.arange(min(x), max(x), 0.0001)
    # y_line = objective(x_line, *popt)
    # pyplot.plot(x_line, y_line, '--', color='red')
    # pyplot.show()