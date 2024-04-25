from pandas import DataFrame
from scipy.optimize import curve_fit
import numpy as np
from numpy import *
import multiprocessing as mp
from sklearn.metrics import max_error
from inspect import signature
from re import findall 
import objectives

COLUMNS = ["formula", "formula_with_coefficients", "params_num", "r2", "adj_r2", "std_err","max_err", "f_stat"]
type_to_y = {
    "simple": lambda y: y,
    "square": lambda y: y ** 2,
    "sqrt": lambda y: np.sqrt(abs(y)),
    "inv": lambda y: 1 / y,
    "ln": lambda y: np.log(y),
    "exp": lambda y: np.e ** y
}
op_to_op = {
    "simple": "simple",
    "sqrt": "square",
    "square": "sqrt",
    "inv": "inv",
    "ln": "exp",
    "exp": "ln"
}


def metrics_calc(xdata, ydata, y_predicted, func):
    residuals = ydata - y_predicted
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((ydata - np.mean(ydata)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    n = len(xdata)
    k = len(signature(func).parameters) - 1
    adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - k - 1))
    std_derr = np.sqrt(np.sum((ydata - np.mean(ydata)) ** 2) / (n - 1))
    std_err = np.sqrt(1 - adj_r2) * std_derr
    max_err = max_error(ydata, y_predicted)
    f = (r2 / (1 - r2)) * ((n - k - 1) / k)
    return r2, adj_r2, std_err, max_err, f


def process_function(func, x, y, type_):
    try:
        popt, _ = curve_fit(func, x, type_to_y[type_](y), maxfev=10000)
        metrics = metrics_calc(x, y, type_to_y[op_to_op[type_]](func(x, *popt)), func)
        return popt, metrics
    except Exception as e:
        print(f"Unable to solve function {func}")
        return None


def find_popts_and_metrics(x, y, f_types):
    """Для всех функций возвращает коэффициенты и метрики"""
    names = [i for i in dir(objectives) if i.startswith("objective_")]
    names.sort(key=lambda x: int(findall(r"\d+", x)[0]))
    functions = [eval(f"objectives.{i}") for i in names]
    pool = mp.Pool(mp.cpu_count())
    results = [pool.apply_async(process_function, args=(f, x, y, f_types[n][0])) for n, f in zip(names, functions)]
    return [i.get() for i in results]


def replace_coeffs_with_numbers(formula, letters, numbers):
    """В функции заменяет буквы на числовые коэффициенты"""
    pattern = dict(zip(letters, list(map(str, numbers))))
    new_f = formula.translate(formula.maketrans(pattern))
    new_f = new_f.replace("+-", "-")
    return new_f

    
def make_result_table(data, columns=COLUMNS):
    """Запись данных в таблицу"""
    result_df = DataFrame(data, columns=columns)
    result_df.sort_values("r2", inplace=True, ascending=False)
    result_df.to_excel("result.xlsx")
