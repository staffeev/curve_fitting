from re import findall, sub

res = set()
f = list(map(str.strip, open("formulas3.txt").readlines()))
for i in f:
    var_exp = r"[x-yX-Y]"
    int_exp = r"(?<![\d.])[0-9](?![\d.])"  # натуральные числа до 9 включительно
    #ln_exp = r"ln\w+"  # натуральные логарифмы
    var_pow_exp = r"\([x-yX-Y]\)\^\(\w+\)"  # переменная в числовой степени
    replace_exp = r"(\g<0>)"  # на что заменить
    ln_replace_exp = r"log(\g<0>)"


    s = sub(var_exp, replace_exp, i)
    s = sub(int_exp, replace_exp, s)
    s = sub(var_pow_exp, replace_exp, s)



    # if findall(int_exp, i):
    #     s = sub(int_exp, replace_exp, i)
    #     if not findall(var_pow_exp, s):
    #         continue
    #     print(i)
    #     print(sub(var_pow_exp, replace_exp, s))
    #     print()


    blocks = set(findall(r"\^\w+", i))
    res = res.union(blocks)
print(sorted(res, key=lambda x: (len(x), x)))