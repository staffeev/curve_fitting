import numpy as np

def objective_84(x, a, b):
    return a+b*(x)

def objective_84_sqrt(x, a, b):
    return np.sqrt(a+b*(x))

def objective_85(x, a, b):
    return a+b*(x)*(np.log(x))

def objective_85_sqrt(x, a, b):
    return np.sqrt(a+b*(x)*(np.log(x)))

def objective_86(x, a, b):
    return a+b*(x)**(1.5)

def objective_86_sqrt(x, a, b):
    return np.sqrt(a+b*(x)**(1.5))

def objective_87(x, a, b):
    return a+b*((x)**(2))

def objective_87_sqrt(x, a, b):
    return np.sqrt(a+b*((x)**(2)))

def objective_88(x, a, b):
    return a+b*((x)**(2))*(np.log(x))

def objective_88_sqrt(x, a, b):
    return np.sqrt(a+b*((x)**(2))*(np.log(x)))

def objective_89(x, a, b):
    return a+b*(x)**(2.5)

def objective_89_sqrt(x, a, b):
    return np.sqrt(a+b*(x)**(2.5))

def objective_90(x, a, b):
    return a+b*((x)**(3))

def objective_90_sqrt(x, a, b):
    return np.sqrt(a+b*((x)**(3)))

def objective_91(x, a, b):
    return a+b*(np.e)**(x)

def objective_91_sqrt(x, a, b):
    return np.sqrt(a+b*(np.e)**(x))

def objective_92(x, a, b):
    return a+b*(x)**(0.5)*(np.log(x))

def objective_92_sqrt(x, a, b):
    return np.sqrt(a+b*(x)**(0.5)*(np.log(x)))

def objective_93(x, a, b):
    return a+b*((np.log(x)))**(2)

def objective_93_sqrt(x, a, b):
    return np.sqrt(a+b*((np.log(x)))**(2))

def objective_94(x, a, b):
    return a+b*(x)/(np.log(x))

def objective_94_sqrt(x, a, b):
    return np.sqrt(a+b*(x)/(np.log(x)))

def objective_95(x, a, b):
    return a+b*(x)**(0.5)

def objective_95_sqrt(x, a, b):
    return np.sqrt(a+b*(x)**(0.5))

def objective_96(x, a, b):
    return a+b*(np.log(x))

def objective_96_sqrt(x, a, b):
    return np.sqrt(a+b*(np.log(x)))

def objective_97(x, a, b):
    return a+b/(np.log(x))

def objective_97_sqrt(x, a, b):
    return np.sqrt(a+b/(np.log(x)))

def objective_98(x, a, b):
    return a+b/(x)**(0.5)

def objective_98_sqrt(x, a, b):
    return np.sqrt(a+b/(x)**(0.5))

def objective_99(x, a, b):
    return a+b*(np.log(x))/(x)

def objective_99_sqrt(x, a, b):
    return np.sqrt(a+b*(np.log(x))/(x))

def objective_100(x, a, b):
    return a+b/(x)

def objective_100_sqrt(x, a, b):
    return np.sqrt(a+b/(x))

def objective_101(x, a, b):
    return a+b/(x)**(1.5)

def objective_101_sqrt(x, a, b):
    return np.sqrt(a+b/(x)**(1.5))

def objective_102(x, a, b):
    return a+b*(np.log(x))/((x)**(2))

def objective_102_sqrt(x, a, b):
    return np.sqrt(a+b*(np.log(x))/((x)**(2)))

def objective_103(x, a, b):
    return a+b/((x)**(2))

def objective_103_sqrt(x, a, b):
    return np.sqrt(a+b/((x)**(2)))

def objective_104(x, a, b):
    return a+b*(np.e)**((-x))

def objective_104_sqrt(x, a, b):
    return np.sqrt(a+b*(np.e)**((-x)))

def objective_3222(x, a, b, c):
    return a+b*(x)+c*((x)**(2))

def objective_3222_sqrt(x, a, b, c):
    return np.sqrt(a+b*(x)+c*((x)**(2)))

def objective_3223(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))

def objective_3223_sqrt(x, a, b, c, d):
    return np.sqrt(a+b*(x)+c*((x)**(2))+d*((x)**(3)))

def objective_3224(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))

def objective_3224_sqrt(x, a, b, c, d, e):
    return np.sqrt(a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4)))


all_objective_not_sqrt = [objective_100, objective_101, objective_102, objective_103, objective_104, objective_3222, objective_3223, objective_3224, objective_84, objective_85, objective_86, objective_87, objective_88, objective_89, objective_90, objective_91, objective_92, objective_93, objective_94, objective_95, objective_96, objective_97, objective_98, objective_99]
all_objective_sqrt = [objective_100_sqrt, objective_101_sqrt, objective_102_sqrt, objective_103_sqrt, objective_104_sqrt, objective_3222_sqrt, objective_3223_sqrt, objective_3224_sqrt, objective_84_sqrt, objective_85_sqrt, objective_86_sqrt, objective_87_sqrt, objective_88_sqrt, objective_89_sqrt, objective_90_sqrt, objective_91_sqrt, objective_92_sqrt, objective_93_sqrt, objective_94_sqrt, objective_95_sqrt, objective_96_sqrt, objective_97_sqrt, objective_98_sqrt, objective_99_sqrt]
