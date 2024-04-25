from pandas import read_excel
import numpy as np
from re import findall
from functions_parser import parse_from_list
from curve_fitting import find_popts_and_metrics, replace_coeffs_with_numbers, make_result_table
from time import time
import warnings
warnings.filterwarnings("ignore")


if __name__ == "__main__":
    start = time()
    formulas = read_excel("functions.xlsx", sheet_name="All_byParamNumber", header=None).iloc[:, 0].values.tolist()
    formulas = [i.strip("[NL]") for i in formulas if "y" in i and "=" in i and "x" in i]  # оставляем только "простые" формулы
    # парсинг формул и запись в файлы; если файлов нет, заменить False на True
    params_and_types = parse_from_list(formulas, write_to_file=False)
    dataframe = read_excel("points4.xlsx", dtype=np.float64)
    x, y = dataframe["X"].to_numpy(), dataframe["Y"].to_numpy()
    popts_and_metrics = find_popts_and_metrics(x, y, params_and_types)  # получение коэффициентовв и метрик
    all_letters = [i[1][1] for i in sorted(params_and_types.items(), key=lambda x: int(findall(r"\d+", x[0])[0]))]

    # занесение в результирующую таблицу
    results = []
    for f, letters, pm in zip(formulas, all_letters, popts_and_metrics):
        if pm is None:
            continue
        results.append((f, replace_coeffs_with_numbers(f, letters, pm[0]), len(letters), *pm[1]))
    make_result_table(results)
    print(f"Прошло времени: {time() - start} секунд")


    
