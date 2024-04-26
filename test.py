# a = open("source/formulas.py").readlines()

# with open("source/formulas2.py", "w", encoding="utf-8") as file:
#     file.write(a[0])
#     for i in a[1:-1]:
#         print(i)
#         file.write('"' + i.strip() + '",\n')
#     file.write(a[-1])

# from scipy.optimize import curve_fit
# import numpy as np

# x = np.arange(0, 10, 0.1)
# y = np.arange(0, 100, 1)
# a = lambda x, a: a * x

# print(curve_fit(a, x, y))

# import re

# from source.formulas import FORMULAS

# a = open("source/formulas.py").readlines()

# with open("source/formulas2.py", "w", encoding="utf-8") as file:
#     file.write(a[0])
#     for i in FORMULAS:
#         i = re.sub("[a-z]", lambda p: p.group(0).upper(), i)
#         i = re.sub("[X-Z]", lambda p: p.group(0).lower(), i)
#         i = re.sub("(LN)", lambda p: p.group(0).lower(), i)
#         i = re.sub(r"E\^", lambda p: p.group(0).lower(), i)
#         file.write('"' + i + '",\n')
#     file.write(a[-1])

# from scipy.optimize import curve_fit


# x_data = [
#         2.35237,
#         2.29363,
#         2.28363,
#         2.26098,
#         2.24592,
#         2.31062,
#         2.33417,
#         2.36682,
#         2.33781,
#         2.33164,
#         2.38865,
#         2.43849,
#         2.43161,
#         2.42777,
#         2.40816,
#         2.37814,
#         2.37278,
#         2.39401,
#         2.37794,
#         2.32952
#     ]

# y_data = [
#     38.714,
#     39.3818,
#     41.4955,
#     42.6163,
#     42.744,
#     42.3376,
#     40.0728,
#     38.894,
#     41.9369,
#     50.2641,
#     58.301,
#     60.2696,
#     61.3845,
#     61.3555,
#     57.6738,
#     49.666,
#     40.5432,
#     36.908,
#     39.4805,
#     45.4094
# ]


# def f(x, A, C, E, B, D, F):
#     return (A+C*x+E*x**2)/(1+B*x+D*x**2+F*x**3)


# print(curve_fit(f, x_data, y_data, maxfev=100000))


# from source.build_objectives import parse_formula



# print(parse_formula("y^2=-10830031+14150350x-6160926x^2+894001x^3"))


import pandas as pd


# df = pd.read_excel("ExampleData.xls")
# df["X"] = -df["X"]
# df.to_excel("ExampleDataMinus.xlsx", index=False)



f = lambda v, a, b: (x := v[0], y := v[1], a * x + b * y)[-1]


env = {
    "x": 5,
    "y": 4,
    "xy": 10
}

print(eval("x+y + x*y", env))
