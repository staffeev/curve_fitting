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



# f = lambda v, a, b: (x := v[0], y := v[1], a * x + b * y)[-1]


# env = {
#     "x": 5,
#     "y": 4,
#     "xy": 10
# }

# print(eval("x+y + x*y", env))


from scipy.optimize import curve_fit
import pandas as pd
import numpy as np


# df = pd.read_csv("res.csv")
# print(df)


x_data = np.array([
    0.2357,
    0.2385,
    0.238,
    0.2355,
    0.2397,
    0.2441,
    0.2478,
    0.2536,
    0.2558,
    0.254,
    0.2499,
    0.2437,
    0.2387,
    0.2346,
    0.2263,
    0.2159,
    0.2242,
    0.2447,
    0.2515,
    0.2416,
])

y_data = np.array([
    2.3878,
    2.3196,
    2.3012,
    2.3032,
    2.3088,
    2.3914,
    2.4479,
    2.4497,
    2.4178,
    2.448,
    2.3864,
    2.3485,
    2.4053,
    2.4863,
    2.4833,
    2.4739,
    2.5254,
    2.409,
    2.433,
    2.4087,
])

z_data = np.array([
    96.5612,
    100.2544,
    99.7177,
    98.5717,
    104.0823,
    117.2733,
    127.875,
    131.7995,
    127.7468,
    115.2782,
    102.9339,
    97.4246,
    99.5319,
    102.1294,
    97.2883,
    93.2749,
    96.7599,
    103.353,
    105.3867,
    100.0734,

])

data = np.vstack((x_data, y_data))

f = lambda xy, A, B, C, D, E, F, G, H, I: A+B/(xy[0])+C/(xy[0])**(2)+D/(xy[0])**(3)+E*(xy[1])+F*(xy[1])**(2)+G*(xy[1])**(3)+H*(xy[1])**(4)+I*(xy[1])**(5)

print(curve_fit(f, data, z_data))
# print(curve_fit(f, data, z_data))

# # df2 = pd.DataFrame(np.hstack((np.array(x_data).T, np.array(y_data).T, np.array(z_data).T)))

# df2 = pd.DataFrame({"X_Value": x_data, "Y_Value": y_data, "Z_Value": z_data})


# m = df2.merge(df)


# x_data = np.array([
#     2.35237,
#     2.29363,
#     2.28363,
#     2.26098,
#     2.24592,
#     2.31062,
#     2.33417,
#     2.36682,
#     2.33781,
#     2.33164,
#     2.38865,
#     2.43849,
#     2.43161,
#     2.42777,
#     2.40816,
#     2.37814,
#     2.37278,
#     2.39401,
#     2.37794,
#     2.32952
# ])

# y_data = np.array([
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
# ])

# df = pd.DataFrame({"X": x_data, "Y": y_data})

