from re import findall, sub
from pandas import read_excel
import os

replace_exp = r"(\g<0>)"
coef_replace_exp = r"\g<0>*"

FUNCTION_PATTERN = """
def objective_{}(x, {}):
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
    for exp, repl_exp in RULES.items():
        s = sub(exp, repl_exp, s)
    return s, list(map(lambda x: x[0], findall(r"[a-z][+*/]", s)))


if __name__ == "__main__":
    try:
        os.remove("objective.py")
        os.remove("objective_square.py")
    except:
        pass
    f = read_excel("functions.xlsx", sheet_name="All_byParamNumber").iloc[:, 0].values.tolist()
    file = open("objective.py", "a", encoding="utf-8")
    file2 = open("objective_square.py", "a", encoding="utf-8")

    file.write("import numpy as np\n")
    file2.write("import numpy as np\n")
    x = 0
    for i in f:
        s, letters = parse_formula(i.strip("[NL]"))
        try:
            v1, v2 = s.split("=")
            if v1 == "(y)":
                file.write(FUNCTION_PATTERN.format(x, ', '.join(letters), v2))
                x += 1
            elif v1 == "(np.log(y))":
                file.write(FUNCTION_PATTERN.format(x, ", ".join(letters), f"np.exp({v2})"))
                x += 1
            elif v1 == "(y)**(0.5)":
                file.write(FUNCTION_PATTERN.format(x, ", ".join(letters), f"({v2}) ** 2"))
                x += 1
            elif v1 == "((y)**(2))":
                file2.write(FUNCTION_PATTERN.format(x, ", ".join(letters), v2))
                file2.write(FUNCTION_PATTERN.format(f"{x}_sqrt", ", ".join(letters), f"np.sqrt({v2})"))
                x += 1
            elif v1 == "((y)**((-1)))":
                file.write(FUNCTION_PATTERN.format(x, ", ".join(letters), f"({v2}) ** (-1)"))
                x += 1
            else:
                print(v1)
        except:
            pass

    file.close()
    file2.close()
