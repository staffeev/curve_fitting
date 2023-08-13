from re import findall
from pandas import read_excel
import numpy as np
from scipy.optimize import curve_fit
#from objective import *

F_PATTERN = """
def objective_{}(x, {}):
	return {}
    
"""
# def func(x, **kwargs):
#     return kwargs["a"] + kwargs["b"] / x


# def objective(x, *args):
#     return func(x, *args)


# def make_obj_function(s, num):
#     letters = findall("[a-wyzA-WYZ] ", s)
#     # with open("objective.py", "a", encoding="utf-8") as file:
#     #     file.write(F_PATTERN.format(num, ",".join(letters), s))



# dataframe = read_excel("points.xls")
# x, y = dataframe["X"], dataframe["Y"]
# # f = list(map(str.strip, open("simple2.txt").readlines()))
# # for x, i in enumerate(f):
# #     make_obj_function(i, x)
# # # sleep(3)
# popt, _ = curve_fit(objective, x, y, p0=np.ones(2))
# print(popt)

# for x, i in enumerate(f):
#     eval(f"print(curve_fit(objective_{x}, x, y))")
#     # popt, _ = curve_fit(objective, x, y)
# # print(popt)
# # [ 0.9425436  -0.12299779]
# # [ 0.46589457 -0.02157439]
