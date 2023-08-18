from pandas import read_excel, DataFrame
from scipy.optimize import curve_fit
import numpy as np
from numpy import *
import time
import multiprocessing as mp
from matplotlib import pyplot
from sklearn.metrics import max_error, r2_score
from inspect import signature
import objective
import objective_square
from csv import writer
from functions_parser import parse_formula
from re import findall 


def metrics_calc(xdata, ydata, y_predicted, func):
    r2 = r2_score(ydata, y_predicted)
    n = len(xdata)
    k = len(signature(func).parameters) - 1
    adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - k - 1))
    std_derr = np.sqrt(np.sum((ydata - y_predicted) ** 2) / (n - k - 1))
    std_err = np.sqrt(1 - adj_r2) * std_derr
    max_err = max_error(ydata, y_predicted)
    f = (r2 / (1 - r2) * (n - k - 1) / k)
    return r2, adj_r2, std_err, max_err, f


if __name__ == "__main__":
    dataframe = read_excel("points.xls", dtype=np.float64)
    x, y = dataframe["X"].to_numpy(), dataframe["Y"].to_numpy()
    y_square = y ** 2

    pool = mp.Pool(mp.cpu_count())
    names1 = list(filter(lambda i: i.startswith("objective_"), dir(objective)))
    functions1 = [eval(f"objective.{i}") for i in names1]
    results = [pool.apply_async(curve_fit, args=(f, x, y), kwds={"maxfev": 10000}) for f in functions1]

    names2 = list(filter(lambda i: i.startswith("objective_") and not i.endswith("_sqrt"), dir(objective_square)))
    functions2 = [eval(f"objective_square.{i}") for i in names2]
    results2 = [pool.apply_async(curve_fit, args=(f, x, y_square), kwds={"maxfev": 10000}) for f in functions2]

    results = [i.get()[0] for i in results + results2]
    functions = functions1 + functions2
    metrics = [pool.apply_async(metrics_calc, args=(x, y, f(x, *popt), f)) for f, popt in zip(functions, results)]
    func_and_metr = list(zip(names1 + names2, results, [i.get() for i in metrics]))
    func_and_metr.sort(key=lambda x: int(findall(r"\d+", x[0])[0]))

    f_replaced = []
    formulas = read_excel("functions.xlsx", sheet_name="All_byParamNumber").iloc[:, 0].values.tolist()
    formulas = [i for i in formulas if "=" in i]
    for f, i in zip(formulas, func_and_metr):
        _, letters = parse_formula(f)
        new_f = f
        for letter, coef in zip(letters, i[1]):
            new_f = new_f.replace(letter, str(coef))
        new_f = new_f.replace("+-", "-")
        f_replaced.append((f, new_f, *i[2]))
    
    result_df = DataFrame(f_replaced, columns=["formula", "formula_with_coefficients", "r2", "adj_r2", "std_err","max_err", "f_stat"])
    result_df.to_excel("result.xlsx")


    


    # res = [i.get() for i in metrics]

    # with open("metrics.csv", "w", newline="", encoding="utf-8") as file:
    #     w = writer(file, delimiter=";")
    #     w.writerow(["r2", "adj_r2", "std_err", "max_err", "f_statistics"])
    #     w.writerows(res)