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
