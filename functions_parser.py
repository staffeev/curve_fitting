from re import findall, sub
from pandas import read_excel
import os
import shutil

replace_exp = r"(\g<0>)"
coef_replace_exp = r"\g<0>*"

FUNCTION_PATTERN = """
def objective_{}_{}(x, {}):
    return {}
"""

RULES = {
    r"-?[x-y]": replace_exp,  # переменная
    r"-?(?<![\d.])[0-9](?![\d.])": replace_exp,  # целое число
    r"e\^": r"(np.e)^",  # е в степени
    r"\([ex-y]\)\^\(+-?\w+\)+": replace_exp,  # переменная в числовой степени или e^x или e^-x
    r"ln\(\w+\)": replace_exp,  # натуральный логарифм
    r"[+-=*/^][a-z]\(": coef_replace_exp,  # коэффициент в уравнении
    r"\(\*": r"*(",  # изменение (* на *(
    r"ln": r"np.log", # натуральный логарифм заменяется на log, чтобы numpy мог посчитать
    r"\)\(": r")*(", # умножение после степени
    r"\^": r"**"  # знак степени
}


def parse_formula(s):
    """Преобразование формулы из текста в вид питоновской функции"""
    for exp, repl_exp in RULES.items():
        s = sub(exp, repl_exp, s)
    return s, list(map(lambda x: x[0], findall(r"[a-z][+*/]", s)))


def parse_from_list(f, write_to_file=True):
    """Парсинг формул из списка и запись в файлы в папке ../objectives. 
    Также возвращает параметры каждой функции и тип в зависимости от степени игрека"""
    try:
        if write_to_file:
            os.remove("objectives.py")
    except:
        pass
    params_and_type = dict()
    file = open("objectives.py", "a", encoding="utf-8")
    file.write("import numpy as np\n")

    formula_start_to_file_and_operation = {
        "(y)": "simple",
        "(y)**(0.5)": "sqrt",
        "((y)**(2))": "square",
        "(np.log(y))": "ln",
        "((y)**((-1)))": "inv",
        "((e)**(y))": "exp"
    }
    x = 0
    for i in f:
        s, letters = parse_formula(i)
        try:
            v1, v2 = s.split("=")
            cur = formula_start_to_file_and_operation[v1]
            #cur = "simple"
            x += 1
            params_and_type[f"objective_{x}_{cur}"] = (cur, letters)
            letters = ", ".join(letters)
            if not write_to_file:
                continue
            file.write(FUNCTION_PATTERN.format(x, cur, letters, v2))
        except:
            print(i)
            
    file.close()
    return params_and_type


if __name__ == "__main__":
    f = read_excel("functions.xlsx", sheet_name="All_byParamNumber", header=None).iloc[:, 0].values.tolist()
    f = [i.strip("[NL]") for i in f if "y" in i and "=" in i and "x" in i]
    parse_from_list(f, write_to_file=True)