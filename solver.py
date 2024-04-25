from collections import defaultdict
from operator import itemgetter
import re
from typing import Dict, List, Optional, Tuple
import numpy as np

# from components.celery.conf import app
from curve_fitting import \
    find_fit_and_metrics, replace_constant_placeholders_with_numbers


EQS = {
    r"([0-9])([(,x,y,l])": r"\1*\2",        # замена слитного написания типа ax на a*x, включая ln
    r"\^": r"**",                           # замена символа возведения в степень
    r"lnx": r"np.log(x)",                   # ln на np.log
    r"xnp": r"x*np",                        # xnp на x*np
    r"e\*\*": r"*np.e**",                   # e** на *np.e**
    r"\)np": r")*np"                        # )np на )*np
}


# @app.task(name='solver.get_solutions')
def get_solutions(
        context: Dict,
        x_list: List[float],
        y_list: List[float],
        rows_count: Optional[int] = None,
        max_parameters: Optional[int] = None) -> List[Dict]:
    """
    Obtain the table with the best solutions by 2d equation solver for points data

    :param context: Celery context
    :param x_list: first log data list (x-curve)
    :param y_list: second log data list (y-curve)
    :param rows_count: result table rows count per function type
    :param max_parameters: max params number of the analyzed functions ("params" field in objectives.py)
    :return: table with the best solutions by 2d solver
    """
    x_data = np.array(x_list)
    y_data = np.array(y_list)

    fr_fit_metrics = find_fit_and_metrics(x_data, y_data, max_parameters)

    results = []

    for fun_record, fit, metrics in fr_fit_metrics:
        formula = fun_record['form']
        params = fun_record['params']
        fin_eq = replace_constant_placeholders_with_numbers(formula, params, fit)

        results.append(
            (formula, fin_eq, len(params), *metrics, fun_record['typ'])
        )

    # make results table
    columns = ("formula", "formula_with_coefficients", "params_num", "r2",
               "adj_r2", "std_err", "max_err", "f_stat", "func_type")
    results.sort(key=itemgetter(8, 3), reverse=True)  # by type and then by r2

    sorted_table = [dict(zip(columns, res)) for res in results]

    # we need rows_count best results of every function type we get (5 simple, 5 sqrt, etc)
    res_table = []

    type_cnt = defaultdict(int)
    for row in sorted_table:
        ft = row['func_type']
        cnt = type_cnt[ft]

        if rows_count is None or cnt < rows_count:
            res_table.append(row)
            type_cnt[ft] += 1

    return res_table


# @app.task(name='solver.evaluate_solver_equation')
def evaluate_solver_equation(context: Dict, equation: str, values: List[float]) -> List[Tuple[float, float]]:
    """
    Evaluate solver equation

    :param context: Celery context
    :param equation: equation as a formula string (2d solver result)
    :param values: values to evaluate formula (x-values)
    :return: x:y-values dict (formula eval result)
    """
    left, right = equation.split('=')

    # check equation for power functions
    power_pattern = r'y\^\(?(-?\d+\.?\d*)\)?'  # y^(number)= or y^number=
    match = re.fullmatch(power_pattern, left)
    additional_power = float(match.group(1)) if match else 1

    # check is equation is exp function
    exp_res = left == 'lny'

    # check equation about lnx functions and filter negative values in that case
    if 'lnx' in right:
        values = [val for val in values if val > 0]

    for exp, rep in EQS.items():
        right = re.sub(exp, rep, right)

    try:
        environment = {
            'np': np,
            'x': np.array(values)
        }

        eval_res = eval(right, environment)

    except OverflowError:
        return []

    res = []
    for er, val in zip(list(eval_res), values):
        if exp_res:
            res.append((val, np.exp(er)))
        elif not (additional_power == 2 and er < 0):
            res.append((val, er ** (1 / additional_power)))

    return res
