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

import re

from source.formulas import FORMULAS

a = open("source/formulas.py").readlines()

with open("source/formulas2.py", "w", encoding="utf-8") as file:
    file.write(a[0])
    for i in FORMULAS:
        i = re.sub("[a-z]", lambda p: p.group(0).upper(), i)
        i = re.sub("[X-Z]", lambda p: p.group(0).lower(), i)
        i = re.sub("(LN)", lambda p: p.group(0).lower(), i)
        i = re.sub(r"E\^", lambda p: p.group(0).lower(), i)
        file.write('"' + i + '",\n')
    file.write(a[-1])

