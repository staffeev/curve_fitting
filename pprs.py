from re import findall, sub

replace_exp = r"(\g<0>)"
coef_replace_exp = r"\g<0>*"


FUNCTION_PATTERN = "lambda x, {}: {}"

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

res = set()
f = list(map(str.strip, open("formulas3.txt").readlines()))
c = 0
c2 = 0


with open("objective.py", "a", encoding="utf-8") as file:
    # file.write("FUNCTIONS = [\n")
    x = 0
    for i in f:
        s, letters = parse_formula(i)
        v1, v2 = s.split("=")
        if v1 == "(y)":
            file.write(FUNCTION_PATTERN.format(x, ', '.join(letters), v2))
            x += 1
    # file.write("]")
