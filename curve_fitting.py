# fit a line to the economic data
from numpy import sin
from numpy import sqrt, log
from numpy import arange
from pandas import read_excel
from scipy.optimize import curve_fit
from matplotlib import pyplot


# def objective(x, a, b, c, d, e, f):
# 	return a + b / log(x) + c / (log(x) ** 2) + d / (log(x) ** 3) + e / (log(x) ** 4) + f / (log(x) ** 5)


objective = lambda x, a, b, c, d, e, f: a + b / log(x) + c / (log(x) ** 2) + d / (log(x) ** 3) + e / (log(x) ** 4) + f / (log(x) ** 5)

dataframe = read_excel("points.xls")
x, y = dataframe["X"], dataframe["Y"]
popt, _ = curve_fit(objective, x, y)
print(popt)
# # summarize the parameter values
# print(popt)
# # plot input vs output
# pyplot.scatter(x, y)
# # define a sequence of inputs between the smallest and largest known inputs
# x_line = arange(min(x), max(x), 1)
# # calculate the output for the range
# y_line = objective(x_line, *popt)
# # create a line plot for the mapping function
# pyplot.plot(x_line, y_line, '--', color='red')
# pyplot.show()