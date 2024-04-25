import numpy as np

def objective_0(x, a, b):
    return a+b*(x)

def objective_1(x, a, b):
    return a+b*(x)*(np.log(x))

def objective_2(x, a, b):
    return a+b*(x)**(1.5)

def objective_3(x, a, b):
    return a+b*((x)**(2))

def objective_4(x, a, b):
    return a+b*((x)**(2))*(np.log(x))

def objective_5(x, a, b):
    return a+b*(x)**(2.5)

def objective_6(x, a, b):
    return a+b*((x)**(3))

def objective_7(x, a, b):
    return a+b*(np.e)**(x)

def objective_8(x, a, b):
    return a+b*(x)**(0.5)*(np.log(x))

def objective_9(x, a, b):
    return a+b*((np.log(x)))**(2)

def objective_10(x, a, b):
    return a+b*(x)/(np.log(x))

def objective_11(x, a, b):
    return a+b*(x)**(0.5)

def objective_12(x, a, b):
    return a+b*(np.log(x))

def objective_13(x, a, b):
    return a+b/(np.log(x))

def objective_14(x, a, b):
    return a+b/(x)**(0.5)

def objective_15(x, a, b):
    return a+b*(np.log(x))/(x)

def objective_16(x, a, b):
    return a+b/(x)

def objective_17(x, a, b):
    return a+b/(x)**(1.5)

def objective_18(x, a, b):
    return a+b*(np.log(x))/((x)**(2))

def objective_19(x, a, b):
    return a+b/((x)**(2))

def objective_20(x, a, b):
    return a+b*(np.e)**((-x))

def objective_21(x, a, b):
    return np.e ** (a+b*(x))

def objective_22(x, a, b):
    return np.e ** (a+b*(x)*(np.log(x)))

def objective_23(x, a, b):
    return np.e ** (a+b*(x)**(1.5))

def objective_24(x, a, b):
    return np.e ** (a+b*((x)**(2)))

def objective_25(x, a, b):
    return np.e ** (a+b*((x)**(2))*(np.log(x)))

def objective_26(x, a, b):
    return np.e ** (a+b*(x)**(2.5))

def objective_27(x, a, b):
    return np.e ** (a+b*((x)**(3)))

def objective_28(x, a, b):
    return np.e ** (a+b*(np.e)**(x))

def objective_29(x, a, b):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x)))

def objective_30(x, a, b):
    return np.e ** (a+b*((np.log(x)))**(2))

def objective_31(x, a, b):
    return np.e ** (a+b*(x)/(np.log(x)))

def objective_32(x, a, b):
    return np.e ** (a+b*(x)**(0.5))

def objective_33(x, a, b):
    return np.e ** (a+b*(np.log(x)))

def objective_34(x, a, b):
    return np.e ** (a+b/(np.log(x)))

def objective_35(x, a, b):
    return np.e ** (a+b/(x)**(0.5))

def objective_36(x, a, b):
    return np.e ** (a+b*(np.log(x))/(x))

def objective_37(x, a, b):
    return np.e ** (a+b/(x))

def objective_38(x, a, b):
    return np.e ** (a+b/(x)**(1.5))

def objective_39(x, a, b):
    return np.e ** (a+b*(np.log(x))/((x)**(2)))

def objective_40(x, a, b):
    return np.e ** (a+b/((x)**(2)))

def objective_41(x, a, b):
    return np.e ** (a+b*(np.e)**((-x)))

def objective_42(x, a, b):
    return (a+b*(x)) ** (-1)

def objective_43(x, a, b):
    return (a+b*(x)*(np.log(x))) ** (-1)

def objective_44(x, a, b):
    return (a+b*(x)**(1.5)) ** (-1)

def objective_45(x, a, b):
    return (a+b*((x)**(2))) ** (-1)

def objective_46(x, a, b):
    return (a+b*((x)**(2))*(np.log(x))) ** (-1)

def objective_47(x, a, b):
    return (a+b*(x)**(2.5)) ** (-1)

def objective_48(x, a, b):
    return (a+b*((x)**(3))) ** (-1)

def objective_49(x, a, b):
    return (a+b*(np.e)**(x)) ** (-1)

def objective_50(x, a, b):
    return (a+b*(x)**(0.5)*(np.log(x))) ** (-1)

def objective_51(x, a, b):
    return (a+b*((np.log(x)))**(2)) ** (-1)

def objective_52(x, a, b):
    return (a+b*(x)/(np.log(x))) ** (-1)

def objective_53(x, a, b):
    return (a+b*(x)**(0.5)) ** (-1)

def objective_54(x, a, b):
    return (a+b*(np.log(x))) ** (-1)

def objective_55(x, a, b):
    return (a+b/(np.log(x))) ** (-1)

def objective_56(x, a, b):
    return (a+b/(x)**(0.5)) ** (-1)

def objective_57(x, a, b):
    return (a+b*(np.log(x))/(x)) ** (-1)

def objective_58(x, a, b):
    return (a+b/(x)) ** (-1)

def objective_59(x, a, b):
    return (a+b/(x)**(1.5)) ** (-1)

def objective_60(x, a, b):
    return (a+b*(np.log(x))/((x)**(2))) ** (-1)

def objective_61(x, a, b):
    return (a+b/((x)**(2))) ** (-1)

def objective_62(x, a, b):
    return (a+b*(np.e)**((-x))) ** (-1)

def objective_63(x, a, b):
    return (a+b*(x)) ** 2

def objective_64(x, a, b):
    return (a+b*(x)*(np.log(x))) ** 2

def objective_65(x, a, b):
    return (a+b*(x)**(1.5)) ** 2

def objective_66(x, a, b):
    return (a+b*((x)**(2))) ** 2

def objective_67(x, a, b):
    return (a+b*((x)**(2))*(np.log(x))) ** 2

def objective_68(x, a, b):
    return (a+b*(x)**(2.5)) ** 2

def objective_69(x, a, b):
    return (a+b*((x)**(3))) ** 2

def objective_70(x, a, b):
    return (a+b*(np.e)**(x)) ** 2

def objective_71(x, a, b):
    return (a+b*(x)**(0.5)*(np.log(x))) ** 2

def objective_72(x, a, b):
    return (a+b*((np.log(x)))**(2)) ** 2

def objective_73(x, a, b):
    return (a+b*(x)/(np.log(x))) ** 2

def objective_74(x, a, b):
    return (a+b*(x)**(0.5)) ** 2

def objective_75(x, a, b):
    return (a+b*(np.log(x))) ** 2

def objective_76(x, a, b):
    return (a+b/(np.log(x))) ** 2

def objective_77(x, a, b):
    return (a+b/(x)**(0.5)) ** 2

def objective_78(x, a, b):
    return (a+b*(np.log(x))/(x)) ** 2

def objective_79(x, a, b):
    return (a+b/(x)) ** 2

def objective_80(x, a, b):
    return (a+b/(x)**(1.5)) ** 2

def objective_81(x, a, b):
    return (a+b*(np.log(x))/((x)**(2))) ** 2

def objective_82(x, a, b):
    return (a+b/((x)**(2))) ** 2

def objective_83(x, a, b):
    return (a+b*(np.e)**((-x))) ** 2

def objective_105(x, a, b, c):
    return a+b*(x)+c*(x)*(np.log(x))

def objective_106(x, a, b, c):
    return a+b*(x)+c*(x)**(1.5)

def objective_107(x, a, b, c):
    return a+b*(x)+c*((x)**(2))

def objective_108(x, a, b, c):
    return a+b*(x)+c*((x)**(2))*(np.log(x))

def objective_109(x, a, b, c):
    return a+b*(x)+c*(x)**(2.5)

def objective_110(x, a, b, c):
    return a+b*(x)+c*((x)**(3))

def objective_111(x, a, b, c):
    return a+b*(x)+c*(np.e)**(x)

def objective_112(x, a, b, c):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))

def objective_113(x, a, b, c):
    return a+b*(x)+c*((np.log(x)))**(2)

def objective_114(x, a, b, c):
    return a+b*(x)+c*(x)/(np.log(x))

def objective_115(x, a, b, c):
    return a+b*(x)+c*(x)**(0.5)

def objective_116(x, a, b, c):
    return a+b*(x)+c*(np.log(x))

def objective_117(x, a, b, c):
    return a+b*(x)+c/(np.log(x))

def objective_118(x, a, b, c):
    return a+b*(x)+c/(x)**(0.5)

def objective_119(x, a, b, c):
    return a+b*(x)+c*(np.log(x))/(x)

def objective_120(x, a, b, c):
    return a+b*(x)+c/(x)

def objective_121(x, a, b, c):
    return a+b*(x)+c/(x)**(1.5)

def objective_122(x, a, b, c):
    return a+b*(x)+c*(np.log(x))/((x)**(2))

def objective_123(x, a, b, c):
    return a+b*(x)+c/((x)**(2))

def objective_124(x, a, b, c):
    return a+b*(x)+c*(np.e)**((-x))

def objective_125(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)

def objective_126(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*((x)**(2))

def objective_127(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))

def objective_128(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)

def objective_129(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*((x)**(3))

def objective_130(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)

def objective_131(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))

def objective_132(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)

def objective_133(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*(x)/(np.log(x))

def objective_134(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)

def objective_135(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*(np.log(x))

def objective_136(x, a, b, c):
    return a+b*(x)*(np.log(x))+c/(np.log(x))

def objective_137(x, a, b, c):
    return a+b*(x)*(np.log(x))+c/(x)**(0.5)

def objective_138(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*(np.log(x))/(x)

def objective_139(x, a, b, c):
    return a+b*(x)*(np.log(x))+c/(x)

def objective_140(x, a, b, c):
    return a+b*(x)*(np.log(x))+c/(x)**(1.5)

def objective_141(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*(np.log(x))/((x)**(2))

def objective_142(x, a, b, c):
    return a+b*(x)*(np.log(x))+c/((x)**(2))

def objective_143(x, a, b, c):
    return a+b*(x)*(np.log(x))+c*(np.e)**((-x))

def objective_144(x, a, b, c):
    return a+b*(x)**(1.5)+c*((x)**(2))

def objective_145(x, a, b, c):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))

def objective_146(x, a, b, c):
    return a+b*(x)**(1.5)+c*(x)**(2.5)

def objective_147(x, a, b, c):
    return a+b*(x)**(1.5)+c*((x)**(3))

def objective_148(x, a, b, c):
    return a+b*(x)**(1.5)+c*(np.e)**(x)

def objective_149(x, a, b, c):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))

def objective_150(x, a, b, c):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)

def objective_151(x, a, b, c):
    return a+b*(x)**(1.5)+c*(x)/(np.log(x))

def objective_152(x, a, b, c):
    return a+b*(x)**(1.5)+c*(x)**(0.5)

def objective_153(x, a, b, c):
    return a+b*(x)**(1.5)+c*(np.log(x))

def objective_154(x, a, b, c):
    return a+b*(x)**(1.5)+c/(np.log(x))

def objective_155(x, a, b, c):
    return a+b*(x)**(1.5)+c/(x)**(0.5)

def objective_156(x, a, b, c):
    return a+b*(x)**(1.5)+c*(np.log(x))/(x)

def objective_157(x, a, b, c):
    return a+b*(x)**(1.5)+c/(x)

def objective_158(x, a, b, c):
    return a+b*(x)**(1.5)+c/(x)**(1.5)

def objective_159(x, a, b, c):
    return a+b*(x)**(1.5)+c*(np.log(x))/((x)**(2))

def objective_160(x, a, b, c):
    return a+b*(x)**(1.5)+c/((x)**(2))

def objective_161(x, a, b, c):
    return a+b*(x)**(1.5)+c*(np.e)**((-x))

def objective_162(x, a, b, c):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))

def objective_163(x, a, b, c):
    return a+b*((x)**(2))+c*(x)**(2.5)

def objective_164(x, a, b, c):
    return a+b*((x)**(2))+c*((x)**(3))

def objective_165(x, a, b, c):
    return a+b*((x)**(2))+c*(np.e)**(x)

def objective_166(x, a, b, c):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))

def objective_167(x, a, b, c):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)

def objective_168(x, a, b, c):
    return a+b*((x)**(2))+c*(x)/(np.log(x))

def objective_169(x, a, b, c):
    return a+b*((x)**(2))+c*(x)**(0.5)

def objective_170(x, a, b, c):
    return a+b*((x)**(2))+c*(np.log(x))

def objective_171(x, a, b, c):
    return a+b*((x)**(2))+c/(np.log(x))

def objective_172(x, a, b, c):
    return a+b*((x)**(2))+c/(x)**(0.5)

def objective_173(x, a, b, c):
    return a+b*((x)**(2))+c*(np.log(x))/(x)

def objective_174(x, a, b, c):
    return a+b*((x)**(2))+c/(x)

def objective_175(x, a, b, c):
    return a+b*((x)**(2))+c/(x)**(1.5)

def objective_176(x, a, b, c):
    return a+b*((x)**(2))+c*(np.log(x))/((x)**(2))

def objective_177(x, a, b, c):
    return a+b*((x)**(2))+c/((x)**(2))

def objective_178(x, a, b, c):
    return a+b*((x)**(2))+c*(np.e)**((-x))

def objective_179(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)

def objective_180(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))

def objective_181(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)

def objective_182(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))

def objective_183(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)

def objective_184(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))

def objective_185(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)

def objective_186(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))

def objective_187(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c/(np.log(x))

def objective_188(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c/(x)**(0.5)

def objective_189(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/(x)

def objective_190(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c/(x)

def objective_191(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c/(x)**(1.5)

def objective_192(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/((x)**(2))

def objective_193(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c/((x)**(2))

def objective_194(x, a, b, c):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**((-x))

def objective_195(x, a, b, c):
    return a+b*(x)**(2.5)+c*((x)**(3))

def objective_196(x, a, b, c):
    return a+b*(x)**(2.5)+c*(np.e)**(x)

def objective_197(x, a, b, c):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))

def objective_198(x, a, b, c):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)

def objective_199(x, a, b, c):
    return a+b*(x)**(2.5)+c*(x)/(np.log(x))

def objective_200(x, a, b, c):
    return a+b*(x)**(2.5)+c*(x)**(0.5)

def objective_201(x, a, b, c):
    return a+b*(x)**(2.5)+c*(np.log(x))

def objective_202(x, a, b, c):
    return a+b*(x)**(2.5)+c/(np.log(x))

def objective_203(x, a, b, c):
    return a+b*(x)**(2.5)+c/(x)**(0.5)

def objective_204(x, a, b, c):
    return a+b*(x)**(2.5)+c*(np.log(x))/(x)

def objective_205(x, a, b, c):
    return a+b*(x)**(2.5)+c/(x)

def objective_206(x, a, b, c):
    return a+b*(x)**(2.5)+c/(x)**(1.5)

def objective_207(x, a, b, c):
    return a+b*(x)**(2.5)+c*(np.log(x))/((x)**(2))

def objective_208(x, a, b, c):
    return a+b*(x)**(2.5)+c/((x)**(2))

def objective_209(x, a, b, c):
    return a+b*(x)**(2.5)+c*(np.e)**((-x))

def objective_210(x, a, b, c):
    return a+b*((x)**(3))+c*(np.e)**(x)

def objective_211(x, a, b, c):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))

def objective_212(x, a, b, c):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)

def objective_213(x, a, b, c):
    return a+b*((x)**(3))+c*(x)/(np.log(x))

def objective_214(x, a, b, c):
    return a+b*((x)**(3))+c*(x)**(0.5)

def objective_215(x, a, b, c):
    return a+b*((x)**(3))+c*(np.log(x))

def objective_216(x, a, b, c):
    return a+b*((x)**(3))+c/(np.log(x))

def objective_217(x, a, b, c):
    return a+b*((x)**(3))+c/(x)**(0.5)

def objective_218(x, a, b, c):
    return a+b*((x)**(3))+c*(np.log(x))/(x)

def objective_219(x, a, b, c):
    return a+b*((x)**(3))+c/(x)

def objective_220(x, a, b, c):
    return a+b*((x)**(3))+c/(x)**(1.5)

def objective_221(x, a, b, c):
    return a+b*((x)**(3))+c*(np.log(x))/((x)**(2))

def objective_222(x, a, b, c):
    return a+b*((x)**(3))+c/((x)**(2))

def objective_223(x, a, b, c):
    return a+b*((x)**(3))+c*(np.e)**((-x))

def objective_224(x, a, b, c):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))

def objective_225(x, a, b, c):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)

def objective_226(x, a, b, c):
    return a+b*(np.e)**(x)+c*(x)/(np.log(x))

def objective_227(x, a, b, c):
    return a+b*(np.e)**(x)+c*(x)**(0.5)

def objective_228(x, a, b, c):
    return a+b*(np.e)**(x)+c*(np.log(x))

def objective_229(x, a, b, c):
    return a+b*(np.e)**(x)+c/(np.log(x))

def objective_230(x, a, b, c):
    return a+b*(np.e)**(x)+c/(x)**(0.5)

def objective_231(x, a, b, c):
    return a+b*(np.e)**(x)+c*(np.log(x))/(x)

def objective_232(x, a, b, c):
    return a+b*(np.e)**(x)+c/(x)

def objective_233(x, a, b, c):
    return a+b*(np.e)**(x)+c/(x)**(1.5)

def objective_234(x, a, b, c):
    return a+b*(np.e)**(x)+c*(np.log(x))/((x)**(2))

def objective_235(x, a, b, c):
    return a+b*(np.e)**(x)+c/((x)**(2))

def objective_236(x, a, b, c):
    return a+b*(np.e)**(x)+c*(np.e)**((-x))

def objective_237(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)

def objective_238(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))

def objective_239(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5)

def objective_240(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))

def objective_241(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c/(np.log(x))

def objective_242(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)**(0.5)

def objective_243(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/(x)

def objective_244(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)

def objective_245(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)**(1.5)

def objective_246(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/((x)**(2))

def objective_247(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c/((x)**(2))

def objective_248(x, a, b, c):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.e)**((-x))

def objective_249(x, a, b, c):
    return a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))

def objective_250(x, a, b, c):
    return a+b*((np.log(x)))**(2)+c*(x)**(0.5)

def objective_251(x, a, b, c):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))

def objective_252(x, a, b, c):
    return a+b*((np.log(x)))**(2)+c/(np.log(x))

def objective_253(x, a, b, c):
    return a+b*((np.log(x)))**(2)+c/(x)**(0.5)

def objective_254(x, a, b, c):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))/(x)

def objective_255(x, a, b, c):
    return a+b*((np.log(x)))**(2)+c/(x)

def objective_256(x, a, b, c):
    return a+b*((np.log(x)))**(2)+c/(x)**(1.5)

def objective_257(x, a, b, c):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))/((x)**(2))

def objective_258(x, a, b, c):
    return a+b*((np.log(x)))**(2)+c/((x)**(2))

def objective_259(x, a, b, c):
    return a+b*((np.log(x)))**(2)+c*(np.e)**((-x))

def objective_260(x, a, b, c):
    return a+b*(x)/(np.log(x))+c*(x)**(0.5)

def objective_261(x, a, b, c):
    return a+b*(x)/(np.log(x))+c*(np.log(x))

def objective_262(x, a, b, c):
    return a+b*(x)/(np.log(x))+c/(np.log(x))

def objective_263(x, a, b, c):
    return a+b*(x)/(np.log(x))+c/(x)**(0.5)

def objective_264(x, a, b, c):
    return a+b*(x)/(np.log(x))+c*(np.log(x))/(x)

def objective_265(x, a, b, c):
    return a+b*(x)/(np.log(x))+c/(x)

def objective_266(x, a, b, c):
    return a+b*(x)/(np.log(x))+c/(x)**(1.5)

def objective_267(x, a, b, c):
    return a+b*(x)/(np.log(x))+c*(np.log(x))/((x)**(2))

def objective_268(x, a, b, c):
    return a+b*(x)/(np.log(x))+c/((x)**(2))

def objective_269(x, a, b, c):
    return a+b*(x)/(np.log(x))+c*(np.e)**((-x))

def objective_270(x, a, b, c):
    return a+b*(x)**(0.5)+c*(np.log(x))

def objective_271(x, a, b, c):
    return a+b*(x)**(0.5)+c/(np.log(x))

def objective_272(x, a, b, c):
    return a+b*(x)**(0.5)+c/(x)**(0.5)

def objective_273(x, a, b, c):
    return a+b*(x)**(0.5)+c*(np.log(x))/(x)

def objective_274(x, a, b, c):
    return a+b*(x)**(0.5)+c/(x)

def objective_275(x, a, b, c):
    return a+b*(x)**(0.5)+c/(x)**(1.5)

def objective_276(x, a, b, c):
    return a+b*(x)**(0.5)+c*(np.log(x))/((x)**(2))

def objective_277(x, a, b, c):
    return a+b*(x)**(0.5)+c/((x)**(2))

def objective_278(x, a, b, c):
    return a+b*(x)**(0.5)+c*(np.e)**((-x))

def objective_279(x, a, b, c):
    return a+b*(np.log(x))+c/(np.log(x))

def objective_280(x, a, b, c):
    return a+b*(np.log(x))+c/(x)**(0.5)

def objective_281(x, a, b, c):
    return a+b*(np.log(x))+c*(np.log(x))/(x)

def objective_282(x, a, b, c):
    return a+b*(np.log(x))+c/(x)

def objective_283(x, a, b, c):
    return a+b*(np.log(x))+c/(x)**(1.5)

def objective_284(x, a, b, c):
    return a+b*(np.log(x))+c*(np.log(x))/((x)**(2))

def objective_285(x, a, b, c):
    return a+b*(np.log(x))+c/((x)**(2))

def objective_286(x, a, b, c):
    return a+b*(np.log(x))+c*(np.e)**((-x))

def objective_287(x, a, b, c):
    return a+b/(np.log(x))+c/(x)**(0.5)

def objective_288(x, a, b, c):
    return a+b/(np.log(x))+c*(np.log(x))/(x)

def objective_289(x, a, b, c):
    return a+b/(np.log(x))+c/(x)

def objective_290(x, a, b, c):
    return a+b/(np.log(x))+c/(x)**(1.5)

def objective_291(x, a, b, c):
    return a+b/(np.log(x))+c*(np.log(x))/((x)**(2))

def objective_292(x, a, b, c):
    return a+b/(np.log(x))+c/((x)**(2))

def objective_293(x, a, b, c):
    return a+b/(np.log(x))+c*(np.e)**((-x))

def objective_294(x, a, b, c):
    return a+b/(x)**(0.5)+c*(np.log(x))/(x)

def objective_295(x, a, b, c):
    return a+b/(x)**(0.5)+c/(x)

def objective_296(x, a, b, c):
    return a+b/(x)**(0.5)+c/(x)**(1.5)

def objective_297(x, a, b, c):
    return a+b/(x)**(0.5)+c*(np.log(x))/((x)**(2))

def objective_298(x, a, b, c):
    return a+b/(x)**(0.5)+c/((x)**(2))

def objective_299(x, a, b, c):
    return a+b/(x)**(0.5)+c*(np.e)**((-x))

def objective_300(x, a, b, c):
    return a+b*(np.log(x))/(x)+c/(x)

def objective_301(x, a, b, c):
    return a+b*(np.log(x))/(x)+c/(x)**(1.5)

def objective_302(x, a, b, c):
    return a+b*(np.log(x))/(x)+c*(np.log(x))/((x)**(2))

def objective_303(x, a, b, c):
    return a+b*(np.log(x))/(x)+c/((x)**(2))

def objective_304(x, a, b, c):
    return a+b*(np.log(x))/(x)+c*(np.e)**((-x))

def objective_305(x, a, b, c):
    return a+b/(x)+c/(x)**(1.5)

def objective_306(x, a, b, c):
    return a+b/(x)+c*(np.log(x))/((x)**(2))

def objective_307(x, a, b, c):
    return a+b/(x)+c/((x)**(2))

def objective_308(x, a, b, c):
    return a+b/(x)+c*(np.e)**((-x))

def objective_309(x, a, b, c):
    return a+b/(x)**(1.5)+c*(np.log(x))/((x)**(2))

def objective_310(x, a, b, c):
    return a+b/(x)**(1.5)+c/((x)**(2))

def objective_311(x, a, b, c):
    return a+b/(x)**(1.5)+c*(np.e)**((-x))

def objective_312(x, a, b, c):
    return a+b*(np.log(x))/((x)**(2))+c/((x)**(2))

def objective_313(x, a, b, c):
    return a+b*(np.log(x))/((x)**(2))+c*(np.e)**((-x))

def objective_314(x, a, b, c):
    return a+b/((x)**(2))+c*(np.e)**((-x))

def objective_315(x, a, b, c):
    return np.e ** (a+b*(x)+c*(x)*(np.log(x)))

def objective_316(x, a, b, c):
    return np.e ** (a+b*(x)+c*(x)**(1.5))

def objective_317(x, a, b, c):
    return np.e ** (a+b*(x)+c*((x)**(2)))

def objective_318(x, a, b, c):
    return np.e ** (a+b*(x)+c*((x)**(2))*(np.log(x)))

def objective_319(x, a, b, c):
    return np.e ** (a+b*(x)+c*(x)**(2.5))

def objective_320(x, a, b, c):
    return np.e ** (a+b*(x)+c*((x)**(3)))

def objective_321(x, a, b, c):
    return np.e ** (a+b*(x)+c*(np.e)**(x))

def objective_322(x, a, b, c):
    return np.e ** (a+b*(x)+c*(x)**(0.5)*(np.log(x)))

def objective_323(x, a, b, c):
    return np.e ** (a+b*(x)+c*((np.log(x)))**(2))

def objective_324(x, a, b, c):
    return np.e ** (a+b*(x)+c*(x)/(np.log(x)))

def objective_325(x, a, b, c):
    return np.e ** (a+b*(x)+c*(x)**(0.5))

def objective_326(x, a, b, c):
    return np.e ** (a+b*(x)+c*(np.log(x)))

def objective_327(x, a, b, c):
    return np.e ** (a+b*(x)+c/(np.log(x)))

def objective_328(x, a, b, c):
    return np.e ** (a+b*(x)+c/(x)**(0.5))

def objective_329(x, a, b, c):
    return np.e ** (a+b*(x)+c*(np.log(x))/(x))

def objective_330(x, a, b, c):
    return np.e ** (a+b*(x)+c/(x))

def objective_331(x, a, b, c):
    return np.e ** (a+b*(x)+c/(x)**(1.5))

def objective_332(x, a, b, c):
    return np.e ** (a+b*(x)+c*(np.log(x))/((x)**(2)))

def objective_333(x, a, b, c):
    return np.e ** (a+b*(x)+c/((x)**(2)))

def objective_334(x, a, b, c):
    return np.e ** (a+b*(x)+c*(np.e)**((-x)))

def objective_335(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*(x)**(1.5))

def objective_336(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*((x)**(2)))

def objective_337(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x)))

def objective_338(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*(x)**(2.5))

def objective_339(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*((x)**(3)))

def objective_340(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*(np.e)**(x))

def objective_341(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x)))

def objective_342(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*((np.log(x)))**(2))

def objective_343(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*(x)/(np.log(x)))

def objective_344(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*(x)**(0.5))

def objective_345(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*(np.log(x)))

def objective_346(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c/(np.log(x)))

def objective_347(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c/(x)**(0.5))

def objective_348(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*(np.log(x))/(x))

def objective_349(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c/(x))

def objective_350(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c/(x)**(1.5))

def objective_351(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*(np.log(x))/((x)**(2)))

def objective_352(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c/((x)**(2)))

def objective_353(x, a, b, c):
    return np.e ** (a+b*(x)*(np.log(x))+c*(np.e)**((-x)))

def objective_354(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*((x)**(2)))

def objective_355(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x)))

def objective_356(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*(x)**(2.5))

def objective_357(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*((x)**(3)))

def objective_358(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*(np.e)**(x))

def objective_359(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x)))

def objective_360(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*((np.log(x)))**(2))

def objective_361(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*(x)/(np.log(x)))

def objective_362(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*(x)**(0.5))

def objective_363(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*(np.log(x)))

def objective_364(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c/(np.log(x)))

def objective_365(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c/(x)**(0.5))

def objective_366(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*(np.log(x))/(x))

def objective_367(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c/(x))

def objective_368(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c/(x)**(1.5))

def objective_369(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*(np.log(x))/((x)**(2)))

def objective_370(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c/((x)**(2)))

def objective_371(x, a, b, c):
    return np.e ** (a+b*(x)**(1.5)+c*(np.e)**((-x)))

def objective_372(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*((x)**(2))*(np.log(x)))

def objective_373(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*(x)**(2.5))

def objective_374(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*((x)**(3)))

def objective_375(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*(np.e)**(x))

def objective_376(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x)))

def objective_377(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*((np.log(x)))**(2))

def objective_378(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*(x)/(np.log(x)))

def objective_379(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*(x)**(0.5))

def objective_380(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*(np.log(x)))

def objective_381(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c/(np.log(x)))

def objective_382(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c/(x)**(0.5))

def objective_383(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*(np.log(x))/(x))

def objective_384(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c/(x))

def objective_385(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c/(x)**(1.5))

def objective_386(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*(np.log(x))/((x)**(2)))

def objective_387(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c/((x)**(2)))

def objective_388(x, a, b, c):
    return np.e ** (a+b*((x)**(2))+c*(np.e)**((-x)))

def objective_389(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5))

def objective_390(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c*((x)**(3)))

def objective_391(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x))

def objective_392(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x)))

def objective_393(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2))

def objective_394(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x)))

def objective_395(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5))

def objective_396(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c*(np.log(x)))

def objective_397(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c/(np.log(x)))

def objective_398(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c/(x)**(0.5))

def objective_399(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/(x))

def objective_400(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c/(x))

def objective_401(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c/(x)**(1.5))

def objective_402(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/((x)**(2)))

def objective_403(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c/((x)**(2)))

def objective_404(x, a, b, c):
    return np.e ** (a+b*((x)**(2))*(np.log(x))+c*(np.e)**((-x)))

def objective_405(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c*((x)**(3)))

def objective_406(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c*(np.e)**(x))

def objective_407(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x)))

def objective_408(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c*((np.log(x)))**(2))

def objective_409(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c*(x)/(np.log(x)))

def objective_410(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c*(x)**(0.5))

def objective_411(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c*(np.log(x)))

def objective_412(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c/(np.log(x)))

def objective_413(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c/(x)**(0.5))

def objective_414(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c*(np.log(x))/(x))

def objective_415(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c/(x))

def objective_416(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c/(x)**(1.5))

def objective_417(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c*(np.log(x))/((x)**(2)))

def objective_418(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c/((x)**(2)))

def objective_419(x, a, b, c):
    return np.e ** (a+b*(x)**(2.5)+c*(np.e)**((-x)))

def objective_420(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c*(np.e)**(x))

def objective_421(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x)))

def objective_422(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c*((np.log(x)))**(2))

def objective_423(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c*(x)/(np.log(x)))

def objective_424(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c*(x)**(0.5))

def objective_425(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c*(np.log(x)))

def objective_426(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c/(np.log(x)))

def objective_427(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c/(x)**(0.5))

def objective_428(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c*(np.log(x))/(x))

def objective_429(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c/(x))

def objective_430(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c/(x)**(1.5))

def objective_431(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c*(np.log(x))/((x)**(2)))

def objective_432(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c/((x)**(2)))

def objective_433(x, a, b, c):
    return np.e ** (a+b*((x)**(3))+c*(np.e)**((-x)))

def objective_434(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x)))

def objective_435(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c*((np.log(x)))**(2))

def objective_436(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c*(x)/(np.log(x)))

def objective_437(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c*(x)**(0.5))

def objective_438(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c*(np.log(x)))

def objective_439(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c/(np.log(x)))

def objective_440(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c/(x)**(0.5))

def objective_441(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c*(np.log(x))/(x))

def objective_442(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c/(x))

def objective_443(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c/(x)**(1.5))

def objective_444(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c*(np.log(x))/((x)**(2)))

def objective_445(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c/((x)**(2)))

def objective_446(x, a, b, c):
    return np.e ** (a+b*(np.e)**(x)+c*(np.e)**((-x)))

def objective_447(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2))

def objective_448(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x)))

def objective_449(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5))

def objective_450(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x)))

def objective_451(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c/(np.log(x)))

def objective_452(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c/(x)**(0.5))

def objective_453(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/(x))

def objective_454(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c/(x))

def objective_455(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c/(x)**(1.5))

def objective_456(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/((x)**(2)))

def objective_457(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c/((x)**(2)))

def objective_458(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)*(np.log(x))+c*(np.e)**((-x)))

def objective_459(x, a, b, c):
    return np.e ** (a+b*((np.log(x)))**(2)+c*(x)/(np.log(x)))

def objective_460(x, a, b, c):
    return np.e ** (a+b*((np.log(x)))**(2)+c*(x)**(0.5))

def objective_461(x, a, b, c):
    return np.e ** (a+b*((np.log(x)))**(2)+c*(np.log(x)))

def objective_462(x, a, b, c):
    return np.e ** (a+b*((np.log(x)))**(2)+c/(np.log(x)))

def objective_463(x, a, b, c):
    return np.e ** (a+b*((np.log(x)))**(2)+c/(x)**(0.5))

def objective_464(x, a, b, c):
    return np.e ** (a+b*((np.log(x)))**(2)+c*(np.log(x))/(x))

def objective_465(x, a, b, c):
    return np.e ** (a+b*((np.log(x)))**(2)+c/(x))

def objective_466(x, a, b, c):
    return np.e ** (a+b*((np.log(x)))**(2)+c/(x)**(1.5))

def objective_467(x, a, b, c):
    return np.e ** (a+b*((np.log(x)))**(2)+c*(np.log(x))/((x)**(2)))

def objective_468(x, a, b, c):
    return np.e ** (a+b*((np.log(x)))**(2)+c/((x)**(2)))

def objective_469(x, a, b, c):
    return np.e ** (a+b*((np.log(x)))**(2)+c*(np.e)**((-x)))

def objective_470(x, a, b, c):
    return np.e ** (a+b*(x)/(np.log(x))+c*(x)**(0.5))

def objective_471(x, a, b, c):
    return np.e ** (a+b*(x)/(np.log(x))+c*(np.log(x)))

def objective_472(x, a, b, c):
    return np.e ** (a+b*(x)/(np.log(x))+c/(np.log(x)))

def objective_473(x, a, b, c):
    return np.e ** (a+b*(x)/(np.log(x))+c/(x)**(0.5))

def objective_474(x, a, b, c):
    return np.e ** (a+b*(x)/(np.log(x))+c*(np.log(x))/(x))

def objective_475(x, a, b, c):
    return np.e ** (a+b*(x)/(np.log(x))+c/(x))

def objective_476(x, a, b, c):
    return np.e ** (a+b*(x)/(np.log(x))+c/(x)**(1.5))

def objective_477(x, a, b, c):
    return np.e ** (a+b*(x)/(np.log(x))+c*(np.log(x))/((x)**(2)))

def objective_478(x, a, b, c):
    return np.e ** (a+b*(x)/(np.log(x))+c/((x)**(2)))

def objective_479(x, a, b, c):
    return np.e ** (a+b*(x)/(np.log(x))+c*(np.e)**((-x)))

def objective_480(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)+c*(np.log(x)))

def objective_481(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)+c/(np.log(x)))

def objective_482(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)+c/(x)**(0.5))

def objective_483(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)+c*(np.log(x))/(x))

def objective_484(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)+c/(x))

def objective_485(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)+c/(x)**(1.5))

def objective_486(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)+c*(np.log(x))/((x)**(2)))

def objective_487(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)+c/((x)**(2)))

def objective_488(x, a, b, c):
    return np.e ** (a+b*(x)**(0.5)+c*(np.e)**((-x)))

def objective_489(x, a, b, c):
    return np.e ** (a+b*(np.log(x))+c/(np.log(x)))

def objective_490(x, a, b, c):
    return np.e ** (a+b*(np.log(x))+c/(x)**(0.5))

def objective_491(x, a, b, c):
    return np.e ** (a+b*(np.log(x))+c*(np.log(x))/(x))

def objective_492(x, a, b, c):
    return np.e ** (a+b*(np.log(x))+c/(x))

def objective_493(x, a, b, c):
    return np.e ** (a+b*(np.log(x))+c/(x)**(1.5))

def objective_494(x, a, b, c):
    return np.e ** (a+b*(np.log(x))+c*(np.log(x))/((x)**(2)))

def objective_495(x, a, b, c):
    return np.e ** (a+b*(np.log(x))+c/((x)**(2)))

def objective_496(x, a, b, c):
    return np.e ** (a+b*(np.log(x))+c*(np.e)**((-x)))

def objective_497(x, a, b, c):
    return np.e ** (a+b/(np.log(x))+c/(x)**(0.5))

def objective_498(x, a, b, c):
    return np.e ** (a+b/(np.log(x))+c*(np.log(x))/(x))

def objective_499(x, a, b, c):
    return np.e ** (a+b/(np.log(x))+c/(x))

def objective_500(x, a, b, c):
    return np.e ** (a+b/(np.log(x))+c/(x)**(1.5))

def objective_501(x, a, b, c):
    return np.e ** (a+b/(np.log(x))+c*(np.log(x))/((x)**(2)))

def objective_502(x, a, b, c):
    return np.e ** (a+b/(np.log(x))+c/((x)**(2)))

def objective_503(x, a, b, c):
    return np.e ** (a+b/(np.log(x))+c*(np.e)**((-x)))

def objective_504(x, a, b, c):
    return np.e ** (a+b/(x)**(0.5)+c*(np.log(x))/(x))

def objective_505(x, a, b, c):
    return np.e ** (a+b/(x)**(0.5)+c/(x))

def objective_506(x, a, b, c):
    return np.e ** (a+b/(x)**(0.5)+c/(x)**(1.5))

def objective_507(x, a, b, c):
    return np.e ** (a+b/(x)**(0.5)+c*(np.log(x))/((x)**(2)))

def objective_508(x, a, b, c):
    return np.e ** (a+b/(x)**(0.5)+c/((x)**(2)))

def objective_509(x, a, b, c):
    return np.e ** (a+b/(x)**(0.5)+c*(np.e)**((-x)))

def objective_510(x, a, b, c):
    return np.e ** (a+b*(np.log(x))/(x)+c/(x))

def objective_511(x, a, b, c):
    return np.e ** (a+b*(np.log(x))/(x)+c/(x)**(1.5))

def objective_512(x, a, b, c):
    return np.e ** (a+b*(np.log(x))/(x)+c*(np.log(x))/((x)**(2)))

def objective_513(x, a, b, c):
    return np.e ** (a+b*(np.log(x))/(x)+c/((x)**(2)))

def objective_514(x, a, b, c):
    return np.e ** (a+b*(np.log(x))/(x)+c*(np.e)**((-x)))

def objective_515(x, a, b, c):
    return np.e ** (a+b/(x)+c/(x)**(1.5))

def objective_516(x, a, b, c):
    return np.e ** (a+b/(x)+c*(np.log(x))/((x)**(2)))

def objective_517(x, a, b, c):
    return np.e ** (a+b/(x)+c/((x)**(2)))

def objective_518(x, a, b, c):
    return np.e ** (a+b/(x)+c*(np.e)**((-x)))

def objective_519(x, a, b, c):
    return np.e ** (a+b/(x)**(1.5)+c*(np.log(x))/((x)**(2)))

def objective_520(x, a, b, c):
    return np.e ** (a+b/(x)**(1.5)+c/((x)**(2)))

def objective_521(x, a, b, c):
    return np.e ** (a+b/(x)**(1.5)+c*(np.e)**((-x)))

def objective_522(x, a, b, c):
    return np.e ** (a+b*(np.log(x))/((x)**(2))+c/((x)**(2)))

def objective_523(x, a, b, c):
    return np.e ** (a+b*(np.log(x))/((x)**(2))+c*(np.e)**((-x)))

def objective_524(x, a, b, c):
    return np.e ** (a+b/((x)**(2))+c*(np.e)**((-x)))

def objective_525(x, a, b, c):
    return (a+b*(x)+c*(x)*(np.log(x))) ** (-1)

def objective_526(x, a, b, c):
    return (a+b*(x)+c*(x)**(1.5)) ** (-1)

def objective_527(x, a, b, c):
    return (a+b*(x)+c*((x)**(2))) ** (-1)

def objective_528(x, a, b, c):
    return (a+b*(x)+c*((x)**(2))*(np.log(x))) ** (-1)

def objective_529(x, a, b, c):
    return (a+b*(x)+c*(x)**(2.5)) ** (-1)

def objective_530(x, a, b, c):
    return (a+b*(x)+c*((x)**(3))) ** (-1)

def objective_531(x, a, b, c):
    return (a+b*(x)+c*(np.e)**(x)) ** (-1)

def objective_532(x, a, b, c):
    return (a+b*(x)+c*(x)**(0.5)*(np.log(x))) ** (-1)

def objective_533(x, a, b, c):
    return (a+b*(x)+c*((np.log(x)))**(2)) ** (-1)

def objective_534(x, a, b, c):
    return (a+b*(x)+c*(x)/(np.log(x))) ** (-1)

def objective_535(x, a, b, c):
    return (a+b*(x)+c*(x)**(0.5)) ** (-1)

def objective_536(x, a, b, c):
    return (a+b*(x)+c*(np.log(x))) ** (-1)

def objective_537(x, a, b, c):
    return (a+b*(x)+c/(np.log(x))) ** (-1)

def objective_538(x, a, b, c):
    return (a+b*(x)+c/(x)**(0.5)) ** (-1)

def objective_539(x, a, b, c):
    return (a+b*(x)+c*(np.log(x))/(x)) ** (-1)

def objective_540(x, a, b, c):
    return (a+b*(x)+c/(x)) ** (-1)

def objective_541(x, a, b, c):
    return (a+b*(x)+c/(x)**(1.5)) ** (-1)

def objective_542(x, a, b, c):
    return (a+b*(x)+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_543(x, a, b, c):
    return (a+b*(x)+c/((x)**(2))) ** (-1)

def objective_544(x, a, b, c):
    return (a+b*(x)+c*(np.e)**((-x))) ** (-1)

def objective_545(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*(x)**(1.5)) ** (-1)

def objective_546(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*((x)**(2))) ** (-1)

def objective_547(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))) ** (-1)

def objective_548(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*(x)**(2.5)) ** (-1)

def objective_549(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*((x)**(3))) ** (-1)

def objective_550(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*(np.e)**(x)) ** (-1)

def objective_551(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))) ** (-1)

def objective_552(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)) ** (-1)

def objective_553(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*(x)/(np.log(x))) ** (-1)

def objective_554(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*(x)**(0.5)) ** (-1)

def objective_555(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*(np.log(x))) ** (-1)

def objective_556(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c/(np.log(x))) ** (-1)

def objective_557(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c/(x)**(0.5)) ** (-1)

def objective_558(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*(np.log(x))/(x)) ** (-1)

def objective_559(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c/(x)) ** (-1)

def objective_560(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c/(x)**(1.5)) ** (-1)

def objective_561(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_562(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c/((x)**(2))) ** (-1)

def objective_563(x, a, b, c):
    return (a+b*(x)*(np.log(x))+c*(np.e)**((-x))) ** (-1)

def objective_564(x, a, b, c):
    return (a+b*(x)**(1.5)+c*((x)**(2))) ** (-1)

def objective_565(x, a, b, c):
    return (a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))) ** (-1)

def objective_566(x, a, b, c):
    return (a+b*(x)**(1.5)+c*(x)**(2.5)) ** (-1)

def objective_567(x, a, b, c):
    return (a+b*(x)**(1.5)+c*((x)**(3))) ** (-1)

def objective_568(x, a, b, c):
    return (a+b*(x)**(1.5)+c*(np.e)**(x)) ** (-1)

def objective_569(x, a, b, c):
    return (a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))) ** (-1)

def objective_570(x, a, b, c):
    return (a+b*(x)**(1.5)+c*((np.log(x)))**(2)) ** (-1)

def objective_571(x, a, b, c):
    return (a+b*(x)**(1.5)+c*(x)/(np.log(x))) ** (-1)

def objective_572(x, a, b, c):
    return (a+b*(x)**(1.5)+c*(x)**(0.5)) ** (-1)

def objective_573(x, a, b, c):
    return (a+b*(x)**(1.5)+c*(np.log(x))) ** (-1)

def objective_574(x, a, b, c):
    return (a+b*(x)**(1.5)+c/(np.log(x))) ** (-1)

def objective_575(x, a, b, c):
    return (a+b*(x)**(1.5)+c/(x)**(0.5)) ** (-1)

def objective_576(x, a, b, c):
    return (a+b*(x)**(1.5)+c*(np.log(x))/(x)) ** (-1)

def objective_577(x, a, b, c):
    return (a+b*(x)**(1.5)+c/(x)) ** (-1)

def objective_578(x, a, b, c):
    return (a+b*(x)**(1.5)+c/(x)**(1.5)) ** (-1)

def objective_579(x, a, b, c):
    return (a+b*(x)**(1.5)+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_580(x, a, b, c):
    return (a+b*(x)**(1.5)+c/((x)**(2))) ** (-1)

def objective_581(x, a, b, c):
    return (a+b*(x)**(1.5)+c*(np.e)**((-x))) ** (-1)

def objective_582(x, a, b, c):
    return (a+b*((x)**(2))+c*((x)**(2))*(np.log(x))) ** (-1)

def objective_583(x, a, b, c):
    return (a+b*((x)**(2))+c*(x)**(2.5)) ** (-1)

def objective_584(x, a, b, c):
    return (a+b*((x)**(2))+c*((x)**(3))) ** (-1)

def objective_585(x, a, b, c):
    return (a+b*((x)**(2))+c*(np.e)**(x)) ** (-1)

def objective_586(x, a, b, c):
    return (a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))) ** (-1)

def objective_587(x, a, b, c):
    return (a+b*((x)**(2))+c*((np.log(x)))**(2)) ** (-1)

def objective_588(x, a, b, c):
    return (a+b*((x)**(2))+c*(x)/(np.log(x))) ** (-1)

def objective_589(x, a, b, c):
    return (a+b*((x)**(2))+c*(x)**(0.5)) ** (-1)

def objective_590(x, a, b, c):
    return (a+b*((x)**(2))+c*(np.log(x))) ** (-1)

def objective_591(x, a, b, c):
    return (a+b*((x)**(2))+c/(np.log(x))) ** (-1)

def objective_592(x, a, b, c):
    return (a+b*((x)**(2))+c/(x)**(0.5)) ** (-1)

def objective_593(x, a, b, c):
    return (a+b*((x)**(2))+c*(np.log(x))/(x)) ** (-1)

def objective_594(x, a, b, c):
    return (a+b*((x)**(2))+c/(x)) ** (-1)

def objective_595(x, a, b, c):
    return (a+b*((x)**(2))+c/(x)**(1.5)) ** (-1)

def objective_596(x, a, b, c):
    return (a+b*((x)**(2))+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_597(x, a, b, c):
    return (a+b*((x)**(2))+c/((x)**(2))) ** (-1)

def objective_598(x, a, b, c):
    return (a+b*((x)**(2))+c*(np.e)**((-x))) ** (-1)

def objective_599(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)) ** (-1)

def objective_600(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c*((x)**(3))) ** (-1)

def objective_601(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)) ** (-1)

def objective_602(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))) ** (-1)

def objective_603(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)) ** (-1)

def objective_604(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))) ** (-1)

def objective_605(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)) ** (-1)

def objective_606(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c*(np.log(x))) ** (-1)

def objective_607(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c/(np.log(x))) ** (-1)

def objective_608(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c/(x)**(0.5)) ** (-1)

def objective_609(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/(x)) ** (-1)

def objective_610(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c/(x)) ** (-1)

def objective_611(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c/(x)**(1.5)) ** (-1)

def objective_612(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_613(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c/((x)**(2))) ** (-1)

def objective_614(x, a, b, c):
    return (a+b*((x)**(2))*(np.log(x))+c*(np.e)**((-x))) ** (-1)

def objective_615(x, a, b, c):
    return (a+b*(x)**(2.5)+c*((x)**(3))) ** (-1)

def objective_616(x, a, b, c):
    return (a+b*(x)**(2.5)+c*(np.e)**(x)) ** (-1)

def objective_617(x, a, b, c):
    return (a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))) ** (-1)

def objective_618(x, a, b, c):
    return (a+b*(x)**(2.5)+c*((np.log(x)))**(2)) ** (-1)

def objective_619(x, a, b, c):
    return (a+b*(x)**(2.5)+c*(x)/(np.log(x))) ** (-1)

def objective_620(x, a, b, c):
    return (a+b*(x)**(2.5)+c*(x)**(0.5)) ** (-1)

def objective_621(x, a, b, c):
    return (a+b*(x)**(2.5)+c*(np.log(x))) ** (-1)

def objective_622(x, a, b, c):
    return (a+b*(x)**(2.5)+c/(np.log(x))) ** (-1)

def objective_623(x, a, b, c):
    return (a+b*(x)**(2.5)+c/(x)**(0.5)) ** (-1)

def objective_624(x, a, b, c):
    return (a+b*(x)**(2.5)+c*(np.log(x))/(x)) ** (-1)

def objective_625(x, a, b, c):
    return (a+b*(x)**(2.5)+c/(x)) ** (-1)

def objective_626(x, a, b, c):
    return (a+b*(x)**(2.5)+c/(x)**(1.5)) ** (-1)

def objective_627(x, a, b, c):
    return (a+b*(x)**(2.5)+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_628(x, a, b, c):
    return (a+b*(x)**(2.5)+c/((x)**(2))) ** (-1)

def objective_629(x, a, b, c):
    return (a+b*(x)**(2.5)+c*(np.e)**((-x))) ** (-1)

def objective_630(x, a, b, c):
    return (a+b*((x)**(3))+c*(np.e)**(x)) ** (-1)

def objective_631(x, a, b, c):
    return (a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))) ** (-1)

def objective_632(x, a, b, c):
    return (a+b*((x)**(3))+c*((np.log(x)))**(2)) ** (-1)

def objective_633(x, a, b, c):
    return (a+b*((x)**(3))+c*(x)/(np.log(x))) ** (-1)

def objective_634(x, a, b, c):
    return (a+b*((x)**(3))+c*(x)**(0.5)) ** (-1)

def objective_635(x, a, b, c):
    return (a+b*((x)**(3))+c*(np.log(x))) ** (-1)

def objective_636(x, a, b, c):
    return (a+b*((x)**(3))+c/(np.log(x))) ** (-1)

def objective_637(x, a, b, c):
    return (a+b*((x)**(3))+c/(x)**(0.5)) ** (-1)

def objective_638(x, a, b, c):
    return (a+b*((x)**(3))+c*(np.log(x))/(x)) ** (-1)

def objective_639(x, a, b, c):
    return (a+b*((x)**(3))+c/(x)) ** (-1)

def objective_640(x, a, b, c):
    return (a+b*((x)**(3))+c/(x)**(1.5)) ** (-1)

def objective_641(x, a, b, c):
    return (a+b*((x)**(3))+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_642(x, a, b, c):
    return (a+b*((x)**(3))+c/((x)**(2))) ** (-1)

def objective_643(x, a, b, c):
    return (a+b*((x)**(3))+c*(np.e)**((-x))) ** (-1)

def objective_644(x, a, b, c):
    return (a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))) ** (-1)

def objective_645(x, a, b, c):
    return (a+b*(np.e)**(x)+c*((np.log(x)))**(2)) ** (-1)

def objective_646(x, a, b, c):
    return (a+b*(np.e)**(x)+c*(x)/(np.log(x))) ** (-1)

def objective_647(x, a, b, c):
    return (a+b*(np.e)**(x)+c*(x)**(0.5)) ** (-1)

def objective_648(x, a, b, c):
    return (a+b*(np.e)**(x)+c*(np.log(x))) ** (-1)

def objective_649(x, a, b, c):
    return (a+b*(np.e)**(x)+c/(np.log(x))) ** (-1)

def objective_650(x, a, b, c):
    return (a+b*(np.e)**(x)+c/(x)**(0.5)) ** (-1)

def objective_651(x, a, b, c):
    return (a+b*(np.e)**(x)+c*(np.log(x))/(x)) ** (-1)

def objective_652(x, a, b, c):
    return (a+b*(np.e)**(x)+c/(x)) ** (-1)

def objective_653(x, a, b, c):
    return (a+b*(np.e)**(x)+c/(x)**(1.5)) ** (-1)

def objective_654(x, a, b, c):
    return (a+b*(np.e)**(x)+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_655(x, a, b, c):
    return (a+b*(np.e)**(x)+c/((x)**(2))) ** (-1)

def objective_656(x, a, b, c):
    return (a+b*(np.e)**(x)+c*(np.e)**((-x))) ** (-1)

def objective_657(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)) ** (-1)

def objective_658(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))) ** (-1)

def objective_659(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5)) ** (-1)

def objective_660(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))) ** (-1)

def objective_661(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c/(np.log(x))) ** (-1)

def objective_662(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c/(x)**(0.5)) ** (-1)

def objective_663(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/(x)) ** (-1)

def objective_664(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c/(x)) ** (-1)

def objective_665(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c/(x)**(1.5)) ** (-1)

def objective_666(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_667(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c/((x)**(2))) ** (-1)

def objective_668(x, a, b, c):
    return (a+b*(x)**(0.5)*(np.log(x))+c*(np.e)**((-x))) ** (-1)

def objective_669(x, a, b, c):
    return (a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))) ** (-1)

def objective_670(x, a, b, c):
    return (a+b*((np.log(x)))**(2)+c*(x)**(0.5)) ** (-1)

def objective_671(x, a, b, c):
    return (a+b*((np.log(x)))**(2)+c*(np.log(x))) ** (-1)

def objective_672(x, a, b, c):
    return (a+b*((np.log(x)))**(2)+c/(np.log(x))) ** (-1)

def objective_673(x, a, b, c):
    return (a+b*((np.log(x)))**(2)+c/(x)**(0.5)) ** (-1)

def objective_674(x, a, b, c):
    return (a+b*((np.log(x)))**(2)+c*(np.log(x))/(x)) ** (-1)

def objective_675(x, a, b, c):
    return (a+b*((np.log(x)))**(2)+c/(x)) ** (-1)

def objective_676(x, a, b, c):
    return (a+b*((np.log(x)))**(2)+c/(x)**(1.5)) ** (-1)

def objective_677(x, a, b, c):
    return (a+b*((np.log(x)))**(2)+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_678(x, a, b, c):
    return (a+b*((np.log(x)))**(2)+c/((x)**(2))) ** (-1)

def objective_679(x, a, b, c):
    return (a+b*((np.log(x)))**(2)+c*(np.e)**((-x))) ** (-1)

def objective_680(x, a, b, c):
    return (a+b*(x)/(np.log(x))+c*(x)**(0.5)) ** (-1)

def objective_681(x, a, b, c):
    return (a+b*(x)/(np.log(x))+c*(np.log(x))) ** (-1)

def objective_682(x, a, b, c):
    return (a+b*(x)/(np.log(x))+c/(np.log(x))) ** (-1)

def objective_683(x, a, b, c):
    return (a+b*(x)/(np.log(x))+c/(x)**(0.5)) ** (-1)

def objective_684(x, a, b, c):
    return (a+b*(x)/(np.log(x))+c*(np.log(x))/(x)) ** (-1)

def objective_685(x, a, b, c):
    return (a+b*(x)/(np.log(x))+c/(x)) ** (-1)

def objective_686(x, a, b, c):
    return (a+b*(x)/(np.log(x))+c/(x)**(1.5)) ** (-1)

def objective_687(x, a, b, c):
    return (a+b*(x)/(np.log(x))+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_688(x, a, b, c):
    return (a+b*(x)/(np.log(x))+c/((x)**(2))) ** (-1)

def objective_689(x, a, b, c):
    return (a+b*(x)/(np.log(x))+c*(np.e)**((-x))) ** (-1)

def objective_690(x, a, b, c):
    return (a+b*(x)**(0.5)+c*(np.log(x))) ** (-1)

def objective_691(x, a, b, c):
    return (a+b*(x)**(0.5)+c/(np.log(x))) ** (-1)

def objective_692(x, a, b, c):
    return (a+b*(x)**(0.5)+c/(x)**(0.5)) ** (-1)

def objective_693(x, a, b, c):
    return (a+b*(x)**(0.5)+c*(np.log(x))/(x)) ** (-1)

def objective_694(x, a, b, c):
    return (a+b*(x)**(0.5)+c/(x)) ** (-1)

def objective_695(x, a, b, c):
    return (a+b*(x)**(0.5)+c/(x)**(1.5)) ** (-1)

def objective_696(x, a, b, c):
    return (a+b*(x)**(0.5)+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_697(x, a, b, c):
    return (a+b*(x)**(0.5)+c/((x)**(2))) ** (-1)

def objective_698(x, a, b, c):
    return (a+b*(x)**(0.5)+c*(np.e)**((-x))) ** (-1)

def objective_699(x, a, b, c):
    return (a+b*(np.log(x))+c/(np.log(x))) ** (-1)

def objective_700(x, a, b, c):
    return (a+b*(np.log(x))+c/(x)**(0.5)) ** (-1)

def objective_701(x, a, b, c):
    return (a+b*(np.log(x))+c*(np.log(x))/(x)) ** (-1)

def objective_702(x, a, b, c):
    return (a+b*(np.log(x))+c/(x)) ** (-1)

def objective_703(x, a, b, c):
    return (a+b*(np.log(x))+c/(x)**(1.5)) ** (-1)

def objective_704(x, a, b, c):
    return (a+b*(np.log(x))+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_705(x, a, b, c):
    return (a+b*(np.log(x))+c/((x)**(2))) ** (-1)

def objective_706(x, a, b, c):
    return (a+b*(np.log(x))+c*(np.e)**((-x))) ** (-1)

def objective_707(x, a, b, c):
    return (a+b/(np.log(x))+c/(x)**(0.5)) ** (-1)

def objective_708(x, a, b, c):
    return (a+b/(np.log(x))+c*(np.log(x))/(x)) ** (-1)

def objective_709(x, a, b, c):
    return (a+b/(np.log(x))+c/(x)) ** (-1)

def objective_710(x, a, b, c):
    return (a+b/(np.log(x))+c/(x)**(1.5)) ** (-1)

def objective_711(x, a, b, c):
    return (a+b/(np.log(x))+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_712(x, a, b, c):
    return (a+b/(np.log(x))+c/((x)**(2))) ** (-1)

def objective_713(x, a, b, c):
    return (a+b/(np.log(x))+c*(np.e)**((-x))) ** (-1)

def objective_714(x, a, b, c):
    return (a+b/(x)**(0.5)+c*(np.log(x))/(x)) ** (-1)

def objective_715(x, a, b, c):
    return (a+b/(x)**(0.5)+c/(x)) ** (-1)

def objective_716(x, a, b, c):
    return (a+b/(x)**(0.5)+c/(x)**(1.5)) ** (-1)

def objective_717(x, a, b, c):
    return (a+b/(x)**(0.5)+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_718(x, a, b, c):
    return (a+b/(x)**(0.5)+c/((x)**(2))) ** (-1)

def objective_719(x, a, b, c):
    return (a+b/(x)**(0.5)+c*(np.e)**((-x))) ** (-1)

def objective_720(x, a, b, c):
    return (a+b*(np.log(x))/(x)+c/(x)) ** (-1)

def objective_721(x, a, b, c):
    return (a+b*(np.log(x))/(x)+c/(x)**(1.5)) ** (-1)

def objective_722(x, a, b, c):
    return (a+b*(np.log(x))/(x)+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_723(x, a, b, c):
    return (a+b*(np.log(x))/(x)+c/((x)**(2))) ** (-1)

def objective_724(x, a, b, c):
    return (a+b*(np.log(x))/(x)+c*(np.e)**((-x))) ** (-1)

def objective_725(x, a, b, c):
    return (a+b/(x)+c/(x)**(1.5)) ** (-1)

def objective_726(x, a, b, c):
    return (a+b/(x)+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_727(x, a, b, c):
    return (a+b/(x)+c/((x)**(2))) ** (-1)

def objective_728(x, a, b, c):
    return (a+b/(x)+c*(np.e)**((-x))) ** (-1)

def objective_729(x, a, b, c):
    return (a+b/(x)**(1.5)+c*(np.log(x))/((x)**(2))) ** (-1)

def objective_730(x, a, b, c):
    return (a+b/(x)**(1.5)+c/((x)**(2))) ** (-1)

def objective_731(x, a, b, c):
    return (a+b/(x)**(1.5)+c*(np.e)**((-x))) ** (-1)

def objective_732(x, a, b, c):
    return (a+b*(np.log(x))/((x)**(2))+c/((x)**(2))) ** (-1)

def objective_733(x, a, b, c):
    return (a+b*(np.log(x))/((x)**(2))+c*(np.e)**((-x))) ** (-1)

def objective_734(x, a, b, c):
    return (a+b/((x)**(2))+c*(np.e)**((-x))) ** (-1)

def objective_735(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)

def objective_736(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))

def objective_737(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))

def objective_738(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)

def objective_739(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))

def objective_740(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)

def objective_741(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))

def objective_742(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)

def objective_743(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)/(np.log(x))

def objective_744(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)

def objective_745(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))

def objective_746(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d/(np.log(x))

def objective_747(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)**(0.5)

def objective_748(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))/(x)

def objective_749(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)

def objective_750(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)**(1.5)

def objective_751(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_752(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d/((x)**(2))

def objective_753(x, a, b, c, d):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**((-x))

def objective_754(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))

def objective_755(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))

def objective_756(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)

def objective_757(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))

def objective_758(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)

def objective_759(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))

def objective_760(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)

def objective_761(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*(x)/(np.log(x))

def objective_762(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)

def objective_763(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))

def objective_764(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d/(np.log(x))

def objective_765(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d/(x)**(0.5)

def objective_766(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))/(x)

def objective_767(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d/(x)

def objective_768(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d/(x)**(1.5)

def objective_769(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_770(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d/((x)**(2))

def objective_771(x, a, b, c, d):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**((-x))

def objective_772(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))

def objective_773(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)

def objective_774(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))

def objective_775(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)

def objective_776(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))

def objective_777(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)

def objective_778(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*(x)/(np.log(x))

def objective_779(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)

def objective_780(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))

def objective_781(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d/(np.log(x))

def objective_782(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d/(x)**(0.5)

def objective_783(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))/(x)

def objective_784(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d/(x)

def objective_785(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d/(x)**(1.5)

def objective_786(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))/((x)**(2))

def objective_787(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d/((x)**(2))

def objective_788(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**((-x))

def objective_789(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)

def objective_790(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))

def objective_791(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)

def objective_792(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))

def objective_793(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)

def objective_794(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))

def objective_795(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)

def objective_796(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))

def objective_797(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(np.log(x))

def objective_798(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)**(0.5)

def objective_799(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))/(x)

def objective_800(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)

def objective_801(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)**(1.5)

def objective_802(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_803(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/((x)**(2))

def objective_804(x, a, b, c, d):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**((-x))

def objective_805(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))

def objective_806(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)

def objective_807(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))

def objective_808(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)

def objective_809(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d*(x)/(np.log(x))

def objective_810(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)

def objective_811(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))

def objective_812(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d/(np.log(x))

def objective_813(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d/(x)**(0.5)

def objective_814(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))/(x)

def objective_815(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d/(x)

def objective_816(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d/(x)**(1.5)

def objective_817(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))/((x)**(2))

def objective_818(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d/((x)**(2))

def objective_819(x, a, b, c, d):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**((-x))

def objective_820(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)

def objective_821(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))

def objective_822(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)

def objective_823(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d*(x)/(np.log(x))

def objective_824(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)

def objective_825(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))

def objective_826(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d/(np.log(x))

def objective_827(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d/(x)**(0.5)

def objective_828(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))/(x)

def objective_829(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d/(x)

def objective_830(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d/(x)**(1.5)

def objective_831(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))/((x)**(2))

def objective_832(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d/((x)**(2))

def objective_833(x, a, b, c, d):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**((-x))

def objective_834(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))

def objective_835(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)

def objective_836(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d*(x)/(np.log(x))

def objective_837(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)

def objective_838(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))

def objective_839(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d/(np.log(x))

def objective_840(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d/(x)**(0.5)

def objective_841(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))/(x)

def objective_842(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d/(x)

def objective_843(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d/(x)**(1.5)

def objective_844(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))/((x)**(2))

def objective_845(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d/((x)**(2))

def objective_846(x, a, b, c, d):
    return a+b*(x)+c*(np.e)**(x)+d*(np.e)**((-x))

def objective_847(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)

def objective_848(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))

def objective_849(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)

def objective_850(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))

def objective_851(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))

def objective_852(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)

def objective_853(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)

def objective_854(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)

def objective_855(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(1.5)

def objective_856(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_857(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/((x)**(2))

def objective_858(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.e)**((-x))

def objective_859(x, a, b, c, d):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))

def objective_860(x, a, b, c, d):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)**(0.5)

def objective_861(x, a, b, c, d):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))

def objective_862(x, a, b, c, d):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(np.log(x))

def objective_863(x, a, b, c, d):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)**(0.5)

def objective_864(x, a, b, c, d):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))/(x)

def objective_865(x, a, b, c, d):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)

def objective_866(x, a, b, c, d):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)**(1.5)

def objective_867(x, a, b, c, d):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))/((x)**(2))

def objective_868(x, a, b, c, d):
    return a+b*(x)+c*((np.log(x)))**(2)+d/((x)**(2))

def objective_869(x, a, b, c, d):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.e)**((-x))

def objective_870(x, a, b, c, d):
    return a+b*(x)+c*(x)/(np.log(x))+d*(x)**(0.5)

def objective_871(x, a, b, c, d):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))

def objective_872(x, a, b, c, d):
    return a+b*(x)+c*(x)/(np.log(x))+d/(np.log(x))

def objective_873(x, a, b, c, d):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)**(0.5)

def objective_874(x, a, b, c, d):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))/(x)

def objective_875(x, a, b, c, d):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)

def objective_876(x, a, b, c, d):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)**(1.5)

def objective_877(x, a, b, c, d):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_878(x, a, b, c, d):
    return a+b*(x)+c*(x)/(np.log(x))+d/((x)**(2))

def objective_879(x, a, b, c, d):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.e)**((-x))

def objective_880(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))

def objective_881(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)+d/(np.log(x))

def objective_882(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)+d/(x)**(0.5)

def objective_883(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))/(x)

def objective_884(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)+d/(x)

def objective_885(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)+d/(x)**(1.5)

def objective_886(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_887(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)+d/((x)**(2))

def objective_888(x, a, b, c, d):
    return a+b*(x)+c*(x)**(0.5)+d*(np.e)**((-x))

def objective_889(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))+d/(np.log(x))

def objective_890(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))+d/(x)**(0.5)

def objective_891(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))+d*(np.log(x))/(x)

def objective_892(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))+d/(x)

def objective_893(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))+d/(x)**(1.5)

def objective_894(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_895(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))+d/((x)**(2))

def objective_896(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))+d*(np.e)**((-x))

def objective_897(x, a, b, c, d):
    return a+b*(x)+c/(np.log(x))+d/(x)**(0.5)

def objective_898(x, a, b, c, d):
    return a+b*(x)+c/(np.log(x))+d*(np.log(x))/(x)

def objective_899(x, a, b, c, d):
    return a+b*(x)+c/(np.log(x))+d/(x)

def objective_900(x, a, b, c, d):
    return a+b*(x)+c/(np.log(x))+d/(x)**(1.5)

def objective_901(x, a, b, c, d):
    return a+b*(x)+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_902(x, a, b, c, d):
    return a+b*(x)+c/(np.log(x))+d/((x)**(2))

def objective_903(x, a, b, c, d):
    return a+b*(x)+c/(np.log(x))+d*(np.e)**((-x))

def objective_904(x, a, b, c, d):
    return a+b*(x)+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_905(x, a, b, c, d):
    return a+b*(x)+c/(x)**(0.5)+d/(x)

def objective_906(x, a, b, c, d):
    return a+b*(x)+c/(x)**(0.5)+d/(x)**(1.5)

def objective_907(x, a, b, c, d):
    return a+b*(x)+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_908(x, a, b, c, d):
    return a+b*(x)+c/(x)**(0.5)+d/((x)**(2))

def objective_909(x, a, b, c, d):
    return a+b*(x)+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_910(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))/(x)+d/(x)

def objective_911(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_912(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_913(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))/(x)+d/((x)**(2))

def objective_914(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_915(x, a, b, c, d):
    return a+b*(x)+c/(x)+d/(x)**(1.5)

def objective_916(x, a, b, c, d):
    return a+b*(x)+c/(x)+d*(np.log(x))/((x)**(2))

def objective_917(x, a, b, c, d):
    return a+b*(x)+c/(x)+d/((x)**(2))

def objective_918(x, a, b, c, d):
    return a+b*(x)+c/(x)+d*(np.e)**((-x))

def objective_919(x, a, b, c, d):
    return a+b*(x)+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_920(x, a, b, c, d):
    return a+b*(x)+c/(x)**(1.5)+d/((x)**(2))

def objective_921(x, a, b, c, d):
    return a+b*(x)+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_922(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_923(x, a, b, c, d):
    return a+b*(x)+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_924(x, a, b, c, d):
    return a+b*(x)+c/((x)**(2))+d*(np.e)**((-x))

def objective_925(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*((x)**(2))

def objective_926(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))

def objective_927(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*(x)**(2.5)

def objective_928(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*((x)**(3))

def objective_929(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*(np.e)**(x)

def objective_930(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))

def objective_931(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*((np.log(x)))**(2)

def objective_932(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*(x)/(np.log(x))

def objective_933(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*(x)**(0.5)

def objective_934(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*(np.log(x))

def objective_935(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d/(np.log(x))

def objective_936(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d/(x)**(0.5)

def objective_937(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*(np.log(x))/(x)

def objective_938(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d/(x)

def objective_939(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d/(x)**(1.5)

def objective_940(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_941(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d/((x)**(2))

def objective_942(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(1.5)+d*(np.e)**((-x))

def objective_943(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*((x)**(2))*(np.log(x))

def objective_944(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*(x)**(2.5)

def objective_945(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*((x)**(3))

def objective_946(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*(np.e)**(x)

def objective_947(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))

def objective_948(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*((np.log(x)))**(2)

def objective_949(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*(x)/(np.log(x))

def objective_950(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*(x)**(0.5)

def objective_951(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*(np.log(x))

def objective_952(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d/(np.log(x))

def objective_953(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d/(x)**(0.5)

def objective_954(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*(np.log(x))/(x)

def objective_955(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d/(x)

def objective_956(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d/(x)**(1.5)

def objective_957(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*(np.log(x))/((x)**(2))

def objective_958(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d/((x)**(2))

def objective_959(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))+d*(np.e)**((-x))

def objective_960(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)

def objective_961(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d*((x)**(3))

def objective_962(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)

def objective_963(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))

def objective_964(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)

def objective_965(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))

def objective_966(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)

def objective_967(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d*(np.log(x))

def objective_968(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d/(np.log(x))

def objective_969(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d/(x)**(0.5)

def objective_970(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d*(np.log(x))/(x)

def objective_971(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d/(x)

def objective_972(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d/(x)**(1.5)

def objective_973(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_974(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d/((x)**(2))

def objective_975(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(2))*(np.log(x))+d*(np.e)**((-x))

def objective_976(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d*((x)**(3))

def objective_977(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d*(np.e)**(x)

def objective_978(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))

def objective_979(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d*((np.log(x)))**(2)

def objective_980(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d*(x)/(np.log(x))

def objective_981(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d*(x)**(0.5)

def objective_982(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d*(np.log(x))

def objective_983(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d/(np.log(x))

def objective_984(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d/(x)**(0.5)

def objective_985(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d*(np.log(x))/(x)

def objective_986(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d/(x)

def objective_987(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d/(x)**(1.5)

def objective_988(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d*(np.log(x))/((x)**(2))

def objective_989(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d/((x)**(2))

def objective_990(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(2.5)+d*(np.e)**((-x))

def objective_991(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d*(np.e)**(x)

def objective_992(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))

def objective_993(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d*((np.log(x)))**(2)

def objective_994(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d*(x)/(np.log(x))

def objective_995(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d*(x)**(0.5)

def objective_996(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d*(np.log(x))

def objective_997(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d/(np.log(x))

def objective_998(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d/(x)**(0.5)

def objective_999(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d*(np.log(x))/(x)

def objective_1000(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d/(x)

def objective_1001(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d/(x)**(1.5)

def objective_1002(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d*(np.log(x))/((x)**(2))

def objective_1003(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d/((x)**(2))

def objective_1004(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((x)**(3))+d*(np.e)**((-x))

def objective_1005(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))

def objective_1006(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d*((np.log(x)))**(2)

def objective_1007(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d*(x)/(np.log(x))

def objective_1008(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d*(x)**(0.5)

def objective_1009(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d*(np.log(x))

def objective_1010(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d/(np.log(x))

def objective_1011(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d/(x)**(0.5)

def objective_1012(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d*(np.log(x))/(x)

def objective_1013(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d/(x)

def objective_1014(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d/(x)**(1.5)

def objective_1015(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d*(np.log(x))/((x)**(2))

def objective_1016(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d/((x)**(2))

def objective_1017(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.e)**(x)+d*(np.e)**((-x))

def objective_1018(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)

def objective_1019(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))

def objective_1020(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)

def objective_1021(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))

def objective_1022(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))

def objective_1023(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)

def objective_1024(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)

def objective_1025(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d/(x)

def objective_1026(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d/(x)**(1.5)

def objective_1027(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1028(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d/((x)**(2))

def objective_1029(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(np.e)**((-x))

def objective_1030(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)+d*(x)/(np.log(x))

def objective_1031(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)+d*(x)**(0.5)

def objective_1032(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)+d*(np.log(x))

def objective_1033(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)+d/(np.log(x))

def objective_1034(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)+d/(x)**(0.5)

def objective_1035(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)+d*(np.log(x))/(x)

def objective_1036(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)+d/(x)

def objective_1037(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)+d/(x)**(1.5)

def objective_1038(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)+d*(np.log(x))/((x)**(2))

def objective_1039(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)+d/((x)**(2))

def objective_1040(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*((np.log(x)))**(2)+d*(np.e)**((-x))

def objective_1041(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)/(np.log(x))+d*(x)**(0.5)

def objective_1042(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)/(np.log(x))+d*(np.log(x))

def objective_1043(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)/(np.log(x))+d/(np.log(x))

def objective_1044(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)/(np.log(x))+d/(x)**(0.5)

def objective_1045(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)/(np.log(x))+d*(np.log(x))/(x)

def objective_1046(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)/(np.log(x))+d/(x)

def objective_1047(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)/(np.log(x))+d/(x)**(1.5)

def objective_1048(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1049(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)/(np.log(x))+d/((x)**(2))

def objective_1050(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)/(np.log(x))+d*(np.e)**((-x))

def objective_1051(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)+d*(np.log(x))

def objective_1052(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)+d/(np.log(x))

def objective_1053(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)+d/(x)**(0.5)

def objective_1054(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)+d*(np.log(x))/(x)

def objective_1055(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)+d/(x)

def objective_1056(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)+d/(x)**(1.5)

def objective_1057(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1058(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)+d/((x)**(2))

def objective_1059(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(x)**(0.5)+d*(np.e)**((-x))

def objective_1060(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))+d/(np.log(x))

def objective_1061(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))+d/(x)**(0.5)

def objective_1062(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))+d*(np.log(x))/(x)

def objective_1063(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))+d/(x)

def objective_1064(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))+d/(x)**(1.5)

def objective_1065(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1066(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))+d/((x)**(2))

def objective_1067(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))+d*(np.e)**((-x))

def objective_1068(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(np.log(x))+d/(x)**(0.5)

def objective_1069(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1070(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(np.log(x))+d/(x)

def objective_1071(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(np.log(x))+d/(x)**(1.5)

def objective_1072(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1073(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(np.log(x))+d/((x)**(2))

def objective_1074(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(np.log(x))+d*(np.e)**((-x))

def objective_1075(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1076(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)**(0.5)+d/(x)

def objective_1077(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1078(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1079(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)**(0.5)+d/((x)**(2))

def objective_1080(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1081(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))/(x)+d/(x)

def objective_1082(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1083(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1084(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1085(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1086(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)+d/(x)**(1.5)

def objective_1087(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)+d*(np.log(x))/((x)**(2))

def objective_1088(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)+d/((x)**(2))

def objective_1089(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)+d*(np.e)**((-x))

def objective_1090(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_1091(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)**(1.5)+d/((x)**(2))

def objective_1092(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_1093(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_1094(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_1095(x, a, b, c, d):
    return a+b*(x)*(np.log(x))+c/((x)**(2))+d*(np.e)**((-x))

def objective_1096(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*((x)**(2))*(np.log(x))

def objective_1097(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*(x)**(2.5)

def objective_1098(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*((x)**(3))

def objective_1099(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*(np.e)**(x)

def objective_1100(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))

def objective_1101(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*((np.log(x)))**(2)

def objective_1102(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*(x)/(np.log(x))

def objective_1103(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*(x)**(0.5)

def objective_1104(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*(np.log(x))

def objective_1105(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d/(np.log(x))

def objective_1106(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d/(x)**(0.5)

def objective_1107(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*(np.log(x))/(x)

def objective_1108(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d/(x)

def objective_1109(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d/(x)**(1.5)

def objective_1110(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*(np.log(x))/((x)**(2))

def objective_1111(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d/((x)**(2))

def objective_1112(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))+d*(np.e)**((-x))

def objective_1113(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)

def objective_1114(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d*((x)**(3))

def objective_1115(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)

def objective_1116(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))

def objective_1117(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)

def objective_1118(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))

def objective_1119(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)

def objective_1120(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d*(np.log(x))

def objective_1121(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d/(np.log(x))

def objective_1122(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d/(x)**(0.5)

def objective_1123(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d*(np.log(x))/(x)

def objective_1124(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d/(x)

def objective_1125(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d/(x)**(1.5)

def objective_1126(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1127(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d/((x)**(2))

def objective_1128(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(2))*(np.log(x))+d*(np.e)**((-x))

def objective_1129(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d*((x)**(3))

def objective_1130(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d*(np.e)**(x)

def objective_1131(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))

def objective_1132(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d*((np.log(x)))**(2)

def objective_1133(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d*(x)/(np.log(x))

def objective_1134(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d*(x)**(0.5)

def objective_1135(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d*(np.log(x))

def objective_1136(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d/(np.log(x))

def objective_1137(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d/(x)**(0.5)

def objective_1138(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d*(np.log(x))/(x)

def objective_1139(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d/(x)

def objective_1140(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d/(x)**(1.5)

def objective_1141(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d*(np.log(x))/((x)**(2))

def objective_1142(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d/((x)**(2))

def objective_1143(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(2.5)+d*(np.e)**((-x))

def objective_1144(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d*(np.e)**(x)

def objective_1145(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))

def objective_1146(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d*((np.log(x)))**(2)

def objective_1147(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d*(x)/(np.log(x))

def objective_1148(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d*(x)**(0.5)

def objective_1149(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d*(np.log(x))

def objective_1150(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d/(np.log(x))

def objective_1151(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d/(x)**(0.5)

def objective_1152(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d*(np.log(x))/(x)

def objective_1153(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d/(x)

def objective_1154(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d/(x)**(1.5)

def objective_1155(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d*(np.log(x))/((x)**(2))

def objective_1156(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d/((x)**(2))

def objective_1157(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((x)**(3))+d*(np.e)**((-x))

def objective_1158(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))

def objective_1159(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d*((np.log(x)))**(2)

def objective_1160(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d*(x)/(np.log(x))

def objective_1161(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d*(x)**(0.5)

def objective_1162(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d*(np.log(x))

def objective_1163(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d/(np.log(x))

def objective_1164(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d/(x)**(0.5)

def objective_1165(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d*(np.log(x))/(x)

def objective_1166(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d/(x)

def objective_1167(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d/(x)**(1.5)

def objective_1168(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d*(np.log(x))/((x)**(2))

def objective_1169(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d/((x)**(2))

def objective_1170(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.e)**(x)+d*(np.e)**((-x))

def objective_1171(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)

def objective_1172(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))

def objective_1173(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)

def objective_1174(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))

def objective_1175(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))

def objective_1176(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)

def objective_1177(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)

def objective_1178(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d/(x)

def objective_1179(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d/(x)**(1.5)

def objective_1180(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1181(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d/((x)**(2))

def objective_1182(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)*(np.log(x))+d*(np.e)**((-x))

def objective_1183(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))

def objective_1184(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)+d*(x)**(0.5)

def objective_1185(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)+d*(np.log(x))

def objective_1186(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)+d/(np.log(x))

def objective_1187(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)+d/(x)**(0.5)

def objective_1188(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)+d*(np.log(x))/(x)

def objective_1189(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)+d/(x)

def objective_1190(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)+d/(x)**(1.5)

def objective_1191(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)+d*(np.log(x))/((x)**(2))

def objective_1192(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)+d/((x)**(2))

def objective_1193(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*((np.log(x)))**(2)+d*(np.e)**((-x))

def objective_1194(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)/(np.log(x))+d*(x)**(0.5)

def objective_1195(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)/(np.log(x))+d*(np.log(x))

def objective_1196(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)/(np.log(x))+d/(np.log(x))

def objective_1197(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)/(np.log(x))+d/(x)**(0.5)

def objective_1198(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)/(np.log(x))+d*(np.log(x))/(x)

def objective_1199(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)/(np.log(x))+d/(x)

def objective_1200(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)/(np.log(x))+d/(x)**(1.5)

def objective_1201(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1202(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)/(np.log(x))+d/((x)**(2))

def objective_1203(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)/(np.log(x))+d*(np.e)**((-x))

def objective_1204(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)+d*(np.log(x))

def objective_1205(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)+d/(np.log(x))

def objective_1206(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)+d/(x)**(0.5)

def objective_1207(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)+d*(np.log(x))/(x)

def objective_1208(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)+d/(x)

def objective_1209(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)+d/(x)**(1.5)

def objective_1210(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1211(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)+d/((x)**(2))

def objective_1212(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(x)**(0.5)+d*(np.e)**((-x))

def objective_1213(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))+d/(np.log(x))

def objective_1214(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))+d/(x)**(0.5)

def objective_1215(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))+d*(np.log(x))/(x)

def objective_1216(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))+d/(x)

def objective_1217(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))+d/(x)**(1.5)

def objective_1218(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1219(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))+d/((x)**(2))

def objective_1220(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))+d*(np.e)**((-x))

def objective_1221(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(np.log(x))+d/(x)**(0.5)

def objective_1222(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1223(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(np.log(x))+d/(x)

def objective_1224(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(np.log(x))+d/(x)**(1.5)

def objective_1225(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1226(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(np.log(x))+d/((x)**(2))

def objective_1227(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(np.log(x))+d*(np.e)**((-x))

def objective_1228(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1229(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)**(0.5)+d/(x)

def objective_1230(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1231(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1232(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)**(0.5)+d/((x)**(2))

def objective_1233(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1234(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))/(x)+d/(x)

def objective_1235(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1236(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1237(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1238(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1239(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)+d/(x)**(1.5)

def objective_1240(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)+d*(np.log(x))/((x)**(2))

def objective_1241(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)+d/((x)**(2))

def objective_1242(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)+d*(np.e)**((-x))

def objective_1243(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_1244(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)**(1.5)+d/((x)**(2))

def objective_1245(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_1246(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_1247(x, a, b, c, d):
    return a+b*(x)**(1.5)+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_1248(x, a, b, c, d):
    return a+b*(x)**(1.5)+c/((x)**(2))+d*(np.e)**((-x))

def objective_1249(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)

def objective_1250(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d*((x)**(3))

def objective_1251(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)

def objective_1252(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))

def objective_1253(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)

def objective_1254(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))

def objective_1255(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)

def objective_1256(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d*(np.log(x))

def objective_1257(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d/(np.log(x))

def objective_1258(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d/(x)**(0.5)

def objective_1259(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d*(np.log(x))/(x)

def objective_1260(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d/(x)

def objective_1261(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d/(x)**(1.5)

def objective_1262(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1263(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d/((x)**(2))

def objective_1264(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(2))*(np.log(x))+d*(np.e)**((-x))

def objective_1265(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d*((x)**(3))

def objective_1266(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d*(np.e)**(x)

def objective_1267(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))

def objective_1268(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d*((np.log(x)))**(2)

def objective_1269(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d*(x)/(np.log(x))

def objective_1270(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d*(x)**(0.5)

def objective_1271(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d*(np.log(x))

def objective_1272(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d/(np.log(x))

def objective_1273(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d/(x)**(0.5)

def objective_1274(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d*(np.log(x))/(x)

def objective_1275(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d/(x)

def objective_1276(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d/(x)**(1.5)

def objective_1277(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d*(np.log(x))/((x)**(2))

def objective_1278(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d/((x)**(2))

def objective_1279(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(2.5)+d*(np.e)**((-x))

def objective_1280(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d*(np.e)**(x)

def objective_1281(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))

def objective_1282(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d*((np.log(x)))**(2)

def objective_1283(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d*(x)/(np.log(x))

def objective_1284(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d*(x)**(0.5)

def objective_1285(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d*(np.log(x))

def objective_1286(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d/(np.log(x))

def objective_1287(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d/(x)**(0.5)

def objective_1288(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d*(np.log(x))/(x)

def objective_1289(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d/(x)

def objective_1290(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d/(x)**(1.5)

def objective_1291(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d*(np.log(x))/((x)**(2))

def objective_1292(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d/((x)**(2))

def objective_1293(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(3))+d*(np.e)**((-x))

def objective_1294(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))

def objective_1295(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d*((np.log(x)))**(2)

def objective_1296(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d*(x)/(np.log(x))

def objective_1297(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d*(x)**(0.5)

def objective_1298(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d*(np.log(x))

def objective_1299(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d/(np.log(x))

def objective_1300(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d/(x)**(0.5)

def objective_1301(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d*(np.log(x))/(x)

def objective_1302(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d/(x)

def objective_1303(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d/(x)**(1.5)

def objective_1304(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d*(np.log(x))/((x)**(2))

def objective_1305(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d/((x)**(2))

def objective_1306(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.e)**(x)+d*(np.e)**((-x))

def objective_1307(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)

def objective_1308(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))

def objective_1309(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)

def objective_1310(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))

def objective_1311(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))

def objective_1312(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)

def objective_1313(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)

def objective_1314(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d/(x)

def objective_1315(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d/(x)**(1.5)

def objective_1316(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1317(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d/((x)**(2))

def objective_1318(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)*(np.log(x))+d*(np.e)**((-x))

def objective_1319(x, a, b, c, d):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)+d*(x)/(np.log(x))

def objective_1320(x, a, b, c, d):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)+d*(x)**(0.5)

def objective_1321(x, a, b, c, d):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)+d*(np.log(x))

def objective_1322(x, a, b, c, d):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)+d/(np.log(x))

def objective_1323(x, a, b, c, d):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)+d/(x)**(0.5)

def objective_1324(x, a, b, c, d):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)+d*(np.log(x))/(x)

def objective_1325(x, a, b, c, d):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)+d/(x)

def objective_1326(x, a, b, c, d):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)+d/(x)**(1.5)

def objective_1327(x, a, b, c, d):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)+d*(np.log(x))/((x)**(2))

def objective_1328(x, a, b, c, d):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)+d/((x)**(2))

def objective_1329(x, a, b, c, d):
    return a+b*((x)**(2))+c*((np.log(x)))**(2)+d*(np.e)**((-x))

def objective_1330(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)/(np.log(x))+d*(x)**(0.5)

def objective_1331(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)/(np.log(x))+d*(np.log(x))

def objective_1332(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)/(np.log(x))+d/(np.log(x))

def objective_1333(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)/(np.log(x))+d/(x)**(0.5)

def objective_1334(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)/(np.log(x))+d*(np.log(x))/(x)

def objective_1335(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)/(np.log(x))+d/(x)

def objective_1336(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)/(np.log(x))+d/(x)**(1.5)

def objective_1337(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1338(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)/(np.log(x))+d/((x)**(2))

def objective_1339(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)/(np.log(x))+d*(np.e)**((-x))

def objective_1340(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)+d*(np.log(x))

def objective_1341(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)+d/(np.log(x))

def objective_1342(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)+d/(x)**(0.5)

def objective_1343(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)+d*(np.log(x))/(x)

def objective_1344(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)+d/(x)

def objective_1345(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)+d/(x)**(1.5)

def objective_1346(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1347(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)+d/((x)**(2))

def objective_1348(x, a, b, c, d):
    return a+b*((x)**(2))+c*(x)**(0.5)+d*(np.e)**((-x))

def objective_1349(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))+d/(np.log(x))

def objective_1350(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))+d/(x)**(0.5)

def objective_1351(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))+d*(np.log(x))/(x)

def objective_1352(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))+d/(x)

def objective_1353(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))+d/(x)**(1.5)

def objective_1354(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1355(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))+d/((x)**(2))

def objective_1356(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))+d*(np.e)**((-x))

def objective_1357(x, a, b, c, d):
    return a+b*((x)**(2))+c/(np.log(x))+d/(x)**(0.5)

def objective_1358(x, a, b, c, d):
    return a+b*((x)**(2))+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1359(x, a, b, c, d):
    return a+b*((x)**(2))+c/(np.log(x))+d/(x)

def objective_1360(x, a, b, c, d):
    return a+b*((x)**(2))+c/(np.log(x))+d/(x)**(1.5)

def objective_1361(x, a, b, c, d):
    return a+b*((x)**(2))+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1362(x, a, b, c, d):
    return a+b*((x)**(2))+c/(np.log(x))+d/((x)**(2))

def objective_1363(x, a, b, c, d):
    return a+b*((x)**(2))+c/(np.log(x))+d*(np.e)**((-x))

def objective_1364(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1365(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)**(0.5)+d/(x)

def objective_1366(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1367(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1368(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)**(0.5)+d/((x)**(2))

def objective_1369(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1370(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))/(x)+d/(x)

def objective_1371(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1372(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1373(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1374(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1375(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)+d/(x)**(1.5)

def objective_1376(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)+d*(np.log(x))/((x)**(2))

def objective_1377(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)+d/((x)**(2))

def objective_1378(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)+d*(np.e)**((-x))

def objective_1379(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_1380(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)**(1.5)+d/((x)**(2))

def objective_1381(x, a, b, c, d):
    return a+b*((x)**(2))+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_1382(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_1383(x, a, b, c, d):
    return a+b*((x)**(2))+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_1384(x, a, b, c, d):
    return a+b*((x)**(2))+c/((x)**(2))+d*(np.e)**((-x))

def objective_1385(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d*((x)**(3))

def objective_1386(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d*(np.e)**(x)

def objective_1387(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))

def objective_1388(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d*((np.log(x)))**(2)

def objective_1389(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d*(x)/(np.log(x))

def objective_1390(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d*(x)**(0.5)

def objective_1391(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d*(np.log(x))

def objective_1392(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d/(np.log(x))

def objective_1393(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d/(x)**(0.5)

def objective_1394(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d*(np.log(x))/(x)

def objective_1395(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d/(x)

def objective_1396(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d/(x)**(1.5)

def objective_1397(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d*(np.log(x))/((x)**(2))

def objective_1398(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d/((x)**(2))

def objective_1399(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(2.5)+d*(np.e)**((-x))

def objective_1400(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d*(np.e)**(x)

def objective_1401(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))

def objective_1402(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d*((np.log(x)))**(2)

def objective_1403(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d*(x)/(np.log(x))

def objective_1404(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d*(x)**(0.5)

def objective_1405(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d*(np.log(x))

def objective_1406(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d/(np.log(x))

def objective_1407(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d/(x)**(0.5)

def objective_1408(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d*(np.log(x))/(x)

def objective_1409(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d/(x)

def objective_1410(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d/(x)**(1.5)

def objective_1411(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d*(np.log(x))/((x)**(2))

def objective_1412(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d/((x)**(2))

def objective_1413(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((x)**(3))+d*(np.e)**((-x))

def objective_1414(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))

def objective_1415(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d*((np.log(x)))**(2)

def objective_1416(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d*(x)/(np.log(x))

def objective_1417(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d*(x)**(0.5)

def objective_1418(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d*(np.log(x))

def objective_1419(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d/(np.log(x))

def objective_1420(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d/(x)**(0.5)

def objective_1421(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d*(np.log(x))/(x)

def objective_1422(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d/(x)

def objective_1423(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d/(x)**(1.5)

def objective_1424(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d*(np.log(x))/((x)**(2))

def objective_1425(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d/((x)**(2))

def objective_1426(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.e)**(x)+d*(np.e)**((-x))

def objective_1427(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)

def objective_1428(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))

def objective_1429(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)

def objective_1430(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))

def objective_1431(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))

def objective_1432(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)

def objective_1433(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)

def objective_1434(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d/(x)

def objective_1435(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d/(x)**(1.5)

def objective_1436(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1437(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d/((x)**(2))

def objective_1438(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)*(np.log(x))+d*(np.e)**((-x))

def objective_1439(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)+d*(x)/(np.log(x))

def objective_1440(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)+d*(x)**(0.5)

def objective_1441(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)+d*(np.log(x))

def objective_1442(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)+d/(np.log(x))

def objective_1443(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)+d/(x)**(0.5)

def objective_1444(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)+d*(np.log(x))/(x)

def objective_1445(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)+d/(x)

def objective_1446(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)+d/(x)**(1.5)

def objective_1447(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)+d*(np.log(x))/((x)**(2))

def objective_1448(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)+d/((x)**(2))

def objective_1449(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*((np.log(x)))**(2)+d*(np.e)**((-x))

def objective_1450(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))+d*(x)**(0.5)

def objective_1451(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))+d*(np.log(x))

def objective_1452(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))+d/(np.log(x))

def objective_1453(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))+d/(x)**(0.5)

def objective_1454(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))+d*(np.log(x))/(x)

def objective_1455(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))+d/(x)

def objective_1456(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))+d/(x)**(1.5)

def objective_1457(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1458(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))+d/((x)**(2))

def objective_1459(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)/(np.log(x))+d*(np.e)**((-x))

def objective_1460(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)+d*(np.log(x))

def objective_1461(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)+d/(np.log(x))

def objective_1462(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)+d/(x)**(0.5)

def objective_1463(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)+d*(np.log(x))/(x)

def objective_1464(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)+d/(x)

def objective_1465(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)+d/(x)**(1.5)

def objective_1466(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1467(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)+d/((x)**(2))

def objective_1468(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(x)**(0.5)+d*(np.e)**((-x))

def objective_1469(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))+d/(np.log(x))

def objective_1470(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))+d/(x)**(0.5)

def objective_1471(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))+d*(np.log(x))/(x)

def objective_1472(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))+d/(x)

def objective_1473(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))+d/(x)**(1.5)

def objective_1474(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1475(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))+d/((x)**(2))

def objective_1476(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))+d*(np.e)**((-x))

def objective_1477(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(np.log(x))+d/(x)**(0.5)

def objective_1478(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1479(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(np.log(x))+d/(x)

def objective_1480(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(np.log(x))+d/(x)**(1.5)

def objective_1481(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1482(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(np.log(x))+d/((x)**(2))

def objective_1483(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(np.log(x))+d*(np.e)**((-x))

def objective_1484(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1485(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)**(0.5)+d/(x)

def objective_1486(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1487(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1488(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)**(0.5)+d/((x)**(2))

def objective_1489(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1490(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/(x)+d/(x)

def objective_1491(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1492(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1493(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1494(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1495(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)+d/(x)**(1.5)

def objective_1496(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)+d*(np.log(x))/((x)**(2))

def objective_1497(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)+d/((x)**(2))

def objective_1498(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)+d*(np.e)**((-x))

def objective_1499(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_1500(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)**(1.5)+d/((x)**(2))

def objective_1501(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_1502(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_1503(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_1504(x, a, b, c, d):
    return a+b*((x)**(2))*(np.log(x))+c/((x)**(2))+d*(np.e)**((-x))

def objective_1505(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d*(np.e)**(x)

def objective_1506(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))

def objective_1507(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d*((np.log(x)))**(2)

def objective_1508(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d*(x)/(np.log(x))

def objective_1509(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d*(x)**(0.5)

def objective_1510(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d*(np.log(x))

def objective_1511(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d/(np.log(x))

def objective_1512(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d/(x)**(0.5)

def objective_1513(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d*(np.log(x))/(x)

def objective_1514(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d/(x)

def objective_1515(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d/(x)**(1.5)

def objective_1516(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d*(np.log(x))/((x)**(2))

def objective_1517(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d/((x)**(2))

def objective_1518(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((x)**(3))+d*(np.e)**((-x))

def objective_1519(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))

def objective_1520(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d*((np.log(x)))**(2)

def objective_1521(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d*(x)/(np.log(x))

def objective_1522(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d*(x)**(0.5)

def objective_1523(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d*(np.log(x))

def objective_1524(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d/(np.log(x))

def objective_1525(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d/(x)**(0.5)

def objective_1526(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d*(np.log(x))/(x)

def objective_1527(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d/(x)

def objective_1528(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d/(x)**(1.5)

def objective_1529(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d*(np.log(x))/((x)**(2))

def objective_1530(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d/((x)**(2))

def objective_1531(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.e)**(x)+d*(np.e)**((-x))

def objective_1532(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)

def objective_1533(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))

def objective_1534(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)

def objective_1535(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))

def objective_1536(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))

def objective_1537(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)

def objective_1538(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)

def objective_1539(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d/(x)

def objective_1540(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d/(x)**(1.5)

def objective_1541(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1542(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d/((x)**(2))

def objective_1543(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)*(np.log(x))+d*(np.e)**((-x))

def objective_1544(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))

def objective_1545(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)+d*(x)**(0.5)

def objective_1546(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)+d*(np.log(x))

def objective_1547(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)+d/(np.log(x))

def objective_1548(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)+d/(x)**(0.5)

def objective_1549(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)+d*(np.log(x))/(x)

def objective_1550(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)+d/(x)

def objective_1551(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)+d/(x)**(1.5)

def objective_1552(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)+d*(np.log(x))/((x)**(2))

def objective_1553(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)+d/((x)**(2))

def objective_1554(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*((np.log(x)))**(2)+d*(np.e)**((-x))

def objective_1555(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)/(np.log(x))+d*(x)**(0.5)

def objective_1556(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)/(np.log(x))+d*(np.log(x))

def objective_1557(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)/(np.log(x))+d/(np.log(x))

def objective_1558(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)/(np.log(x))+d/(x)**(0.5)

def objective_1559(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)/(np.log(x))+d*(np.log(x))/(x)

def objective_1560(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)/(np.log(x))+d/(x)

def objective_1561(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)/(np.log(x))+d/(x)**(1.5)

def objective_1562(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1563(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)/(np.log(x))+d/((x)**(2))

def objective_1564(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)/(np.log(x))+d*(np.e)**((-x))

def objective_1565(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)+d*(np.log(x))

def objective_1566(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)+d/(np.log(x))

def objective_1567(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)+d/(x)**(0.5)

def objective_1568(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)+d*(np.log(x))/(x)

def objective_1569(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)+d/(x)

def objective_1570(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)+d/(x)**(1.5)

def objective_1571(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1572(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)+d/((x)**(2))

def objective_1573(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(x)**(0.5)+d*(np.e)**((-x))

def objective_1574(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))+d/(np.log(x))

def objective_1575(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))+d/(x)**(0.5)

def objective_1576(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))+d*(np.log(x))/(x)

def objective_1577(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))+d/(x)

def objective_1578(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))+d/(x)**(1.5)

def objective_1579(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1580(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))+d/((x)**(2))

def objective_1581(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))+d*(np.e)**((-x))

def objective_1582(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(np.log(x))+d/(x)**(0.5)

def objective_1583(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1584(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(np.log(x))+d/(x)

def objective_1585(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(np.log(x))+d/(x)**(1.5)

def objective_1586(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1587(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(np.log(x))+d/((x)**(2))

def objective_1588(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(np.log(x))+d*(np.e)**((-x))

def objective_1589(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1590(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)**(0.5)+d/(x)

def objective_1591(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1592(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1593(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)**(0.5)+d/((x)**(2))

def objective_1594(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1595(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))/(x)+d/(x)

def objective_1596(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1597(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1598(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1599(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1600(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)+d/(x)**(1.5)

def objective_1601(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)+d*(np.log(x))/((x)**(2))

def objective_1602(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)+d/((x)**(2))

def objective_1603(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)+d*(np.e)**((-x))

def objective_1604(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_1605(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)**(1.5)+d/((x)**(2))

def objective_1606(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_1607(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_1608(x, a, b, c, d):
    return a+b*(x)**(2.5)+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_1609(x, a, b, c, d):
    return a+b*(x)**(2.5)+c/((x)**(2))+d*(np.e)**((-x))

def objective_1610(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))

def objective_1611(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d*((np.log(x)))**(2)

def objective_1612(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d*(x)/(np.log(x))

def objective_1613(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d*(x)**(0.5)

def objective_1614(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d*(np.log(x))

def objective_1615(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d/(np.log(x))

def objective_1616(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d/(x)**(0.5)

def objective_1617(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d*(np.log(x))/(x)

def objective_1618(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d/(x)

def objective_1619(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d/(x)**(1.5)

def objective_1620(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d*(np.log(x))/((x)**(2))

def objective_1621(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d/((x)**(2))

def objective_1622(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.e)**(x)+d*(np.e)**((-x))

def objective_1623(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)

def objective_1624(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))

def objective_1625(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)

def objective_1626(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))

def objective_1627(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))

def objective_1628(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)

def objective_1629(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)

def objective_1630(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d/(x)

def objective_1631(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d/(x)**(1.5)

def objective_1632(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1633(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d/((x)**(2))

def objective_1634(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)*(np.log(x))+d*(np.e)**((-x))

def objective_1635(x, a, b, c, d):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)+d*(x)/(np.log(x))

def objective_1636(x, a, b, c, d):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)+d*(x)**(0.5)

def objective_1637(x, a, b, c, d):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)+d*(np.log(x))

def objective_1638(x, a, b, c, d):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)+d/(np.log(x))

def objective_1639(x, a, b, c, d):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)+d/(x)**(0.5)

def objective_1640(x, a, b, c, d):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)+d*(np.log(x))/(x)

def objective_1641(x, a, b, c, d):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)+d/(x)

def objective_1642(x, a, b, c, d):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)+d/(x)**(1.5)

def objective_1643(x, a, b, c, d):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)+d*(np.log(x))/((x)**(2))

def objective_1644(x, a, b, c, d):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)+d/((x)**(2))

def objective_1645(x, a, b, c, d):
    return a+b*((x)**(3))+c*((np.log(x)))**(2)+d*(np.e)**((-x))

def objective_1646(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)/(np.log(x))+d*(x)**(0.5)

def objective_1647(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)/(np.log(x))+d*(np.log(x))

def objective_1648(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)/(np.log(x))+d/(np.log(x))

def objective_1649(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)/(np.log(x))+d/(x)**(0.5)

def objective_1650(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)/(np.log(x))+d*(np.log(x))/(x)

def objective_1651(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)/(np.log(x))+d/(x)

def objective_1652(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)/(np.log(x))+d/(x)**(1.5)

def objective_1653(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1654(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)/(np.log(x))+d/((x)**(2))

def objective_1655(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)/(np.log(x))+d*(np.e)**((-x))

def objective_1656(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)+d*(np.log(x))

def objective_1657(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)+d/(np.log(x))

def objective_1658(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)+d/(x)**(0.5)

def objective_1659(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)+d*(np.log(x))/(x)

def objective_1660(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)+d/(x)

def objective_1661(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)+d/(x)**(1.5)

def objective_1662(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1663(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)+d/((x)**(2))

def objective_1664(x, a, b, c, d):
    return a+b*((x)**(3))+c*(x)**(0.5)+d*(np.e)**((-x))

def objective_1665(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))+d/(np.log(x))

def objective_1666(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))+d/(x)**(0.5)

def objective_1667(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))+d*(np.log(x))/(x)

def objective_1668(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))+d/(x)

def objective_1669(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))+d/(x)**(1.5)

def objective_1670(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1671(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))+d/((x)**(2))

def objective_1672(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))+d*(np.e)**((-x))

def objective_1673(x, a, b, c, d):
    return a+b*((x)**(3))+c/(np.log(x))+d/(x)**(0.5)

def objective_1674(x, a, b, c, d):
    return a+b*((x)**(3))+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1675(x, a, b, c, d):
    return a+b*((x)**(3))+c/(np.log(x))+d/(x)

def objective_1676(x, a, b, c, d):
    return a+b*((x)**(3))+c/(np.log(x))+d/(x)**(1.5)

def objective_1677(x, a, b, c, d):
    return a+b*((x)**(3))+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1678(x, a, b, c, d):
    return a+b*((x)**(3))+c/(np.log(x))+d/((x)**(2))

def objective_1679(x, a, b, c, d):
    return a+b*((x)**(3))+c/(np.log(x))+d*(np.e)**((-x))

def objective_1680(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1681(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)**(0.5)+d/(x)

def objective_1682(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1683(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1684(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)**(0.5)+d/((x)**(2))

def objective_1685(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1686(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))/(x)+d/(x)

def objective_1687(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1688(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1689(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1690(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1691(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)+d/(x)**(1.5)

def objective_1692(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)+d*(np.log(x))/((x)**(2))

def objective_1693(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)+d/((x)**(2))

def objective_1694(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)+d*(np.e)**((-x))

def objective_1695(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_1696(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)**(1.5)+d/((x)**(2))

def objective_1697(x, a, b, c, d):
    return a+b*((x)**(3))+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_1698(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_1699(x, a, b, c, d):
    return a+b*((x)**(3))+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_1700(x, a, b, c, d):
    return a+b*((x)**(3))+c/((x)**(2))+d*(np.e)**((-x))

def objective_1701(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)

def objective_1702(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))

def objective_1703(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)

def objective_1704(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))

def objective_1705(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))

def objective_1706(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)

def objective_1707(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)

def objective_1708(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d/(x)

def objective_1709(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(1.5)

def objective_1710(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1711(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d/((x)**(2))

def objective_1712(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)*(np.log(x))+d*(np.e)**((-x))

def objective_1713(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))

def objective_1714(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)+d*(x)**(0.5)

def objective_1715(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)+d*(np.log(x))

def objective_1716(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)+d/(np.log(x))

def objective_1717(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)+d/(x)**(0.5)

def objective_1718(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)+d*(np.log(x))/(x)

def objective_1719(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)+d/(x)

def objective_1720(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)+d/(x)**(1.5)

def objective_1721(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)+d*(np.log(x))/((x)**(2))

def objective_1722(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)+d/((x)**(2))

def objective_1723(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*((np.log(x)))**(2)+d*(np.e)**((-x))

def objective_1724(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)/(np.log(x))+d*(x)**(0.5)

def objective_1725(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)/(np.log(x))+d*(np.log(x))

def objective_1726(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)/(np.log(x))+d/(np.log(x))

def objective_1727(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)/(np.log(x))+d/(x)**(0.5)

def objective_1728(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)/(np.log(x))+d*(np.log(x))/(x)

def objective_1729(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)/(np.log(x))+d/(x)

def objective_1730(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)/(np.log(x))+d/(x)**(1.5)

def objective_1731(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1732(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)/(np.log(x))+d/((x)**(2))

def objective_1733(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)/(np.log(x))+d*(np.e)**((-x))

def objective_1734(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)+d*(np.log(x))

def objective_1735(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)+d/(np.log(x))

def objective_1736(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)+d/(x)**(0.5)

def objective_1737(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)+d*(np.log(x))/(x)

def objective_1738(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)+d/(x)

def objective_1739(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)+d/(x)**(1.5)

def objective_1740(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1741(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)+d/((x)**(2))

def objective_1742(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(x)**(0.5)+d*(np.e)**((-x))

def objective_1743(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))+d/(np.log(x))

def objective_1744(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))+d/(x)**(0.5)

def objective_1745(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))+d*(np.log(x))/(x)

def objective_1746(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))+d/(x)

def objective_1747(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))+d/(x)**(1.5)

def objective_1748(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1749(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))+d/((x)**(2))

def objective_1750(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))+d*(np.e)**((-x))

def objective_1751(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(np.log(x))+d/(x)**(0.5)

def objective_1752(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1753(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(np.log(x))+d/(x)

def objective_1754(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(np.log(x))+d/(x)**(1.5)

def objective_1755(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1756(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(np.log(x))+d/((x)**(2))

def objective_1757(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(np.log(x))+d*(np.e)**((-x))

def objective_1758(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1759(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)**(0.5)+d/(x)

def objective_1760(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1761(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1762(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)**(0.5)+d/((x)**(2))

def objective_1763(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1764(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))/(x)+d/(x)

def objective_1765(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1766(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1767(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1768(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1769(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)+d/(x)**(1.5)

def objective_1770(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)+d*(np.log(x))/((x)**(2))

def objective_1771(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)+d/((x)**(2))

def objective_1772(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)+d*(np.e)**((-x))

def objective_1773(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_1774(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)**(1.5)+d/((x)**(2))

def objective_1775(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_1776(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_1777(x, a, b, c, d):
    return a+b*(np.e)**(x)+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_1778(x, a, b, c, d):
    return a+b*(np.e)**(x)+c/((x)**(2))+d*(np.e)**((-x))

def objective_1779(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)+d*(x)/(np.log(x))

def objective_1780(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)+d*(x)**(0.5)

def objective_1781(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)+d*(np.log(x))

def objective_1782(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)+d/(np.log(x))

def objective_1783(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)+d/(x)**(0.5)

def objective_1784(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)+d*(np.log(x))/(x)

def objective_1785(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)+d/(x)

def objective_1786(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)+d/(x)**(1.5)

def objective_1787(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)+d*(np.log(x))/((x)**(2))

def objective_1788(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)+d/((x)**(2))

def objective_1789(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*((np.log(x)))**(2)+d*(np.e)**((-x))

def objective_1790(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))+d*(x)**(0.5)

def objective_1791(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))+d*(np.log(x))

def objective_1792(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))+d/(np.log(x))

def objective_1793(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))+d/(x)**(0.5)

def objective_1794(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))+d*(np.log(x))/(x)

def objective_1795(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))+d/(x)

def objective_1796(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))+d/(x)**(1.5)

def objective_1797(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1798(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))+d/((x)**(2))

def objective_1799(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)/(np.log(x))+d*(np.e)**((-x))

def objective_1800(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5)+d*(np.log(x))

def objective_1801(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5)+d/(np.log(x))

def objective_1802(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5)+d/(x)**(0.5)

def objective_1803(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5)+d*(np.log(x))/(x)

def objective_1804(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5)+d/(x)

def objective_1805(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5)+d/(x)**(1.5)

def objective_1806(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1807(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5)+d/((x)**(2))

def objective_1808(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(x)**(0.5)+d*(np.e)**((-x))

def objective_1809(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))+d/(np.log(x))

def objective_1810(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))+d/(x)**(0.5)

def objective_1811(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))+d*(np.log(x))/(x)

def objective_1812(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))+d/(x)

def objective_1813(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))+d/(x)**(1.5)

def objective_1814(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1815(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))+d/((x)**(2))

def objective_1816(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))+d*(np.e)**((-x))

def objective_1817(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(np.log(x))+d/(x)**(0.5)

def objective_1818(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1819(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(np.log(x))+d/(x)

def objective_1820(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(np.log(x))+d/(x)**(1.5)

def objective_1821(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1822(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(np.log(x))+d/((x)**(2))

def objective_1823(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(np.log(x))+d*(np.e)**((-x))

def objective_1824(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1825(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)**(0.5)+d/(x)

def objective_1826(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1827(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1828(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)**(0.5)+d/((x)**(2))

def objective_1829(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1830(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/(x)+d/(x)

def objective_1831(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1832(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1833(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1834(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1835(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)+d/(x)**(1.5)

def objective_1836(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)+d*(np.log(x))/((x)**(2))

def objective_1837(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)+d/((x)**(2))

def objective_1838(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)+d*(np.e)**((-x))

def objective_1839(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_1840(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)**(1.5)+d/((x)**(2))

def objective_1841(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_1842(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_1843(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_1844(x, a, b, c, d):
    return a+b*(x)**(0.5)*(np.log(x))+c/((x)**(2))+d*(np.e)**((-x))

def objective_1845(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))+d*(x)**(0.5)

def objective_1846(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))+d*(np.log(x))

def objective_1847(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))+d/(np.log(x))

def objective_1848(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))+d/(x)**(0.5)

def objective_1849(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))+d*(np.log(x))/(x)

def objective_1850(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))+d/(x)

def objective_1851(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))+d/(x)**(1.5)

def objective_1852(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1853(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))+d/((x)**(2))

def objective_1854(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)/(np.log(x))+d*(np.e)**((-x))

def objective_1855(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)**(0.5)+d*(np.log(x))

def objective_1856(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)**(0.5)+d/(np.log(x))

def objective_1857(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)**(0.5)+d/(x)**(0.5)

def objective_1858(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)**(0.5)+d*(np.log(x))/(x)

def objective_1859(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)**(0.5)+d/(x)

def objective_1860(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)**(0.5)+d/(x)**(1.5)

def objective_1861(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1862(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)**(0.5)+d/((x)**(2))

def objective_1863(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(x)**(0.5)+d*(np.e)**((-x))

def objective_1864(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))+d/(np.log(x))

def objective_1865(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))+d/(x)**(0.5)

def objective_1866(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))+d*(np.log(x))/(x)

def objective_1867(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))+d/(x)

def objective_1868(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))+d/(x)**(1.5)

def objective_1869(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1870(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))+d/((x)**(2))

def objective_1871(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))+d*(np.e)**((-x))

def objective_1872(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(np.log(x))+d/(x)**(0.5)

def objective_1873(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1874(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(np.log(x))+d/(x)

def objective_1875(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(np.log(x))+d/(x)**(1.5)

def objective_1876(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1877(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(np.log(x))+d/((x)**(2))

def objective_1878(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(np.log(x))+d*(np.e)**((-x))

def objective_1879(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1880(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)**(0.5)+d/(x)

def objective_1881(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1882(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1883(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)**(0.5)+d/((x)**(2))

def objective_1884(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1885(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))/(x)+d/(x)

def objective_1886(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1887(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1888(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1889(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1890(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)+d/(x)**(1.5)

def objective_1891(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)+d*(np.log(x))/((x)**(2))

def objective_1892(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)+d/((x)**(2))

def objective_1893(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)+d*(np.e)**((-x))

def objective_1894(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_1895(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)**(1.5)+d/((x)**(2))

def objective_1896(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_1897(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_1898(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_1899(x, a, b, c, d):
    return a+b*((np.log(x)))**(2)+c/((x)**(2))+d*(np.e)**((-x))

def objective_1900(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(x)**(0.5)+d*(np.log(x))

def objective_1901(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(x)**(0.5)+d/(np.log(x))

def objective_1902(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(x)**(0.5)+d/(x)**(0.5)

def objective_1903(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(x)**(0.5)+d*(np.log(x))/(x)

def objective_1904(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(x)**(0.5)+d/(x)

def objective_1905(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(x)**(0.5)+d/(x)**(1.5)

def objective_1906(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1907(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(x)**(0.5)+d/((x)**(2))

def objective_1908(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(x)**(0.5)+d*(np.e)**((-x))

def objective_1909(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))+d/(np.log(x))

def objective_1910(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))+d/(x)**(0.5)

def objective_1911(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))+d*(np.log(x))/(x)

def objective_1912(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))+d/(x)

def objective_1913(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))+d/(x)**(1.5)

def objective_1914(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1915(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))+d/((x)**(2))

def objective_1916(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))+d*(np.e)**((-x))

def objective_1917(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(np.log(x))+d/(x)**(0.5)

def objective_1918(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1919(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(np.log(x))+d/(x)

def objective_1920(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(np.log(x))+d/(x)**(1.5)

def objective_1921(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1922(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(np.log(x))+d/((x)**(2))

def objective_1923(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(np.log(x))+d*(np.e)**((-x))

def objective_1924(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1925(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)**(0.5)+d/(x)

def objective_1926(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1927(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1928(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)**(0.5)+d/((x)**(2))

def objective_1929(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1930(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))/(x)+d/(x)

def objective_1931(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1932(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1933(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1934(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1935(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)+d/(x)**(1.5)

def objective_1936(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)+d*(np.log(x))/((x)**(2))

def objective_1937(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)+d/((x)**(2))

def objective_1938(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)+d*(np.e)**((-x))

def objective_1939(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_1940(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)**(1.5)+d/((x)**(2))

def objective_1941(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_1942(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_1943(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_1944(x, a, b, c, d):
    return a+b*(x)/(np.log(x))+c/((x)**(2))+d*(np.e)**((-x))

def objective_1945(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))+d/(np.log(x))

def objective_1946(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))+d/(x)**(0.5)

def objective_1947(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))+d*(np.log(x))/(x)

def objective_1948(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))+d/(x)

def objective_1949(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))+d/(x)**(1.5)

def objective_1950(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1951(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))+d/((x)**(2))

def objective_1952(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))+d*(np.e)**((-x))

def objective_1953(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(np.log(x))+d/(x)**(0.5)

def objective_1954(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1955(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(np.log(x))+d/(x)

def objective_1956(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(np.log(x))+d/(x)**(1.5)

def objective_1957(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1958(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(np.log(x))+d/((x)**(2))

def objective_1959(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(np.log(x))+d*(np.e)**((-x))

def objective_1960(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1961(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)**(0.5)+d/(x)

def objective_1962(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1963(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1964(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)**(0.5)+d/((x)**(2))

def objective_1965(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1966(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))/(x)+d/(x)

def objective_1967(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1968(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1969(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1970(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1971(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)+d/(x)**(1.5)

def objective_1972(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)+d*(np.log(x))/((x)**(2))

def objective_1973(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)+d/((x)**(2))

def objective_1974(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)+d*(np.e)**((-x))

def objective_1975(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_1976(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)**(1.5)+d/((x)**(2))

def objective_1977(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_1978(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_1979(x, a, b, c, d):
    return a+b*(x)**(0.5)+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_1980(x, a, b, c, d):
    return a+b*(x)**(0.5)+c/((x)**(2))+d*(np.e)**((-x))

def objective_1981(x, a, b, c, d):
    return a+b*(np.log(x))+c/(np.log(x))+d/(x)**(0.5)

def objective_1982(x, a, b, c, d):
    return a+b*(np.log(x))+c/(np.log(x))+d*(np.log(x))/(x)

def objective_1983(x, a, b, c, d):
    return a+b*(np.log(x))+c/(np.log(x))+d/(x)

def objective_1984(x, a, b, c, d):
    return a+b*(np.log(x))+c/(np.log(x))+d/(x)**(1.5)

def objective_1985(x, a, b, c, d):
    return a+b*(np.log(x))+c/(np.log(x))+d*(np.log(x))/((x)**(2))

def objective_1986(x, a, b, c, d):
    return a+b*(np.log(x))+c/(np.log(x))+d/((x)**(2))

def objective_1987(x, a, b, c, d):
    return a+b*(np.log(x))+c/(np.log(x))+d*(np.e)**((-x))

def objective_1988(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_1989(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)**(0.5)+d/(x)

def objective_1990(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)**(0.5)+d/(x)**(1.5)

def objective_1991(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_1992(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)**(0.5)+d/((x)**(2))

def objective_1993(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_1994(x, a, b, c, d):
    return a+b*(np.log(x))+c*(np.log(x))/(x)+d/(x)

def objective_1995(x, a, b, c, d):
    return a+b*(np.log(x))+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_1996(x, a, b, c, d):
    return a+b*(np.log(x))+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_1997(x, a, b, c, d):
    return a+b*(np.log(x))+c*(np.log(x))/(x)+d/((x)**(2))

def objective_1998(x, a, b, c, d):
    return a+b*(np.log(x))+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_1999(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)+d/(x)**(1.5)

def objective_2000(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)+d*(np.log(x))/((x)**(2))

def objective_2001(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)+d/((x)**(2))

def objective_2002(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)+d*(np.e)**((-x))

def objective_2003(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_2004(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)**(1.5)+d/((x)**(2))

def objective_2005(x, a, b, c, d):
    return a+b*(np.log(x))+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_2006(x, a, b, c, d):
    return a+b*(np.log(x))+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_2007(x, a, b, c, d):
    return a+b*(np.log(x))+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_2008(x, a, b, c, d):
    return a+b*(np.log(x))+c/((x)**(2))+d*(np.e)**((-x))

def objective_2009(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/(x)

def objective_2010(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)**(0.5)+d/(x)

def objective_2011(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)**(0.5)+d/(x)**(1.5)

def objective_2012(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))

def objective_2013(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)**(0.5)+d/((x)**(2))

def objective_2014(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)**(0.5)+d*(np.e)**((-x))

def objective_2015(x, a, b, c, d):
    return a+b/(np.log(x))+c*(np.log(x))/(x)+d/(x)

def objective_2016(x, a, b, c, d):
    return a+b/(np.log(x))+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_2017(x, a, b, c, d):
    return a+b/(np.log(x))+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_2018(x, a, b, c, d):
    return a+b/(np.log(x))+c*(np.log(x))/(x)+d/((x)**(2))

def objective_2019(x, a, b, c, d):
    return a+b/(np.log(x))+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_2020(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)+d/(x)**(1.5)

def objective_2021(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)+d*(np.log(x))/((x)**(2))

def objective_2022(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)+d/((x)**(2))

def objective_2023(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)+d*(np.e)**((-x))

def objective_2024(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_2025(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)**(1.5)+d/((x)**(2))

def objective_2026(x, a, b, c, d):
    return a+b/(np.log(x))+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_2027(x, a, b, c, d):
    return a+b/(np.log(x))+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_2028(x, a, b, c, d):
    return a+b/(np.log(x))+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_2029(x, a, b, c, d):
    return a+b/(np.log(x))+c/((x)**(2))+d*(np.e)**((-x))

def objective_2030(x, a, b, c, d):
    return a+b/(x)**(0.5)+c*(np.log(x))/(x)+d/(x)

def objective_2031(x, a, b, c, d):
    return a+b/(x)**(0.5)+c*(np.log(x))/(x)+d/(x)**(1.5)

def objective_2032(x, a, b, c, d):
    return a+b/(x)**(0.5)+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))

def objective_2033(x, a, b, c, d):
    return a+b/(x)**(0.5)+c*(np.log(x))/(x)+d/((x)**(2))

def objective_2034(x, a, b, c, d):
    return a+b/(x)**(0.5)+c*(np.log(x))/(x)+d*(np.e)**((-x))

def objective_2035(x, a, b, c, d):
    return a+b/(x)**(0.5)+c/(x)+d/(x)**(1.5)

def objective_2036(x, a, b, c, d):
    return a+b/(x)**(0.5)+c/(x)+d*(np.log(x))/((x)**(2))

def objective_2037(x, a, b, c, d):
    return a+b/(x)**(0.5)+c/(x)+d/((x)**(2))

def objective_2038(x, a, b, c, d):
    return a+b/(x)**(0.5)+c/(x)+d*(np.e)**((-x))

def objective_2039(x, a, b, c, d):
    return a+b/(x)**(0.5)+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_2040(x, a, b, c, d):
    return a+b/(x)**(0.5)+c/(x)**(1.5)+d/((x)**(2))

def objective_2041(x, a, b, c, d):
    return a+b/(x)**(0.5)+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_2042(x, a, b, c, d):
    return a+b/(x)**(0.5)+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_2043(x, a, b, c, d):
    return a+b/(x)**(0.5)+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_2044(x, a, b, c, d):
    return a+b/(x)**(0.5)+c/((x)**(2))+d*(np.e)**((-x))

def objective_2045(x, a, b, c, d):
    return a+b*(np.log(x))/(x)+c/(x)+d/(x)**(1.5)

def objective_2046(x, a, b, c, d):
    return a+b*(np.log(x))/(x)+c/(x)+d*(np.log(x))/((x)**(2))

def objective_2047(x, a, b, c, d):
    return a+b*(np.log(x))/(x)+c/(x)+d/((x)**(2))

def objective_2048(x, a, b, c, d):
    return a+b*(np.log(x))/(x)+c/(x)+d*(np.e)**((-x))

def objective_2049(x, a, b, c, d):
    return a+b*(np.log(x))/(x)+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_2050(x, a, b, c, d):
    return a+b*(np.log(x))/(x)+c/(x)**(1.5)+d/((x)**(2))

def objective_2051(x, a, b, c, d):
    return a+b*(np.log(x))/(x)+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_2052(x, a, b, c, d):
    return a+b*(np.log(x))/(x)+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_2053(x, a, b, c, d):
    return a+b*(np.log(x))/(x)+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_2054(x, a, b, c, d):
    return a+b*(np.log(x))/(x)+c/((x)**(2))+d*(np.e)**((-x))

def objective_2055(x, a, b, c, d):
    return a+b/(x)+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))

def objective_2056(x, a, b, c, d):
    return a+b/(x)+c/(x)**(1.5)+d/((x)**(2))

def objective_2057(x, a, b, c, d):
    return a+b/(x)+c/(x)**(1.5)+d*(np.e)**((-x))

def objective_2058(x, a, b, c, d):
    return a+b/(x)+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_2059(x, a, b, c, d):
    return a+b/(x)+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_2060(x, a, b, c, d):
    return a+b/(x)+c/((x)**(2))+d*(np.e)**((-x))

def objective_2061(x, a, b, c, d):
    return a+b/(x)**(1.5)+c*(np.log(x))/((x)**(2))+d/((x)**(2))

def objective_2062(x, a, b, c, d):
    return a+b/(x)**(1.5)+c*(np.log(x))/((x)**(2))+d*(np.e)**((-x))

def objective_2063(x, a, b, c, d):
    return a+b/(x)**(1.5)+c/((x)**(2))+d*(np.e)**((-x))

def objective_2064(x, a, b, c, d):
    return a+b*(np.log(x))/((x)**(2))+c/((x)**(2))+d*(np.e)**((-x))

def objective_2065(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*((x)**(2))

def objective_2066(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*((x)**(2))*(np.log(x))

def objective_2067(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*(x)**(2.5)

def objective_2068(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*((x)**(3))

def objective_2069(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*(np.e)**(x)

def objective_2070(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*(x)**(0.5)*(np.log(x))

def objective_2071(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*((np.log(x)))**(2)

def objective_2072(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*(x)/(np.log(x))

def objective_2073(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*(x)**(0.5)

def objective_2074(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*(np.log(x))

def objective_2075(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e/(np.log(x))

def objective_2076(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e/(x)**(0.5)

def objective_2077(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*(np.log(x))/(x)

def objective_2078(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e/(x)

def objective_2079(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e/(x)**(1.5)

def objective_2080(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_2081(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e/((x)**(2))

def objective_2082(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(1.5)+e*(np.e)**((-x))

def objective_2083(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*((x)**(2))*(np.log(x))

def objective_2084(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*(x)**(2.5)

def objective_2085(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*((x)**(3))

def objective_2086(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*(np.e)**(x)

def objective_2087(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*(x)**(0.5)*(np.log(x))

def objective_2088(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*((np.log(x)))**(2)

def objective_2089(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*(x)/(np.log(x))

def objective_2090(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*(x)**(0.5)

def objective_2091(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*(np.log(x))

def objective_2092(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e/(np.log(x))

def objective_2093(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e/(x)**(0.5)

def objective_2094(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*(np.log(x))/(x)

def objective_2095(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e/(x)

def objective_2096(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e/(x)**(1.5)

def objective_2097(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*(np.log(x))/((x)**(2))

def objective_2098(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e/((x)**(2))

def objective_2099(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))+e*(np.e)**((-x))

def objective_2100(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e*(x)**(2.5)

def objective_2101(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e*((x)**(3))

def objective_2102(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e*(np.e)**(x)

def objective_2103(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e*(x)**(0.5)*(np.log(x))

def objective_2104(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e*((np.log(x)))**(2)

def objective_2105(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e*(x)/(np.log(x))

def objective_2106(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e*(x)**(0.5)

def objective_2107(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e*(np.log(x))

def objective_2108(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e/(np.log(x))

def objective_2109(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e/(x)**(0.5)

def objective_2110(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e*(np.log(x))/(x)

def objective_2111(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e/(x)

def objective_2112(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e/(x)**(1.5)

def objective_2113(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2114(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e/((x)**(2))

def objective_2115(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(2))*(np.log(x))+e*(np.e)**((-x))

def objective_2116(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e*((x)**(3))

def objective_2117(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e*(np.e)**(x)

def objective_2118(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e*(x)**(0.5)*(np.log(x))

def objective_2119(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e*((np.log(x)))**(2)

def objective_2120(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e*(x)/(np.log(x))

def objective_2121(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e*(x)**(0.5)

def objective_2122(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e*(np.log(x))

def objective_2123(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e/(np.log(x))

def objective_2124(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e/(x)**(0.5)

def objective_2125(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e*(np.log(x))/(x)

def objective_2126(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e/(x)

def objective_2127(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e/(x)**(1.5)

def objective_2128(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e*(np.log(x))/((x)**(2))

def objective_2129(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e/((x)**(2))

def objective_2130(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(2.5)+e*(np.e)**((-x))

def objective_2131(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e*(np.e)**(x)

def objective_2132(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e*(x)**(0.5)*(np.log(x))

def objective_2133(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e*((np.log(x)))**(2)

def objective_2134(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e*(x)/(np.log(x))

def objective_2135(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e*(x)**(0.5)

def objective_2136(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e*(np.log(x))

def objective_2137(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e/(np.log(x))

def objective_2138(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e/(x)**(0.5)

def objective_2139(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e*(np.log(x))/(x)

def objective_2140(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e/(x)

def objective_2141(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e/(x)**(1.5)

def objective_2142(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e*(np.log(x))/((x)**(2))

def objective_2143(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e/((x)**(2))

def objective_2144(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((x)**(3))+e*(np.e)**((-x))

def objective_2145(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e*(x)**(0.5)*(np.log(x))

def objective_2146(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e*((np.log(x)))**(2)

def objective_2147(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e*(x)/(np.log(x))

def objective_2148(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e*(x)**(0.5)

def objective_2149(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e*(np.log(x))

def objective_2150(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e/(np.log(x))

def objective_2151(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e/(x)**(0.5)

def objective_2152(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e*(np.log(x))/(x)

def objective_2153(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e/(x)

def objective_2154(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e/(x)**(1.5)

def objective_2155(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e*(np.log(x))/((x)**(2))

def objective_2156(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e/((x)**(2))

def objective_2157(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.e)**(x)+e*(np.e)**((-x))

def objective_2158(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*((np.log(x)))**(2)

def objective_2159(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(x)/(np.log(x))

def objective_2160(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(x)**(0.5)

def objective_2161(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))

def objective_2162(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e/(np.log(x))

def objective_2163(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e/(x)**(0.5)

def objective_2164(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/(x)

def objective_2165(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e/(x)

def objective_2166(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e/(x)**(1.5)

def objective_2167(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2168(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e/((x)**(2))

def objective_2169(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(np.e)**((-x))

def objective_2170(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)+e*(x)/(np.log(x))

def objective_2171(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)+e*(x)**(0.5)

def objective_2172(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)+e*(np.log(x))

def objective_2173(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)+e/(np.log(x))

def objective_2174(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)+e/(x)**(0.5)

def objective_2175(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)+e*(np.log(x))/(x)

def objective_2176(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)+e/(x)

def objective_2177(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)+e/(x)**(1.5)

def objective_2178(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)+e*(np.log(x))/((x)**(2))

def objective_2179(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)+e/((x)**(2))

def objective_2180(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*((np.log(x)))**(2)+e*(np.e)**((-x))

def objective_2181(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)/(np.log(x))+e*(x)**(0.5)

def objective_2182(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)/(np.log(x))+e*(np.log(x))

def objective_2183(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)/(np.log(x))+e/(np.log(x))

def objective_2184(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)/(np.log(x))+e/(x)**(0.5)

def objective_2185(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)/(np.log(x))+e*(np.log(x))/(x)

def objective_2186(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)/(np.log(x))+e/(x)

def objective_2187(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)/(np.log(x))+e/(x)**(1.5)

def objective_2188(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2189(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)/(np.log(x))+e/((x)**(2))

def objective_2190(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)/(np.log(x))+e*(np.e)**((-x))

def objective_2191(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)+e*(np.log(x))

def objective_2192(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)+e/(np.log(x))

def objective_2193(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)+e/(x)**(0.5)

def objective_2194(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)+e*(np.log(x))/(x)

def objective_2195(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)+e/(x)

def objective_2196(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)+e/(x)**(1.5)

def objective_2197(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2198(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)+e/((x)**(2))

def objective_2199(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(x)**(0.5)+e*(np.e)**((-x))

def objective_2200(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))+e/(np.log(x))

def objective_2201(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))+e/(x)**(0.5)

def objective_2202(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))+e*(np.log(x))/(x)

def objective_2203(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))+e/(x)

def objective_2204(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))+e/(x)**(1.5)

def objective_2205(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2206(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))+e/((x)**(2))

def objective_2207(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))+e*(np.e)**((-x))

def objective_2208(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(np.log(x))+e/(x)**(0.5)

def objective_2209(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(np.log(x))+e*(np.log(x))/(x)

def objective_2210(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(np.log(x))+e/(x)

def objective_2211(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(np.log(x))+e/(x)**(1.5)

def objective_2212(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2213(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(np.log(x))+e/((x)**(2))

def objective_2214(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(np.log(x))+e*(np.e)**((-x))

def objective_2215(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_2216(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)**(0.5)+e/(x)

def objective_2217(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)**(0.5)+e/(x)**(1.5)

def objective_2218(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2219(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)**(0.5)+e/((x)**(2))

def objective_2220(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_2221(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))/(x)+e/(x)

def objective_2222(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_2223(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_2224(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))/(x)+e/((x)**(2))

def objective_2225(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_2226(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)+e/(x)**(1.5)

def objective_2227(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)+e*(np.log(x))/((x)**(2))

def objective_2228(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)+e/((x)**(2))

def objective_2229(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)+e*(np.e)**((-x))

def objective_2230(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_2231(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)**(1.5)+e/((x)**(2))

def objective_2232(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_2233(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_2234(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_2235(x, a, b, c, d, e):
    return a+b*(x)+c*(x)*(np.log(x))+d/((x)**(2))+e*(np.e)**((-x))

def objective_2236(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*((x)**(2))*(np.log(x))

def objective_2237(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*(x)**(2.5)

def objective_2238(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*((x)**(3))

def objective_2239(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*(np.e)**(x)

def objective_2240(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*(x)**(0.5)*(np.log(x))

def objective_2241(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*((np.log(x)))**(2)

def objective_2242(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*(x)/(np.log(x))

def objective_2243(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*(x)**(0.5)

def objective_2244(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*(np.log(x))

def objective_2245(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e/(np.log(x))

def objective_2246(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e/(x)**(0.5)

def objective_2247(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*(np.log(x))/(x)

def objective_2248(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e/(x)

def objective_2249(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e/(x)**(1.5)

def objective_2250(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*(np.log(x))/((x)**(2))

def objective_2251(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e/((x)**(2))

def objective_2252(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))+e*(np.e)**((-x))

def objective_2253(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e*(x)**(2.5)

def objective_2254(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e*((x)**(3))

def objective_2255(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e*(np.e)**(x)

def objective_2256(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e*(x)**(0.5)*(np.log(x))

def objective_2257(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e*((np.log(x)))**(2)

def objective_2258(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e*(x)/(np.log(x))

def objective_2259(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e*(x)**(0.5)

def objective_2260(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e*(np.log(x))

def objective_2261(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e/(np.log(x))

def objective_2262(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e/(x)**(0.5)

def objective_2263(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e*(np.log(x))/(x)

def objective_2264(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e/(x)

def objective_2265(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e/(x)**(1.5)

def objective_2266(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2267(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e/((x)**(2))

def objective_2268(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(2))*(np.log(x))+e*(np.e)**((-x))

def objective_2269(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e*((x)**(3))

def objective_2270(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e*(np.e)**(x)

def objective_2271(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e*(x)**(0.5)*(np.log(x))

def objective_2272(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e*((np.log(x)))**(2)

def objective_2273(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e*(x)/(np.log(x))

def objective_2274(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e*(x)**(0.5)

def objective_2275(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e*(np.log(x))

def objective_2276(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e/(np.log(x))

def objective_2277(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e/(x)**(0.5)

def objective_2278(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e*(np.log(x))/(x)

def objective_2279(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e/(x)

def objective_2280(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e/(x)**(1.5)

def objective_2281(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e*(np.log(x))/((x)**(2))

def objective_2282(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e/((x)**(2))

def objective_2283(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(2.5)+e*(np.e)**((-x))

def objective_2284(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e*(np.e)**(x)

def objective_2285(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e*(x)**(0.5)*(np.log(x))

def objective_2286(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e*((np.log(x)))**(2)

def objective_2287(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e*(x)/(np.log(x))

def objective_2288(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e*(x)**(0.5)

def objective_2289(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e*(np.log(x))

def objective_2290(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e/(np.log(x))

def objective_2291(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e/(x)**(0.5)

def objective_2292(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e*(np.log(x))/(x)

def objective_2293(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e/(x)

def objective_2294(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e/(x)**(1.5)

def objective_2295(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e*(np.log(x))/((x)**(2))

def objective_2296(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e/((x)**(2))

def objective_2297(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((x)**(3))+e*(np.e)**((-x))

def objective_2298(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e*(x)**(0.5)*(np.log(x))

def objective_2299(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e*((np.log(x)))**(2)

def objective_2300(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e*(x)/(np.log(x))

def objective_2301(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e*(x)**(0.5)

def objective_2302(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e*(np.log(x))

def objective_2303(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e/(np.log(x))

def objective_2304(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e/(x)**(0.5)

def objective_2305(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e*(np.log(x))/(x)

def objective_2306(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e/(x)

def objective_2307(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e/(x)**(1.5)

def objective_2308(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e*(np.log(x))/((x)**(2))

def objective_2309(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e/((x)**(2))

def objective_2310(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.e)**(x)+e*(np.e)**((-x))

def objective_2311(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e*((np.log(x)))**(2)

def objective_2312(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e*(x)/(np.log(x))

def objective_2313(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e*(x)**(0.5)

def objective_2314(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))

def objective_2315(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e/(np.log(x))

def objective_2316(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e/(x)**(0.5)

def objective_2317(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/(x)

def objective_2318(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e/(x)

def objective_2319(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e/(x)**(1.5)

def objective_2320(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2321(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e/((x)**(2))

def objective_2322(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)*(np.log(x))+e*(np.e)**((-x))

def objective_2323(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)+e*(x)/(np.log(x))

def objective_2324(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)+e*(x)**(0.5)

def objective_2325(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)+e*(np.log(x))

def objective_2326(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)+e/(np.log(x))

def objective_2327(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)+e/(x)**(0.5)

def objective_2328(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)+e*(np.log(x))/(x)

def objective_2329(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)+e/(x)

def objective_2330(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)+e/(x)**(1.5)

def objective_2331(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)+e*(np.log(x))/((x)**(2))

def objective_2332(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)+e/((x)**(2))

def objective_2333(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*((np.log(x)))**(2)+e*(np.e)**((-x))

def objective_2334(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)/(np.log(x))+e*(x)**(0.5)

def objective_2335(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)/(np.log(x))+e*(np.log(x))

def objective_2336(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)/(np.log(x))+e/(np.log(x))

def objective_2337(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)/(np.log(x))+e/(x)**(0.5)

def objective_2338(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)/(np.log(x))+e*(np.log(x))/(x)

def objective_2339(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)/(np.log(x))+e/(x)

def objective_2340(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)/(np.log(x))+e/(x)**(1.5)

def objective_2341(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2342(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)/(np.log(x))+e/((x)**(2))

def objective_2343(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)/(np.log(x))+e*(np.e)**((-x))

def objective_2344(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)+e*(np.log(x))

def objective_2345(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)+e/(np.log(x))

def objective_2346(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)+e/(x)**(0.5)

def objective_2347(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)+e*(np.log(x))/(x)

def objective_2348(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)+e/(x)

def objective_2349(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)+e/(x)**(1.5)

def objective_2350(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2351(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)+e/((x)**(2))

def objective_2352(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(x)**(0.5)+e*(np.e)**((-x))

def objective_2353(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))+e/(np.log(x))

def objective_2354(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))+e/(x)**(0.5)

def objective_2355(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))+e*(np.log(x))/(x)

def objective_2356(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))+e/(x)

def objective_2357(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))+e/(x)**(1.5)

def objective_2358(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2359(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))+e/((x)**(2))

def objective_2360(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))+e*(np.e)**((-x))

def objective_2361(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(np.log(x))+e/(x)**(0.5)

def objective_2362(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(np.log(x))+e*(np.log(x))/(x)

def objective_2363(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(np.log(x))+e/(x)

def objective_2364(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(np.log(x))+e/(x)**(1.5)

def objective_2365(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2366(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(np.log(x))+e/((x)**(2))

def objective_2367(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(np.log(x))+e*(np.e)**((-x))

def objective_2368(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_2369(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)**(0.5)+e/(x)

def objective_2370(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)**(0.5)+e/(x)**(1.5)

def objective_2371(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2372(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)**(0.5)+e/((x)**(2))

def objective_2373(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_2374(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))/(x)+e/(x)

def objective_2375(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_2376(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_2377(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))/(x)+e/((x)**(2))

def objective_2378(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_2379(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)+e/(x)**(1.5)

def objective_2380(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)+e*(np.log(x))/((x)**(2))

def objective_2381(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)+e/((x)**(2))

def objective_2382(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)+e*(np.e)**((-x))

def objective_2383(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_2384(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)**(1.5)+e/((x)**(2))

def objective_2385(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_2386(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_2387(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_2388(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(1.5)+d/((x)**(2))+e*(np.e)**((-x))

def objective_2389(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e*(x)**(2.5)

def objective_2390(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e*((x)**(3))

def objective_2391(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e*(np.e)**(x)

def objective_2392(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e*(x)**(0.5)*(np.log(x))

def objective_2393(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e*((np.log(x)))**(2)

def objective_2394(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e*(x)/(np.log(x))

def objective_2395(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e*(x)**(0.5)

def objective_2396(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e*(np.log(x))

def objective_2397(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e/(np.log(x))

def objective_2398(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e/(x)**(0.5)

def objective_2399(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e*(np.log(x))/(x)

def objective_2400(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e/(x)

def objective_2401(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e/(x)**(1.5)

def objective_2402(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2403(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e/((x)**(2))

def objective_2404(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(2))*(np.log(x))+e*(np.e)**((-x))

def objective_2405(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e*((x)**(3))

def objective_2406(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e*(np.e)**(x)

def objective_2407(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e*(x)**(0.5)*(np.log(x))

def objective_2408(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e*((np.log(x)))**(2)

def objective_2409(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e*(x)/(np.log(x))

def objective_2410(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e*(x)**(0.5)

def objective_2411(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e*(np.log(x))

def objective_2412(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e/(np.log(x))

def objective_2413(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e/(x)**(0.5)

def objective_2414(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e*(np.log(x))/(x)

def objective_2415(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e/(x)

def objective_2416(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e/(x)**(1.5)

def objective_2417(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e*(np.log(x))/((x)**(2))

def objective_2418(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e/((x)**(2))

def objective_2419(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(2.5)+e*(np.e)**((-x))

def objective_2420(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*(np.e)**(x)

def objective_2421(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*(x)**(0.5)*(np.log(x))

def objective_2422(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((np.log(x)))**(2)

def objective_2423(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*(x)/(np.log(x))

def objective_2424(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*(x)**(0.5)

def objective_2425(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*(np.log(x))

def objective_2426(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e/(np.log(x))

def objective_2427(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e/(x)**(0.5)

def objective_2428(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*(np.log(x))/(x)

def objective_2429(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e/(x)

def objective_2430(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e/(x)**(1.5)

def objective_2431(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*(np.log(x))/((x)**(2))

def objective_2432(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e/((x)**(2))

def objective_2433(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*(np.e)**((-x))

def objective_2434(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e*(x)**(0.5)*(np.log(x))

def objective_2435(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e*((np.log(x)))**(2)

def objective_2436(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e*(x)/(np.log(x))

def objective_2437(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e*(x)**(0.5)

def objective_2438(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e*(np.log(x))

def objective_2439(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e/(np.log(x))

def objective_2440(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e/(x)**(0.5)

def objective_2441(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e*(np.log(x))/(x)

def objective_2442(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e/(x)

def objective_2443(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e/(x)**(1.5)

def objective_2444(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e*(np.log(x))/((x)**(2))

def objective_2445(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e/((x)**(2))

def objective_2446(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.e)**(x)+e*(np.e)**((-x))

def objective_2447(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e*((np.log(x)))**(2)

def objective_2448(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e*(x)/(np.log(x))

def objective_2449(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e*(x)**(0.5)

def objective_2450(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))

def objective_2451(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e/(np.log(x))

def objective_2452(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e/(x)**(0.5)

def objective_2453(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/(x)

def objective_2454(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e/(x)

def objective_2455(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e/(x)**(1.5)

def objective_2456(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2457(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e/((x)**(2))

def objective_2458(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)*(np.log(x))+e*(np.e)**((-x))

def objective_2459(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)+e*(x)/(np.log(x))

def objective_2460(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)+e*(x)**(0.5)

def objective_2461(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)+e*(np.log(x))

def objective_2462(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)+e/(np.log(x))

def objective_2463(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)+e/(x)**(0.5)

def objective_2464(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)+e*(np.log(x))/(x)

def objective_2465(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)+e/(x)

def objective_2466(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)+e/(x)**(1.5)

def objective_2467(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)+e*(np.log(x))/((x)**(2))

def objective_2468(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)+e/((x)**(2))

def objective_2469(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((np.log(x)))**(2)+e*(np.e)**((-x))

def objective_2470(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)/(np.log(x))+e*(x)**(0.5)

def objective_2471(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)/(np.log(x))+e*(np.log(x))

def objective_2472(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)/(np.log(x))+e/(np.log(x))

def objective_2473(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)/(np.log(x))+e/(x)**(0.5)

def objective_2474(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)/(np.log(x))+e*(np.log(x))/(x)

def objective_2475(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)/(np.log(x))+e/(x)

def objective_2476(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)/(np.log(x))+e/(x)**(1.5)

def objective_2477(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2478(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)/(np.log(x))+e/((x)**(2))

def objective_2479(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)/(np.log(x))+e*(np.e)**((-x))

def objective_2480(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)+e*(np.log(x))

def objective_2481(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)+e/(np.log(x))

def objective_2482(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)+e/(x)**(0.5)

def objective_2483(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)+e*(np.log(x))/(x)

def objective_2484(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)+e/(x)

def objective_2485(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)+e/(x)**(1.5)

def objective_2486(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2487(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)+e/((x)**(2))

def objective_2488(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(x)**(0.5)+e*(np.e)**((-x))

def objective_2489(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))+e/(np.log(x))

def objective_2490(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))+e/(x)**(0.5)

def objective_2491(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))+e*(np.log(x))/(x)

def objective_2492(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))+e/(x)

def objective_2493(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))+e/(x)**(1.5)

def objective_2494(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2495(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))+e/((x)**(2))

def objective_2496(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))+e*(np.e)**((-x))

def objective_2497(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(np.log(x))+e/(x)**(0.5)

def objective_2498(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(np.log(x))+e*(np.log(x))/(x)

def objective_2499(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(np.log(x))+e/(x)

def objective_2500(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(np.log(x))+e/(x)**(1.5)

def objective_2501(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2502(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(np.log(x))+e/((x)**(2))

def objective_2503(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(np.log(x))+e*(np.e)**((-x))

def objective_2504(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_2505(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)**(0.5)+e/(x)

def objective_2506(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)**(0.5)+e/(x)**(1.5)

def objective_2507(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2508(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)**(0.5)+e/((x)**(2))

def objective_2509(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_2510(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))/(x)+e/(x)

def objective_2511(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_2512(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_2513(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))/(x)+e/((x)**(2))

def objective_2514(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_2515(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)+e/(x)**(1.5)

def objective_2516(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)+e*(np.log(x))/((x)**(2))

def objective_2517(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)+e/((x)**(2))

def objective_2518(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)+e*(np.e)**((-x))

def objective_2519(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_2520(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)**(1.5)+e/((x)**(2))

def objective_2521(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_2522(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_2523(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_2524(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d/((x)**(2))+e*(np.e)**((-x))

def objective_2525(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e*((x)**(3))

def objective_2526(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e*(np.e)**(x)

def objective_2527(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e*(x)**(0.5)*(np.log(x))

def objective_2528(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e*((np.log(x)))**(2)

def objective_2529(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e*(x)/(np.log(x))

def objective_2530(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e*(x)**(0.5)

def objective_2531(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e*(np.log(x))

def objective_2532(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e/(np.log(x))

def objective_2533(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e/(x)**(0.5)

def objective_2534(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e*(np.log(x))/(x)

def objective_2535(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e/(x)

def objective_2536(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e/(x)**(1.5)

def objective_2537(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e*(np.log(x))/((x)**(2))

def objective_2538(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e/((x)**(2))

def objective_2539(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(2.5)+e*(np.e)**((-x))

def objective_2540(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e*(np.e)**(x)

def objective_2541(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e*(x)**(0.5)*(np.log(x))

def objective_2542(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e*((np.log(x)))**(2)

def objective_2543(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e*(x)/(np.log(x))

def objective_2544(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e*(x)**(0.5)

def objective_2545(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e*(np.log(x))

def objective_2546(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e/(np.log(x))

def objective_2547(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e/(x)**(0.5)

def objective_2548(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e*(np.log(x))/(x)

def objective_2549(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e/(x)

def objective_2550(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e/(x)**(1.5)

def objective_2551(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e*(np.log(x))/((x)**(2))

def objective_2552(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e/((x)**(2))

def objective_2553(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((x)**(3))+e*(np.e)**((-x))

def objective_2554(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e*(x)**(0.5)*(np.log(x))

def objective_2555(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e*((np.log(x)))**(2)

def objective_2556(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e*(x)/(np.log(x))

def objective_2557(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e*(x)**(0.5)

def objective_2558(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e*(np.log(x))

def objective_2559(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e/(np.log(x))

def objective_2560(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e/(x)**(0.5)

def objective_2561(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e*(np.log(x))/(x)

def objective_2562(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e/(x)

def objective_2563(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e/(x)**(1.5)

def objective_2564(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e*(np.log(x))/((x)**(2))

def objective_2565(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e/((x)**(2))

def objective_2566(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.e)**(x)+e*(np.e)**((-x))

def objective_2567(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*((np.log(x)))**(2)

def objective_2568(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(x)/(np.log(x))

def objective_2569(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(x)**(0.5)

def objective_2570(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))

def objective_2571(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e/(np.log(x))

def objective_2572(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e/(x)**(0.5)

def objective_2573(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/(x)

def objective_2574(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e/(x)

def objective_2575(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e/(x)**(1.5)

def objective_2576(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2577(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e/((x)**(2))

def objective_2578(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)*(np.log(x))+e*(np.e)**((-x))

def objective_2579(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)+e*(x)/(np.log(x))

def objective_2580(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)+e*(x)**(0.5)

def objective_2581(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)+e*(np.log(x))

def objective_2582(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)+e/(np.log(x))

def objective_2583(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)+e/(x)**(0.5)

def objective_2584(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)+e*(np.log(x))/(x)

def objective_2585(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)+e/(x)

def objective_2586(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)+e/(x)**(1.5)

def objective_2587(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)+e*(np.log(x))/((x)**(2))

def objective_2588(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)+e/((x)**(2))

def objective_2589(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*((np.log(x)))**(2)+e*(np.e)**((-x))

def objective_2590(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))+e*(x)**(0.5)

def objective_2591(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))+e*(np.log(x))

def objective_2592(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))+e/(np.log(x))

def objective_2593(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))+e/(x)**(0.5)

def objective_2594(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))+e*(np.log(x))/(x)

def objective_2595(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))+e/(x)

def objective_2596(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))+e/(x)**(1.5)

def objective_2597(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2598(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))+e/((x)**(2))

def objective_2599(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)/(np.log(x))+e*(np.e)**((-x))

def objective_2600(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)+e*(np.log(x))

def objective_2601(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)+e/(np.log(x))

def objective_2602(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)+e/(x)**(0.5)

def objective_2603(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)+e*(np.log(x))/(x)

def objective_2604(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)+e/(x)

def objective_2605(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)+e/(x)**(1.5)

def objective_2606(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2607(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)+e/((x)**(2))

def objective_2608(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(x)**(0.5)+e*(np.e)**((-x))

def objective_2609(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))+e/(np.log(x))

def objective_2610(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))+e/(x)**(0.5)

def objective_2611(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))+e*(np.log(x))/(x)

def objective_2612(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))+e/(x)

def objective_2613(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))+e/(x)**(1.5)

def objective_2614(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2615(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))+e/((x)**(2))

def objective_2616(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))+e*(np.e)**((-x))

def objective_2617(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(np.log(x))+e/(x)**(0.5)

def objective_2618(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(np.log(x))+e*(np.log(x))/(x)

def objective_2619(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(np.log(x))+e/(x)

def objective_2620(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(np.log(x))+e/(x)**(1.5)

def objective_2621(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2622(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(np.log(x))+e/((x)**(2))

def objective_2623(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(np.log(x))+e*(np.e)**((-x))

def objective_2624(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_2625(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)**(0.5)+e/(x)

def objective_2626(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)**(0.5)+e/(x)**(1.5)

def objective_2627(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2628(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)**(0.5)+e/((x)**(2))

def objective_2629(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_2630(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))/(x)+e/(x)

def objective_2631(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_2632(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_2633(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))/(x)+e/((x)**(2))

def objective_2634(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_2635(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)+e/(x)**(1.5)

def objective_2636(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)+e*(np.log(x))/((x)**(2))

def objective_2637(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)+e/((x)**(2))

def objective_2638(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)+e*(np.e)**((-x))

def objective_2639(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_2640(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)**(1.5)+e/((x)**(2))

def objective_2641(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_2642(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_2643(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_2644(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))*(np.log(x))+d/((x)**(2))+e*(np.e)**((-x))

def objective_2645(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e*(np.e)**(x)

def objective_2646(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e*(x)**(0.5)*(np.log(x))

def objective_2647(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e*((np.log(x)))**(2)

def objective_2648(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e*(x)/(np.log(x))

def objective_2649(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e*(x)**(0.5)

def objective_2650(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e*(np.log(x))

def objective_2651(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e/(np.log(x))

def objective_2652(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e/(x)**(0.5)

def objective_2653(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e*(np.log(x))/(x)

def objective_2654(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e/(x)

def objective_2655(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e/(x)**(1.5)

def objective_2656(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e*(np.log(x))/((x)**(2))

def objective_2657(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e/((x)**(2))

def objective_2658(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((x)**(3))+e*(np.e)**((-x))

def objective_2659(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e*(x)**(0.5)*(np.log(x))

def objective_2660(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e*((np.log(x)))**(2)

def objective_2661(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e*(x)/(np.log(x))

def objective_2662(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e*(x)**(0.5)

def objective_2663(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e*(np.log(x))

def objective_2664(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e/(np.log(x))

def objective_2665(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e/(x)**(0.5)

def objective_2666(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e*(np.log(x))/(x)

def objective_2667(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e/(x)

def objective_2668(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e/(x)**(1.5)

def objective_2669(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e*(np.log(x))/((x)**(2))

def objective_2670(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e/((x)**(2))

def objective_2671(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.e)**(x)+e*(np.e)**((-x))

def objective_2672(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e*((np.log(x)))**(2)

def objective_2673(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e*(x)/(np.log(x))

def objective_2674(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e*(x)**(0.5)

def objective_2675(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))

def objective_2676(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e/(np.log(x))

def objective_2677(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e/(x)**(0.5)

def objective_2678(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/(x)

def objective_2679(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e/(x)

def objective_2680(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e/(x)**(1.5)

def objective_2681(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2682(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e/((x)**(2))

def objective_2683(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)*(np.log(x))+e*(np.e)**((-x))

def objective_2684(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)+e*(x)/(np.log(x))

def objective_2685(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)+e*(x)**(0.5)

def objective_2686(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)+e*(np.log(x))

def objective_2687(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)+e/(np.log(x))

def objective_2688(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)+e/(x)**(0.5)

def objective_2689(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)+e*(np.log(x))/(x)

def objective_2690(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)+e/(x)

def objective_2691(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)+e/(x)**(1.5)

def objective_2692(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)+e*(np.log(x))/((x)**(2))

def objective_2693(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)+e/((x)**(2))

def objective_2694(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*((np.log(x)))**(2)+e*(np.e)**((-x))

def objective_2695(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)/(np.log(x))+e*(x)**(0.5)

def objective_2696(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)/(np.log(x))+e*(np.log(x))

def objective_2697(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)/(np.log(x))+e/(np.log(x))

def objective_2698(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)/(np.log(x))+e/(x)**(0.5)

def objective_2699(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)/(np.log(x))+e*(np.log(x))/(x)

def objective_2700(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)/(np.log(x))+e/(x)

def objective_2701(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)/(np.log(x))+e/(x)**(1.5)

def objective_2702(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2703(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)/(np.log(x))+e/((x)**(2))

def objective_2704(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)/(np.log(x))+e*(np.e)**((-x))

def objective_2705(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)+e*(np.log(x))

def objective_2706(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)+e/(np.log(x))

def objective_2707(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)+e/(x)**(0.5)

def objective_2708(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)+e*(np.log(x))/(x)

def objective_2709(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)+e/(x)

def objective_2710(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)+e/(x)**(1.5)

def objective_2711(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2712(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)+e/((x)**(2))

def objective_2713(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(x)**(0.5)+e*(np.e)**((-x))

def objective_2714(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))+e/(np.log(x))

def objective_2715(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))+e/(x)**(0.5)

def objective_2716(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))+e*(np.log(x))/(x)

def objective_2717(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))+e/(x)

def objective_2718(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))+e/(x)**(1.5)

def objective_2719(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2720(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))+e/((x)**(2))

def objective_2721(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))+e*(np.e)**((-x))

def objective_2722(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(np.log(x))+e/(x)**(0.5)

def objective_2723(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(np.log(x))+e*(np.log(x))/(x)

def objective_2724(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(np.log(x))+e/(x)

def objective_2725(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(np.log(x))+e/(x)**(1.5)

def objective_2726(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2727(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(np.log(x))+e/((x)**(2))

def objective_2728(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(np.log(x))+e*(np.e)**((-x))

def objective_2729(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_2730(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)**(0.5)+e/(x)

def objective_2731(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)**(0.5)+e/(x)**(1.5)

def objective_2732(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2733(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)**(0.5)+e/((x)**(2))

def objective_2734(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_2735(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))/(x)+e/(x)

def objective_2736(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_2737(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_2738(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))/(x)+e/((x)**(2))

def objective_2739(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_2740(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)+e/(x)**(1.5)

def objective_2741(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)+e*(np.log(x))/((x)**(2))

def objective_2742(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)+e/((x)**(2))

def objective_2743(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)+e*(np.e)**((-x))

def objective_2744(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_2745(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)**(1.5)+e/((x)**(2))

def objective_2746(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_2747(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_2748(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_2749(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(2.5)+d/((x)**(2))+e*(np.e)**((-x))

def objective_2750(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e*(x)**(0.5)*(np.log(x))

def objective_2751(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e*((np.log(x)))**(2)

def objective_2752(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e*(x)/(np.log(x))

def objective_2753(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e*(x)**(0.5)

def objective_2754(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e*(np.log(x))

def objective_2755(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e/(np.log(x))

def objective_2756(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e/(x)**(0.5)

def objective_2757(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e*(np.log(x))/(x)

def objective_2758(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e/(x)

def objective_2759(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e/(x)**(1.5)

def objective_2760(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e*(np.log(x))/((x)**(2))

def objective_2761(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e/((x)**(2))

def objective_2762(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.e)**(x)+e*(np.e)**((-x))

def objective_2763(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e*((np.log(x)))**(2)

def objective_2764(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e*(x)/(np.log(x))

def objective_2765(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e*(x)**(0.5)

def objective_2766(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))

def objective_2767(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e/(np.log(x))

def objective_2768(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e/(x)**(0.5)

def objective_2769(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/(x)

def objective_2770(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e/(x)

def objective_2771(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e/(x)**(1.5)

def objective_2772(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2773(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e/((x)**(2))

def objective_2774(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)*(np.log(x))+e*(np.e)**((-x))

def objective_2775(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)+e*(x)/(np.log(x))

def objective_2776(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)+e*(x)**(0.5)

def objective_2777(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)+e*(np.log(x))

def objective_2778(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)+e/(np.log(x))

def objective_2779(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)+e/(x)**(0.5)

def objective_2780(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)+e*(np.log(x))/(x)

def objective_2781(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)+e/(x)

def objective_2782(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)+e/(x)**(1.5)

def objective_2783(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)+e*(np.log(x))/((x)**(2))

def objective_2784(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)+e/((x)**(2))

def objective_2785(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*((np.log(x)))**(2)+e*(np.e)**((-x))

def objective_2786(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)/(np.log(x))+e*(x)**(0.5)

def objective_2787(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)/(np.log(x))+e*(np.log(x))

def objective_2788(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)/(np.log(x))+e/(np.log(x))

def objective_2789(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)/(np.log(x))+e/(x)**(0.5)

def objective_2790(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)/(np.log(x))+e*(np.log(x))/(x)

def objective_2791(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)/(np.log(x))+e/(x)

def objective_2792(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)/(np.log(x))+e/(x)**(1.5)

def objective_2793(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2794(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)/(np.log(x))+e/((x)**(2))

def objective_2795(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)/(np.log(x))+e*(np.e)**((-x))

def objective_2796(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)+e*(np.log(x))

def objective_2797(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)+e/(np.log(x))

def objective_2798(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)+e/(x)**(0.5)

def objective_2799(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)+e*(np.log(x))/(x)

def objective_2800(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)+e/(x)

def objective_2801(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)+e/(x)**(1.5)

def objective_2802(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2803(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)+e/((x)**(2))

def objective_2804(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(x)**(0.5)+e*(np.e)**((-x))

def objective_2805(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))+e/(np.log(x))

def objective_2806(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))+e/(x)**(0.5)

def objective_2807(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))+e*(np.log(x))/(x)

def objective_2808(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))+e/(x)

def objective_2809(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))+e/(x)**(1.5)

def objective_2810(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2811(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))+e/((x)**(2))

def objective_2812(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))+e*(np.e)**((-x))

def objective_2813(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(np.log(x))+e/(x)**(0.5)

def objective_2814(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(np.log(x))+e*(np.log(x))/(x)

def objective_2815(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(np.log(x))+e/(x)

def objective_2816(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(np.log(x))+e/(x)**(1.5)

def objective_2817(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2818(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(np.log(x))+e/((x)**(2))

def objective_2819(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(np.log(x))+e*(np.e)**((-x))

def objective_2820(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_2821(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)**(0.5)+e/(x)

def objective_2822(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)**(0.5)+e/(x)**(1.5)

def objective_2823(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2824(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)**(0.5)+e/((x)**(2))

def objective_2825(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_2826(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))/(x)+e/(x)

def objective_2827(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_2828(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_2829(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))/(x)+e/((x)**(2))

def objective_2830(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_2831(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)+e/(x)**(1.5)

def objective_2832(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)+e*(np.log(x))/((x)**(2))

def objective_2833(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)+e/((x)**(2))

def objective_2834(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)+e*(np.e)**((-x))

def objective_2835(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_2836(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)**(1.5)+e/((x)**(2))

def objective_2837(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_2838(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_2839(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_2840(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(3))+d/((x)**(2))+e*(np.e)**((-x))

def objective_2841(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e*((np.log(x)))**(2)

def objective_2842(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e*(x)/(np.log(x))

def objective_2843(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e*(x)**(0.5)

def objective_2844(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))

def objective_2845(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e/(np.log(x))

def objective_2846(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e/(x)**(0.5)

def objective_2847(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/(x)

def objective_2848(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e/(x)

def objective_2849(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e/(x)**(1.5)

def objective_2850(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2851(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e/((x)**(2))

def objective_2852(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)*(np.log(x))+e*(np.e)**((-x))

def objective_2853(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)+e*(x)/(np.log(x))

def objective_2854(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)+e*(x)**(0.5)

def objective_2855(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)+e*(np.log(x))

def objective_2856(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)+e/(np.log(x))

def objective_2857(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)+e/(x)**(0.5)

def objective_2858(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)+e*(np.log(x))/(x)

def objective_2859(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)+e/(x)

def objective_2860(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)+e/(x)**(1.5)

def objective_2861(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)+e*(np.log(x))/((x)**(2))

def objective_2862(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)+e/((x)**(2))

def objective_2863(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*((np.log(x)))**(2)+e*(np.e)**((-x))

def objective_2864(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)/(np.log(x))+e*(x)**(0.5)

def objective_2865(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)/(np.log(x))+e*(np.log(x))

def objective_2866(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)/(np.log(x))+e/(np.log(x))

def objective_2867(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)/(np.log(x))+e/(x)**(0.5)

def objective_2868(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)/(np.log(x))+e*(np.log(x))/(x)

def objective_2869(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)/(np.log(x))+e/(x)

def objective_2870(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)/(np.log(x))+e/(x)**(1.5)

def objective_2871(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2872(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)/(np.log(x))+e/((x)**(2))

def objective_2873(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)/(np.log(x))+e*(np.e)**((-x))

def objective_2874(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)+e*(np.log(x))

def objective_2875(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)+e/(np.log(x))

def objective_2876(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)+e/(x)**(0.5)

def objective_2877(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)+e*(np.log(x))/(x)

def objective_2878(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)+e/(x)

def objective_2879(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)+e/(x)**(1.5)

def objective_2880(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2881(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)+e/((x)**(2))

def objective_2882(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(x)**(0.5)+e*(np.e)**((-x))

def objective_2883(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))+e/(np.log(x))

def objective_2884(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))+e/(x)**(0.5)

def objective_2885(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))+e*(np.log(x))/(x)

def objective_2886(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))+e/(x)

def objective_2887(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))+e/(x)**(1.5)

def objective_2888(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2889(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))+e/((x)**(2))

def objective_2890(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))+e*(np.e)**((-x))

def objective_2891(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(np.log(x))+e/(x)**(0.5)

def objective_2892(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(np.log(x))+e*(np.log(x))/(x)

def objective_2893(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(np.log(x))+e/(x)

def objective_2894(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(np.log(x))+e/(x)**(1.5)

def objective_2895(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2896(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(np.log(x))+e/((x)**(2))

def objective_2897(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(np.log(x))+e*(np.e)**((-x))

def objective_2898(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_2899(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)**(0.5)+e/(x)

def objective_2900(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)**(0.5)+e/(x)**(1.5)

def objective_2901(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2902(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)**(0.5)+e/((x)**(2))

def objective_2903(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_2904(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))/(x)+e/(x)

def objective_2905(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_2906(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_2907(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))/(x)+e/((x)**(2))

def objective_2908(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_2909(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)+e/(x)**(1.5)

def objective_2910(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)+e*(np.log(x))/((x)**(2))

def objective_2911(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)+e/((x)**(2))

def objective_2912(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)+e*(np.e)**((-x))

def objective_2913(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_2914(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)**(1.5)+e/((x)**(2))

def objective_2915(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_2916(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_2917(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_2918(x, a, b, c, d, e):
    return a+b*(x)+c*(np.e)**(x)+d/((x)**(2))+e*(np.e)**((-x))

def objective_2919(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)+e*(x)/(np.log(x))

def objective_2920(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)+e*(x)**(0.5)

def objective_2921(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)+e*(np.log(x))

def objective_2922(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)+e/(np.log(x))

def objective_2923(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)+e/(x)**(0.5)

def objective_2924(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)+e*(np.log(x))/(x)

def objective_2925(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)+e/(x)

def objective_2926(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)+e/(x)**(1.5)

def objective_2927(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)+e*(np.log(x))/((x)**(2))

def objective_2928(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)+e/((x)**(2))

def objective_2929(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*((np.log(x)))**(2)+e*(np.e)**((-x))

def objective_2930(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))+e*(x)**(0.5)

def objective_2931(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))+e*(np.log(x))

def objective_2932(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))+e/(np.log(x))

def objective_2933(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))+e/(x)**(0.5)

def objective_2934(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))+e*(np.log(x))/(x)

def objective_2935(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))+e/(x)

def objective_2936(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))+e/(x)**(1.5)

def objective_2937(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2938(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))+e/((x)**(2))

def objective_2939(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)/(np.log(x))+e*(np.e)**((-x))

def objective_2940(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)+e*(np.log(x))

def objective_2941(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)+e/(np.log(x))

def objective_2942(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)+e/(x)**(0.5)

def objective_2943(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)+e*(np.log(x))/(x)

def objective_2944(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)+e/(x)

def objective_2945(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)+e/(x)**(1.5)

def objective_2946(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2947(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)+e/((x)**(2))

def objective_2948(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(x)**(0.5)+e*(np.e)**((-x))

def objective_2949(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))+e/(np.log(x))

def objective_2950(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))+e/(x)**(0.5)

def objective_2951(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))+e*(np.log(x))/(x)

def objective_2952(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))+e/(x)

def objective_2953(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))+e/(x)**(1.5)

def objective_2954(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2955(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))+e/((x)**(2))

def objective_2956(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))+e*(np.e)**((-x))

def objective_2957(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))+e/(x)**(0.5)

def objective_2958(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))+e*(np.log(x))/(x)

def objective_2959(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))+e/(x)

def objective_2960(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))+e/(x)**(1.5)

def objective_2961(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2962(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))+e/((x)**(2))

def objective_2963(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(np.log(x))+e*(np.e)**((-x))

def objective_2964(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_2965(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)+e/(x)

def objective_2966(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)+e/(x)**(1.5)

def objective_2967(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_2968(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)+e/((x)**(2))

def objective_2969(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_2970(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)+e/(x)

def objective_2971(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_2972(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_2973(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)+e/((x)**(2))

def objective_2974(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_2975(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)+e/(x)**(1.5)

def objective_2976(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)+e*(np.log(x))/((x)**(2))

def objective_2977(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)+e/((x)**(2))

def objective_2978(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)+e*(np.e)**((-x))

def objective_2979(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_2980(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(1.5)+e/((x)**(2))

def objective_2981(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_2982(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_2983(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_2984(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)*(np.log(x))+d/((x)**(2))+e*(np.e)**((-x))

def objective_2985(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))+e*(x)**(0.5)

def objective_2986(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))+e*(np.log(x))

def objective_2987(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))+e/(np.log(x))

def objective_2988(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))+e/(x)**(0.5)

def objective_2989(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))+e*(np.log(x))/(x)

def objective_2990(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))+e/(x)

def objective_2991(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))+e/(x)**(1.5)

def objective_2992(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_2993(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))+e/((x)**(2))

def objective_2994(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)/(np.log(x))+e*(np.e)**((-x))

def objective_2995(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)**(0.5)+e*(np.log(x))

def objective_2996(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)**(0.5)+e/(np.log(x))

def objective_2997(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)**(0.5)+e/(x)**(0.5)

def objective_2998(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)**(0.5)+e*(np.log(x))/(x)

def objective_2999(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)**(0.5)+e/(x)

def objective_3000(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)**(0.5)+e/(x)**(1.5)

def objective_3001(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_3002(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)**(0.5)+e/((x)**(2))

def objective_3003(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(x)**(0.5)+e*(np.e)**((-x))

def objective_3004(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))+e/(np.log(x))

def objective_3005(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))+e/(x)**(0.5)

def objective_3006(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))+e*(np.log(x))/(x)

def objective_3007(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))+e/(x)

def objective_3008(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))+e/(x)**(1.5)

def objective_3009(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_3010(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))+e/((x)**(2))

def objective_3011(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))+e*(np.e)**((-x))

def objective_3012(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(np.log(x))+e/(x)**(0.5)

def objective_3013(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(np.log(x))+e*(np.log(x))/(x)

def objective_3014(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(np.log(x))+e/(x)

def objective_3015(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(np.log(x))+e/(x)**(1.5)

def objective_3016(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_3017(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(np.log(x))+e/((x)**(2))

def objective_3018(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(np.log(x))+e*(np.e)**((-x))

def objective_3019(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_3020(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)**(0.5)+e/(x)

def objective_3021(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)**(0.5)+e/(x)**(1.5)

def objective_3022(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_3023(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)**(0.5)+e/((x)**(2))

def objective_3024(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_3025(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))/(x)+e/(x)

def objective_3026(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_3027(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_3028(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))/(x)+e/((x)**(2))

def objective_3029(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_3030(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)+e/(x)**(1.5)

def objective_3031(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)+e*(np.log(x))/((x)**(2))

def objective_3032(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)+e/((x)**(2))

def objective_3033(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)+e*(np.e)**((-x))

def objective_3034(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_3035(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)**(1.5)+e/((x)**(2))

def objective_3036(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_3037(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_3038(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_3039(x, a, b, c, d, e):
    return a+b*(x)+c*((np.log(x)))**(2)+d/((x)**(2))+e*(np.e)**((-x))

def objective_3040(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(x)**(0.5)+e*(np.log(x))

def objective_3041(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(x)**(0.5)+e/(np.log(x))

def objective_3042(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(x)**(0.5)+e/(x)**(0.5)

def objective_3043(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(x)**(0.5)+e*(np.log(x))/(x)

def objective_3044(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(x)**(0.5)+e/(x)

def objective_3045(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(x)**(0.5)+e/(x)**(1.5)

def objective_3046(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_3047(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(x)**(0.5)+e/((x)**(2))

def objective_3048(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(x)**(0.5)+e*(np.e)**((-x))

def objective_3049(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))+e/(np.log(x))

def objective_3050(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))+e/(x)**(0.5)

def objective_3051(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))+e*(np.log(x))/(x)

def objective_3052(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))+e/(x)

def objective_3053(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))+e/(x)**(1.5)

def objective_3054(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_3055(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))+e/((x)**(2))

def objective_3056(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))+e*(np.e)**((-x))

def objective_3057(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(np.log(x))+e/(x)**(0.5)

def objective_3058(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(np.log(x))+e*(np.log(x))/(x)

def objective_3059(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(np.log(x))+e/(x)

def objective_3060(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(np.log(x))+e/(x)**(1.5)

def objective_3061(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_3062(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(np.log(x))+e/((x)**(2))

def objective_3063(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(np.log(x))+e*(np.e)**((-x))

def objective_3064(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_3065(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)**(0.5)+e/(x)

def objective_3066(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)**(0.5)+e/(x)**(1.5)

def objective_3067(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_3068(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)**(0.5)+e/((x)**(2))

def objective_3069(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_3070(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))/(x)+e/(x)

def objective_3071(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_3072(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_3073(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))/(x)+e/((x)**(2))

def objective_3074(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_3075(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)+e/(x)**(1.5)

def objective_3076(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)+e*(np.log(x))/((x)**(2))

def objective_3077(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)+e/((x)**(2))

def objective_3078(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)+e*(np.e)**((-x))

def objective_3079(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_3080(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)**(1.5)+e/((x)**(2))

def objective_3081(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_3082(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_3083(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_3084(x, a, b, c, d, e):
    return a+b*(x)+c*(x)/(np.log(x))+d/((x)**(2))+e*(np.e)**((-x))

def objective_3085(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))+e/(np.log(x))

def objective_3086(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))+e/(x)**(0.5)

def objective_3087(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))+e*(np.log(x))/(x)

def objective_3088(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))+e/(x)

def objective_3089(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))+e/(x)**(1.5)

def objective_3090(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_3091(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))+e/((x)**(2))

def objective_3092(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))+e*(np.e)**((-x))

def objective_3093(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(np.log(x))+e/(x)**(0.5)

def objective_3094(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(np.log(x))+e*(np.log(x))/(x)

def objective_3095(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(np.log(x))+e/(x)

def objective_3096(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(np.log(x))+e/(x)**(1.5)

def objective_3097(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_3098(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(np.log(x))+e/((x)**(2))

def objective_3099(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(np.log(x))+e*(np.e)**((-x))

def objective_3100(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_3101(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)**(0.5)+e/(x)

def objective_3102(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)**(0.5)+e/(x)**(1.5)

def objective_3103(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_3104(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)**(0.5)+e/((x)**(2))

def objective_3105(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_3106(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))/(x)+e/(x)

def objective_3107(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_3108(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_3109(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))/(x)+e/((x)**(2))

def objective_3110(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_3111(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)+e/(x)**(1.5)

def objective_3112(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)+e*(np.log(x))/((x)**(2))

def objective_3113(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)+e/((x)**(2))

def objective_3114(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)+e*(np.e)**((-x))

def objective_3115(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_3116(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)**(1.5)+e/((x)**(2))

def objective_3117(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_3118(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_3119(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_3120(x, a, b, c, d, e):
    return a+b*(x)+c*(x)**(0.5)+d/((x)**(2))+e*(np.e)**((-x))

def objective_3121(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(np.log(x))+e/(x)**(0.5)

def objective_3122(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(np.log(x))+e*(np.log(x))/(x)

def objective_3123(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(np.log(x))+e/(x)

def objective_3124(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(np.log(x))+e/(x)**(1.5)

def objective_3125(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(np.log(x))+e*(np.log(x))/((x)**(2))

def objective_3126(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(np.log(x))+e/((x)**(2))

def objective_3127(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(np.log(x))+e*(np.e)**((-x))

def objective_3128(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_3129(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)**(0.5)+e/(x)

def objective_3130(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)**(0.5)+e/(x)**(1.5)

def objective_3131(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_3132(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)**(0.5)+e/((x)**(2))

def objective_3133(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_3134(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d*(np.log(x))/(x)+e/(x)

def objective_3135(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_3136(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_3137(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d*(np.log(x))/(x)+e/((x)**(2))

def objective_3138(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_3139(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)+e/(x)**(1.5)

def objective_3140(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)+e*(np.log(x))/((x)**(2))

def objective_3141(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)+e/((x)**(2))

def objective_3142(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)+e*(np.e)**((-x))

def objective_3143(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_3144(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)**(1.5)+e/((x)**(2))

def objective_3145(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_3146(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_3147(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_3148(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))+d/((x)**(2))+e*(np.e)**((-x))

def objective_3149(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/(x)

def objective_3150(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)**(0.5)+e/(x)

def objective_3151(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)**(0.5)+e/(x)**(1.5)

def objective_3152(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)**(0.5)+e*(np.log(x))/((x)**(2))

def objective_3153(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)**(0.5)+e/((x)**(2))

def objective_3154(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)**(0.5)+e*(np.e)**((-x))

def objective_3155(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d*(np.log(x))/(x)+e/(x)

def objective_3156(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_3157(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_3158(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d*(np.log(x))/(x)+e/((x)**(2))

def objective_3159(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_3160(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)+e/(x)**(1.5)

def objective_3161(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)+e*(np.log(x))/((x)**(2))

def objective_3162(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)+e/((x)**(2))

def objective_3163(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)+e*(np.e)**((-x))

def objective_3164(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_3165(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)**(1.5)+e/((x)**(2))

def objective_3166(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_3167(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_3168(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_3169(x, a, b, c, d, e):
    return a+b*(x)+c/(np.log(x))+d/((x)**(2))+e*(np.e)**((-x))

def objective_3170(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d*(np.log(x))/(x)+e/(x)

def objective_3171(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d*(np.log(x))/(x)+e/(x)**(1.5)

def objective_3172(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d*(np.log(x))/(x)+e*(np.log(x))/((x)**(2))

def objective_3173(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d*(np.log(x))/(x)+e/((x)**(2))

def objective_3174(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d*(np.log(x))/(x)+e*(np.e)**((-x))

def objective_3175(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d/(x)+e/(x)**(1.5)

def objective_3176(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d/(x)+e*(np.log(x))/((x)**(2))

def objective_3177(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d/(x)+e/((x)**(2))

def objective_3178(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d/(x)+e*(np.e)**((-x))

def objective_3179(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_3180(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d/(x)**(1.5)+e/((x)**(2))

def objective_3181(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_3182(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_3183(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_3184(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(0.5)+d/((x)**(2))+e*(np.e)**((-x))

def objective_3185(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))/(x)+d/(x)+e/(x)**(1.5)

def objective_3186(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))/(x)+d/(x)+e*(np.log(x))/((x)**(2))

def objective_3187(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))/(x)+d/(x)+e/((x)**(2))

def objective_3188(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))/(x)+d/(x)+e*(np.e)**((-x))

def objective_3189(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))/(x)+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_3190(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))/(x)+d/(x)**(1.5)+e/((x)**(2))

def objective_3191(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))/(x)+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_3192(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_3193(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))/(x)+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_3194(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))/(x)+d/((x)**(2))+e*(np.e)**((-x))

def objective_3195(x, a, b, c, d, e):
    return a+b*(x)+c/(x)+d/(x)**(1.5)+e*(np.log(x))/((x)**(2))

def objective_3196(x, a, b, c, d, e):
    return a+b*(x)+c/(x)+d/(x)**(1.5)+e/((x)**(2))

def objective_3197(x, a, b, c, d, e):
    return a+b*(x)+c/(x)+d/(x)**(1.5)+e*(np.e)**((-x))

def objective_3198(x, a, b, c, d, e):
    return a+b*(x)+c/(x)+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_3199(x, a, b, c, d, e):
    return a+b*(x)+c/(x)+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_3200(x, a, b, c, d, e):
    return a+b*(x)+c/(x)+d/((x)**(2))+e*(np.e)**((-x))

def objective_3201(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))+e/((x)**(2))

def objective_3202(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(1.5)+d*(np.log(x))/((x)**(2))+e*(np.e)**((-x))

def objective_3203(x, a, b, c, d, e):
    return a+b*(x)+c/(x)**(1.5)+d/((x)**(2))+e*(np.e)**((-x))

def objective_3204(x, a, b, c, d, e):
    return a+b*(x)+c*(np.log(x))/((x)**(2))+d/((x)**(2))+e*(np.e)**((-x))

def objective_3205(x, a, b, c, d, e):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))

def objective_3206(x, a, b, c, d, e, f):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))+f*((x)**(5))

def objective_3207(x, a, b, c, d, e, f, g):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))+f*((x)**(5))+g*((x)**(6))

def objective_3208(x, a, b, c, d, e, f, g, h):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))+f*((x)**(5))+g*((x)**(6))+h*((x)**(7))

def objective_3209(x, a, b, c, d, e, f, g, h, i):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))+f*((x)**(5))+g*((x)**(6))+h*((x)**(7))+i*((x)**(8))

def objective_3210(x, a, b, c, d, e, f, g, h, i, j):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))+f*((x)**(5))+g*((x)**(6))+h*((x)**(7))+i*((x)**(8))+j*((x)**(9))

def objective_3211(x, a, b, c, d, e, f, g, h, i, j, k):
    return a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))+f*((x)**(5))+g*((x)**(6))+h*((x)**(7))+i*((x)**(8))+j*((x)**(9))+k*((x)**(10))

def objective_3212(x, a, b, c, d):
    return np.e ** (a+b*(x)+c*((x)**(2))+d*((x)**(3)))

def objective_3213(x, a, b, c, d, e):
    return np.e ** (a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4)))

def objective_3214(x, a, b, c, d, e, f):
    return np.e ** (a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))+f*((x)**(5)))

def objective_3215(x, a, b, c, d):
    return (a+b*(x)+c*((x)**(2))+d*((x)**(3))) ** (-1)

def objective_3216(x, a, b, c, d, e):
    return (a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))) ** (-1)

def objective_3217(x, a, b, c, d, e, f):
    return (a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))+f*((x)**(5))) ** (-1)

def objective_3218(x, a, b, c):
    return (a+b*(x)+c*((x)**(2))) ** 2

def objective_3219(x, a, b, c, d):
    return (a+b*(x)+c*((x)**(2))+d*((x)**(3))) ** 2

def objective_3220(x, a, b, c, d, e):
    return (a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))) ** 2

def objective_3221(x, a, b, c, d, e, f):
    return (a+b*(x)+c*((x)**(2))+d*((x)**(3))+e*((x)**(4))+f*((x)**(5))) ** 2

def objective_3225(x, a, b, c, d, e, f):
    return a+b*(x)+c/(x)+d*((x)**(2))+e/((x)**(2))+f*((x)**(3))

def objective_3226(x, a, b, c, d, e, f, g):
    return a+b*(x)+c/(x)+d*((x)**(2))+e/((x)**(2))+f*((x)**(3))+g/((x)**(3))

def objective_3227(x, a, b, c, d, e, f, g, h):
    return a+b*(x)+c/(x)+d*((x)**(2))+e/((x)**(2))+f*((x)**(3))+g/((x)**(3))+h*((x)**(4))

def objective_3228(x, a, b, c, d, e, f, g, h, i):
    return a+b*(x)+c/(x)+d*((x)**(2))+e/((x)**(2))+f*((x)**(3))+g/((x)**(3))+h*((x)**(4))+i/((x)**(4))

def objective_3229(x, a, b, c, d, e, f, g, h, i, j):
    return a+b*(x)+c/(x)+d*((x)**(2))+e/((x)**(2))+f*((x)**(3))+g/((x)**(3))+h*((x)**(4))+i/((x)**(4))+j*((x)**(5))

def objective_3230(x, a, b, c, d, e, f, g, h, i, j, k):
    return a+b*(x)+c/(x)+d*((x)**(2))+e/((x)**(2))+f*((x)**(3))+g/((x)**(3))+h*((x)**(4))+i/((x)**(4))+j*((x)**(5))+k/((x)**(5))

def objective_3231(x, a, b, c, d):
    return a+b*(np.log(x))+c*((np.log(x)))**(2)+d*((np.log(x)))**(3)

def objective_3232(x, a, b, c, d, e):
    return a+b*(np.log(x))+c*((np.log(x)))**(2)+d*((np.log(x)))**(3)+e*((np.log(x)))**(4)

def objective_3233(x, a, b, c, d, e, f):
    return a+b*(np.log(x))+c*((np.log(x)))**(2)+d*((np.log(x)))**(3)+e*((np.log(x)))**(4)+f*((np.log(x)))**(5)

def objective_3234(x, a, b, c, d, e, f, g):
    return a+b*(np.log(x))+c*((np.log(x)))**(2)+d*((np.log(x)))**(3)+e*((np.log(x)))**(4)+f*((np.log(x)))**(5)+g*((np.log(x)))**(6)

def objective_3235(x, a, b, c, d, e, f, g, h):
    return a+b*(np.log(x))+c*((np.log(x)))**(2)+d*((np.log(x)))**(3)+e*((np.log(x)))**(4)+f*((np.log(x)))**(5)+g*((np.log(x)))**(6)+h*((np.log(x)))**(7)

def objective_3236(x, a, b, c, d, e, f, g, h, i):
    return a+b*(np.log(x))+c*((np.log(x)))**(2)+d*((np.log(x)))**(3)+e*((np.log(x)))**(4)+f*((np.log(x)))**(5)+g*((np.log(x)))**(6)+h*((np.log(x)))**(7)+i*((np.log(x)))**(8)

def objective_3237(x, a, b, c, d, e, f, g, h, i, j):
    return a+b*(np.log(x))+c*((np.log(x)))**(2)+d*((np.log(x)))**(3)+e*((np.log(x)))**(4)+f*((np.log(x)))**(5)+g*((np.log(x)))**(6)+h*((np.log(x)))**(7)+i*((np.log(x)))**(8)+j*((np.log(x)))**(9)

def objective_3238(x, a, b, c, d, e, f, g, h, i, j, k):
    return a+b*(np.log(x))+c*((np.log(x)))**(2)+d*((np.log(x)))**(3)+e*((np.log(x)))**(4)+f*((np.log(x)))**(5)+g*((np.log(x)))**(6)+h*((np.log(x)))**(7)+i*((np.log(x)))**(8)+j*((np.log(x)))**(9)+k*((np.log(x)))**(10)

def objective_3239(x, a, b, c, d, e):
    return a+b*(np.log(x))+c/(np.log(x))+d*((np.log(x)))**(2)+e/((np.log(x)))**(2)

def objective_3240(x, a, b, c, d, e, f):
    return a+b*(np.log(x))+c/(np.log(x))+d*((np.log(x)))**(2)+e/((np.log(x)))**(2)+f*((np.log(x)))**(3)

def objective_3241(x, a, b, c, d, e, f, g):
    return a+b*(np.log(x))+c/(np.log(x))+d*((np.log(x)))**(2)+e/((np.log(x)))**(2)+f*((np.log(x)))**(3)+g/((np.log(x)))**(3)

def objective_3242(x, a, b, c, d, e, f, g, h):
    return a+b*(np.log(x))+c/(np.log(x))+d*((np.log(x)))**(2)+e/((np.log(x)))**(2)+f*((np.log(x)))**(3)+g/((np.log(x)))**(3)+h*((np.log(x)))**(4)

def objective_3243(x, a, b, c, d, e, f, g, h, i):
    return a+b*(np.log(x))+c/(np.log(x))+d*((np.log(x)))**(2)+e/((np.log(x)))**(2)+f*((np.log(x)))**(3)+g/((np.log(x)))**(3)+h*((np.log(x)))**(4)+i/((np.log(x)))**(4)

def objective_3244(x, a, b, c, d, e, f, g, h, i, j):
    return a+b*(np.log(x))+c/(np.log(x))+d*((np.log(x)))**(2)+e/((np.log(x)))**(2)+f*((np.log(x)))**(3)+g/((np.log(x)))**(3)+h*((np.log(x)))**(4)+i/((np.log(x)))**(4)+j*((np.log(x)))**(5)

def objective_3245(x, a, b, c, d, e, f, g, h, i, j, k):
    return a+b*(np.log(x))+c/(np.log(x))+d*((np.log(x)))**(2)+e/((np.log(x)))**(2)+f*((np.log(x)))**(3)+g/((np.log(x)))**(3)+h*((np.log(x)))**(4)+i/((np.log(x)))**(4)+j*((np.log(x)))**(5)+k/((np.log(x)))**(5)

def objective_3246(x, a, b, c, d):
    return a+b/(x)+c/((x)**(2))+d/((x)**(3))

def objective_3247(x, a, b, c, d, e):
    return a+b/(x)+c/((x)**(2))+d/((x)**(3))+e/((x)**(4))

def objective_3248(x, a, b, c, d, e, f):
    return a+b/(x)+c/((x)**(2))+d/((x)**(3))+e/((x)**(4))+f/((x)**(5))

def objective_3249(x, a, b, c, d, e, f, g):
    return a+b/(x)+c/((x)**(2))+d/((x)**(3))+e/((x)**(4))+f/((x)**(5))+g/((x)**(6))

def objective_3250(x, a, b, c, d, e, f, g, h):
    return a+b/(x)+c/((x)**(2))+d/((x)**(3))+e/((x)**(4))+f/((x)**(5))+g/((x)**(6))+h/((x)**(7))

def objective_3251(x, a, b, c, d, e, f, g, h, i):
    return a+b/(x)+c/((x)**(2))+d/((x)**(3))+e/((x)**(4))+f/((x)**(5))+g/((x)**(6))+h/((x)**(7))+i/((x)**(8))

def objective_3252(x, a, b, c, d, e, f, g, h, i, j):
    return a+b/(x)+c/((x)**(2))+d/((x)**(3))+e/((x)**(4))+f/((x)**(5))+g/((x)**(6))+h/((x)**(7))+i/((x)**(8))+j/((x)**(9))

def objective_3253(x, a, b, c, d, e, f, g, h, i, j, k):
    return a+b/(x)+c/((x)**(2))+d/((x)**(3))+e/((x)**(4))+f/((x)**(5))+g/((x)**(6))+h/((x)**(7))+i/((x)**(8))+j/((x)**(9))+k/((x)**(10))

def objective_3254(x, a, b, c):
    return a+b/(np.log(x))+c/((np.log(x)))**(2)

def objective_3255(x, a, b, c, d):
    return a+b/(np.log(x))+c/((np.log(x)))**(2)+d/((np.log(x)))**(3)

def objective_3256(x, a, b, c, d, e):
    return a+b/(np.log(x))+c/((np.log(x)))**(2)+d/((np.log(x)))**(3)+e/((np.log(x)))**(4)

def objective_3257(x, a, b, c, d, e, f):
    return a+b/(np.log(x))+c/((np.log(x)))**(2)+d/((np.log(x)))**(3)+e/((np.log(x)))**(4)+f/((np.log(x)))**(5)

def objective_3258(x, a, b, c, d, e, f, g):
    return a+b/(np.log(x))+c/((np.log(x)))**(2)+d/((np.log(x)))**(3)+e/((np.log(x)))**(4)+f/((np.log(x)))**(5)+g/((np.log(x)))**(6)

def objective_3259(x, a, b, c, d, e, f, g, h):
    return a+b/(np.log(x))+c/((np.log(x)))**(2)+d/((np.log(x)))**(3)+e/((np.log(x)))**(4)+f/((np.log(x)))**(5)+g/((np.log(x)))**(6)+h/((np.log(x)))**(7)

def objective_3260(x, a, b, c, d, e, f, g, h, i):
    return a+b/(np.log(x))+c/((np.log(x)))**(2)+d/((np.log(x)))**(3)+e/((np.log(x)))**(4)+f/((np.log(x)))**(5)+g/((np.log(x)))**(6)+h/((np.log(x)))**(7)+i/((np.log(x)))**(8)

def objective_3261(x, a, b, c, d, e, f, g, h, i, j):
    return a+b/(np.log(x))+c/((np.log(x)))**(2)+d/((np.log(x)))**(3)+e/((np.log(x)))**(4)+f/((np.log(x)))**(5)+g/((np.log(x)))**(6)+h/((np.log(x)))**(7)+i/((np.log(x)))**(8)+j/((np.log(x)))**(9)

def objective_3262(x, a, b, c, d, e, f, g, h, i, j, k):
    return a+b/(np.log(x))+c/((np.log(x)))**(2)+d/((np.log(x)))**(3)+e/((np.log(x)))**(4)+f/((np.log(x)))**(5)+g/((np.log(x)))**(6)+h/((np.log(x)))**(7)+i/((np.log(x)))**(8)+j/((np.log(x)))**(9)+k/((np.log(x)))**(10)

def objective_3263(x, a, b, c, d, e, f):
    return a+b*(x)**(0.5)+c*(x)+d*(x)**(1.5)+e*((x)**(2))+f*(x)**(2.5)

def objective_3264(x, a, b, c, d, e, f, g):
    return a+b*(x)**(0.5)+c*(x)+d*(x)**(1.5)+e*((x)**(2))+f*(x)**(2.5)+g*((x)**(3))

def objective_3265(x, a, b, c, d, e, f, g, h):
    return a+b*(x)**(0.5)+c*(x)+d*(x)**(1.5)+e*((x)**(2))+f*(x)**(2.5)+g*((x)**(3))+h*(x)**(3.5)

def objective_3266(x, a, b, c, d, e, f, g, h, i):
    return a+b*(x)**(0.5)+c*(x)+d*(x)**(1.5)+e*((x)**(2))+f*(x)**(2.5)+g*((x)**(3))+h*(x)**(3.5)+i*((x)**(4))

def objective_3267(x, a, b, c, d, e, f, g, h, i, j):
    return a+b*(x)**(0.5)+c*(x)+d*(x)**(1.5)+e*((x)**(2))+f*(x)**(2.5)+g*((x)**(3))+h*(x)**(3.5)+i*((x)**(4))+j*(x)**(4.5)

def objective_3268(x, a, b, c, d, e, f, g, h, i, j, k):
    return a+b*(x)**(0.5)+c*(x)+d*(x)**(1.5)+e*((x)**(2))+f*(x)**(2.5)+g*((x)**(3))+h*(x)**(3.5)+i*((x)**(4))+j*(x)**(4.5)+k*((x)**(5))

def objective_3269(x, a, b, c):
    return a+b*((x)**(2))+c*((x)**(4))

def objective_3270(x, a, b, c, d):
    return a+b*((x)**(2))+c*((x)**(4))+d*((x)**(6))

def objective_3271(x, a, b, c, d, e):
    return a+b*((x)**(2))+c*((x)**(4))+d*((x)**(6))+e*((x)**(8))

def objective_3272(x, a, b, c, d, e, f):
    return a+b*((x)**(2))+c*((x)**(4))+d*((x)**(6))+e*((x)**(8))+f*((x)**(10))

def objective_3273(x, a, b, c, d, e, f, g):
    return a+b*((x)**(2))+c*((x)**(4))+d*((x)**(6))+e*((x)**(8))+f*((x)**(10))+g*((x)**(12))

def objective_3274(x, a, b, c, d, e, f, g, h):
    return a+b*((x)**(2))+c*((x)**(4))+d*((x)**(6))+e*((x)**(8))+f*((x)**(10))+g*((x)**(12))+h*((x)**(14))

def objective_3275(x, a, b, c, d, e, f, g, h, i):
    return a+b*((x)**(2))+c*((x)**(4))+d*((x)**(6))+e*((x)**(8))+f*((x)**(10))+g*((x)**(12))+h*((x)**(14))+i*((x)**(16))

def objective_3276(x, a, b, c, d, e, f, g, h, i, j):
    return a+b*((x)**(2))+c*((x)**(4))+d*((x)**(6))+e*((x)**(8))+f*((x)**(10))+g*((x)**(12))+h*((x)**(14))+i*((x)**(16))+j*((x)**(18))

def objective_3277(x, a, b, c, d, e, f, g, h, i, j, k):
    return a+b*((x)**(2))+c*((x)**(4))+d*((x)**(6))+e*((x)**(8))+f*((x)**(10))+g*((x)**(12))+h*((x)**(14))+i*((x)**(16))+j*((x)**(18))+k*((x)**(20))

def objective_3278(x, a, c, b):
    return (a+c*(x))/((1)+b*(x)) 

def objective_3279(x, a, c, b, d):
    return (a+c*(x))/((1)+b*(x)+d*((x)**(2)))

def objective_3280(x, a, c, e, b, d):
    return (a+c*(x)+e*((x)**(2)))/((1)+b*(x)+d*((x)**(2))) 

def objective_3281(x, a, c, e, b, d, f):
    return (a+c*(x)+e*((x)**(2)))/((1)+b*(x)+d*((x)**(2))+f*((x)**(3)))

def objective_3282(x, a, c, e, g, b, d, f):
    return (a+c*(x)+e*((x)**(2))+g*((x)**(3)))/((1)+b*(x)+d*((x)**(2))+f*((x)**(3)))

def objective_3283(x, a, c, e, g, b, d, f, h):
    return (a+c*(x)+e*((x)**(2))+g*((x)**(3)))/((1)+b*(x)+d*((x)**(2))+f*((x)**(3))+h*((x)**(4))) 

def objective_3284(x, a, c, e, g, i, b, d, f, h):
    return (a+c*(x)+e*((x)**(2))+g*((x)**(3))+i*((x)**(4)))/((1)+b*(x)+d*((x)**(2))+f*((x)**(3))+h*((x)**(4))) 

def objective_3285(x, a, c, e, g, i, b, d, f, h, j):
    return (a+c*(x)+e*((x)**(2))+g*((x)**(3))+i*((x)**(4)))/((1)+b*(x)+d*((x)**(2))+f*((x)**(3))+h*((x)**(4))+j*((x)**(5))) 

def objective_3286(x, a, c, e, g, i, k, b, d, f, h, j):
    return (a+c*(x)+e*((x)**(2))+g*((x)**(3))+i*((x)**(4))+k*((x)**(5)))/((1)+b*(x)+d*((x)**(2))+f*((x)**(3))+h*((x)**(4))+j*((x)**(5))) 

def objective_3287(x, a, c, e, g, b, d, f, h):
    return (a+c*((x)**(2))+e*((x)**(4))+g*((x)**(6)))/((1)+b*((x)**(2))+d*((x)**(4))+f*((x)**(6))+h*((x)**(8))) 


all_objectives = [objective_0, objective_1, objective_10, objective_1000, objective_1001, objective_1002, objective_1003, objective_1004, objective_1005, objective_1006, objective_1007, objective_1008, objective_1009, objective_1010, objective_1011, objective_1012, objective_1013, objective_1014, objective_1015, objective_1016, objective_1017, objective_1018, objective_1019, objective_1020, objective_1021, objective_1022, objective_1023, objective_1024, objective_1025, objective_1026, objective_1027, objective_1028, objective_1029, objective_1030, objective_1031, objective_1032, objective_1033, objective_1034, objective_1035, objective_1036, objective_1037, objective_1038, objective_1039, objective_1040, objective_1041, objective_1042, objective_1043, objective_1044, objective_1045, objective_1046, objective_1047, objective_1048, objective_1049, objective_105, objective_1050, objective_1051, 
objective_1052, objective_1053, objective_1054, objective_1055, objective_1056, objective_1057, objective_1058, objective_1059, objective_106, objective_1060, objective_1061, objective_1062, objective_1063, objective_1064, objective_1065, objective_1066, objective_1067, objective_1068, objective_1069, objective_107, objective_1070, objective_1071, objective_1072, objective_1073, objective_1074, objective_1075, objective_1076, objective_1077, objective_1078, objective_1079, objective_108, objective_1080, objective_1081, objective_1082, objective_1083, objective_1084, objective_1085, objective_1086, objective_1087, objective_1088, objective_1089, objective_109, objective_1090, objective_1091, objective_1092, objective_1093, objective_1094, objective_1095, objective_1096, objective_1097, objective_1098, objective_1099, objective_11, objective_110, objective_1100, objective_1101, objective_1102, objective_1103, objective_1104, objective_1105, objective_1106, objective_1107, objective_1108, objective_1109, objective_111, objective_1110, objective_1111, objective_1112, objective_1113, objective_1114, objective_1115, objective_1116, objective_1117, objective_1118, objective_1119, objective_112, objective_1120, objective_1121, objective_1122, objective_1123, objective_1124, objective_1125, objective_1126, objective_1127, objective_1128, objective_1129, objective_113, objective_1130, objective_1131, objective_1132, objective_1133, objective_1134, objective_1135, objective_1136, objective_1137, objective_1138, objective_1139, objective_114, objective_1140, objective_1141, objective_1142, objective_1143, objective_1144, objective_1145, objective_1146, objective_1147, objective_1148, objective_1149, objective_115, objective_1150, objective_1151, objective_1152, objective_1153, objective_1154, objective_1155, objective_1156, objective_1157, objective_1158, objective_1159, objective_116, objective_1160, objective_1161, objective_1162, objective_1163, objective_1164, objective_1165, objective_1166, objective_1167, objective_1168, objective_1169, objective_117, objective_1170, objective_1171, objective_1172, objective_1173, objective_1174, objective_1175, objective_1176, objective_1177, objective_1178, objective_1179, objective_118, objective_1180, objective_1181, objective_1182, objective_1183, objective_1184, objective_1185, objective_1186, objective_1187, objective_1188, objective_1189, objective_119, objective_1190, objective_1191, objective_1192, objective_1193, objective_1194, objective_1195, objective_1196, objective_1197, objective_1198, objective_1199, objective_12, objective_120, objective_1200, objective_1201, objective_1202, objective_1203, objective_1204, objective_1205, objective_1206, objective_1207, objective_1208, objective_1209, objective_121, objective_1210, 
objective_1211, objective_1212, objective_1213, objective_1214, objective_1215, objective_1216, objective_1217, objective_1218, objective_1219, objective_122, objective_1220, objective_1221, objective_1222, objective_1223, objective_1224, objective_1225, objective_1226, objective_1227, objective_1228, objective_1229, objective_123, objective_1230, objective_1231, objective_1232, objective_1233, objective_1234, objective_1235, objective_1236, objective_1237, objective_1238, objective_1239, objective_124, objective_1240, objective_1241, objective_1242, objective_1243, objective_1244, objective_1245, objective_1246, objective_1247, objective_1248, objective_1249, objective_125, objective_1250, objective_1251, objective_1252, objective_1253, objective_1254, objective_1255, objective_1256, objective_1257, objective_1258, objective_1259, objective_126, objective_1260, objective_1261, objective_1262, objective_1263, objective_1264, objective_1265, objective_1266, objective_1267, objective_1268, objective_1269, objective_127, objective_1270, objective_1271, objective_1272, objective_1273, objective_1274, objective_1275, objective_1276, objective_1277, objective_1278, objective_1279, objective_128, objective_1280, objective_1281, objective_1282, objective_1283, objective_1284, objective_1285, objective_1286, objective_1287, objective_1288, objective_1289, objective_129, objective_1290, objective_1291, objective_1292, objective_1293, objective_1294, objective_1295, 
objective_1296, objective_1297, objective_1298, objective_1299, objective_13, objective_130, objective_1300, objective_1301, objective_1302, objective_1303, objective_1304, objective_1305, objective_1306, objective_1307, objective_1308, objective_1309, objective_131, objective_1310, objective_1311, objective_1312, objective_1313, objective_1314, objective_1315, objective_1316, objective_1317, objective_1318, objective_1319, objective_132, objective_1320, objective_1321, objective_1322, objective_1323, objective_1324, objective_1325, objective_1326, objective_1327, objective_1328, objective_1329, objective_133, objective_1330, objective_1331, objective_1332, objective_1333, objective_1334, objective_1335, objective_1336, objective_1337, objective_1338, objective_1339, objective_134, objective_1340, objective_1341, objective_1342, objective_1343, objective_1344, objective_1345, objective_1346, objective_1347, objective_1348, objective_1349, objective_135, objective_1350, objective_1351, objective_1352, objective_1353, objective_1354, objective_1355, objective_1356, objective_1357, objective_1358, objective_1359, objective_136, objective_1360, objective_1361, objective_1362, objective_1363, objective_1364, objective_1365, objective_1366, objective_1367, objective_1368, objective_1369, objective_137, objective_1370, objective_1371, objective_1372, objective_1373, objective_1374, objective_1375, objective_1376, objective_1377, objective_1378, objective_1379, objective_138, objective_1380, objective_1381, objective_1382, objective_1383, objective_1384, objective_1385, objective_1386, objective_1387, objective_1388, objective_1389, objective_139, objective_1390, objective_1391, objective_1392, objective_1393, objective_1394, objective_1395, objective_1396, objective_1397, objective_1398, objective_1399, objective_14, objective_140, objective_1400, objective_1401, objective_1402, objective_1403, objective_1404, objective_1405, objective_1406, objective_1407, objective_1408, objective_1409, objective_141, objective_1410, objective_1411, objective_1412, objective_1413, objective_1414, objective_1415, objective_1416, objective_1417, objective_1418, objective_1419, objective_142, objective_1420, objective_1421, objective_1422, objective_1423, objective_1424, objective_1425, objective_1426, objective_1427, objective_1428, objective_1429, objective_143, objective_1430, objective_1431, objective_1432, objective_1433, objective_1434, objective_1435, objective_1436, objective_1437, objective_1438, objective_1439, objective_144, objective_1440, objective_1441, objective_1442, objective_1443, objective_1444, objective_1445, objective_1446, objective_1447, objective_1448, objective_1449, objective_145, objective_1450, objective_1451, objective_1452, objective_1453, objective_1454, 
objective_1455, objective_1456, objective_1457, objective_1458, objective_1459, objective_146, objective_1460, objective_1461, objective_1462, objective_1463, objective_1464, objective_1465, objective_1466, objective_1467, objective_1468, objective_1469, objective_147, objective_1470, objective_1471, objective_1472, objective_1473, objective_1474, objective_1475, objective_1476, objective_1477, objective_1478, objective_1479, objective_148, objective_1480, objective_1481, objective_1482, objective_1483, objective_1484, objective_1485, objective_1486, objective_1487, objective_1488, objective_1489, objective_149, objective_1490, objective_1491, objective_1492, objective_1493, objective_1494, objective_1495, objective_1496, objective_1497, objective_1498, objective_1499, objective_15, objective_150, objective_1500, objective_1501, objective_1502, objective_1503, objective_1504, objective_1505, objective_1506, objective_1507, objective_1508, objective_1509, objective_151, objective_1510, objective_1511, objective_1512, objective_1513, objective_1514, objective_1515, objective_1516, objective_1517, objective_1518, objective_1519, objective_152, objective_1520, objective_1521, objective_1522, objective_1523, objective_1524, objective_1525, objective_1526, objective_1527, objective_1528, objective_1529, objective_153, objective_1530, objective_1531, objective_1532, objective_1533, objective_1534, objective_1535, objective_1536, objective_1537, objective_1538, objective_1539, objective_154, objective_1540, objective_1541, objective_1542, objective_1543, objective_1544, objective_1545, objective_1546, objective_1547, objective_1548, objective_1549, objective_155, objective_1550, objective_1551, objective_1552, objective_1553, objective_1554, objective_1555, objective_1556, objective_1557, objective_1558, objective_1559, objective_156, objective_1560, objective_1561, objective_1562, objective_1563, objective_1564, objective_1565, objective_1566, objective_1567, objective_1568, objective_1569, objective_157, objective_1570, objective_1571, objective_1572, objective_1573, objective_1574, objective_1575, objective_1576, objective_1577, objective_1578, objective_1579, objective_158, objective_1580, objective_1581, objective_1582, objective_1583, objective_1584, objective_1585, objective_1586, objective_1587, objective_1588, objective_1589, objective_159, objective_1590, objective_1591, objective_1592, objective_1593, objective_1594, objective_1595, objective_1596, objective_1597, objective_1598, objective_1599, objective_16, objective_160, objective_1600, objective_1601, objective_1602, objective_1603, objective_1604, objective_1605, objective_1606, objective_1607, objective_1608, objective_1609, objective_161, objective_1610, objective_1611, objective_1612, objective_1613, 
objective_1614, objective_1615, objective_1616, objective_1617, objective_1618, objective_1619, objective_162, objective_1620, objective_1621, objective_1622, objective_1623, objective_1624, objective_1625, objective_1626, objective_1627, objective_1628, objective_1629, objective_163, objective_1630, objective_1631, objective_1632, objective_1633, objective_1634, objective_1635, objective_1636, objective_1637, objective_1638, objective_1639, objective_164, objective_1640, objective_1641, objective_1642, objective_1643, objective_1644, objective_1645, objective_1646, objective_1647, objective_1648, objective_1649, objective_165, objective_1650, objective_1651, objective_1652, objective_1653, objective_1654, objective_1655, objective_1656, objective_1657, objective_1658, objective_1659, objective_166, objective_1660, objective_1661, objective_1662, objective_1663, objective_1664, objective_1665, objective_1666, objective_1667, objective_1668, objective_1669, objective_167, objective_1670, objective_1671, objective_1672, objective_1673, objective_1674, objective_1675, objective_1676, objective_1677, objective_1678, objective_1679, objective_168, objective_1680, objective_1681, objective_1682, objective_1683, objective_1684, objective_1685, objective_1686, objective_1687, objective_1688, objective_1689, objective_169, objective_1690, objective_1691, objective_1692, objective_1693, objective_1694, objective_1695, objective_1696, objective_1697, objective_1698, 
objective_1699, objective_17, objective_170, objective_1700, objective_1701, objective_1702, objective_1703, objective_1704, objective_1705, objective_1706, objective_1707, objective_1708, objective_1709, objective_171, objective_1710, objective_1711, objective_1712, objective_1713, objective_1714, objective_1715, objective_1716, objective_1717, objective_1718, objective_1719, objective_172, objective_1720, objective_1721, objective_1722, objective_1723, objective_1724, objective_1725, objective_1726, objective_1727, objective_1728, objective_1729, objective_173, objective_1730, objective_1731, objective_1732, objective_1733, objective_1734, objective_1735, objective_1736, objective_1737, objective_1738, objective_1739, objective_174, objective_1740, objective_1741, objective_1742, objective_1743, objective_1744, objective_1745, objective_1746, objective_1747, objective_1748, objective_1749, objective_175, objective_1750, objective_1751, objective_1752, objective_1753, objective_1754, objective_1755, objective_1756, objective_1757, objective_1758, objective_1759, objective_176, objective_1760, objective_1761, objective_1762, objective_1763, objective_1764, objective_1765, objective_1766, objective_1767, objective_1768, objective_1769, objective_177, objective_1770, objective_1771, objective_1772, objective_1773, objective_1774, objective_1775, objective_1776, objective_1777, objective_1778, objective_1779, objective_178, objective_1780, objective_1781, objective_1782, objective_1783, objective_1784, objective_1785, objective_1786, objective_1787, objective_1788, objective_1789, objective_179, objective_1790, objective_1791, objective_1792, objective_1793, objective_1794, objective_1795, objective_1796, objective_1797, objective_1798, objective_1799, objective_18, objective_180, objective_1800, objective_1801, objective_1802, objective_1803, objective_1804, objective_1805, objective_1806, objective_1807, objective_1808, objective_1809, objective_181, objective_1810, objective_1811, objective_1812, objective_1813, objective_1814, objective_1815, objective_1816, objective_1817, objective_1818, objective_1819, objective_182, objective_1820, objective_1821, objective_1822, objective_1823, objective_1824, objective_1825, objective_1826, objective_1827, objective_1828, objective_1829, objective_183, objective_1830, objective_1831, objective_1832, objective_1833, objective_1834, objective_1835, objective_1836, objective_1837, objective_1838, objective_1839, objective_184, objective_1840, objective_1841, objective_1842, objective_1843, objective_1844, objective_1845, objective_1846, objective_1847, objective_1848, objective_1849, objective_185, objective_1850, objective_1851, objective_1852, objective_1853, objective_1854, objective_1855, objective_1856, objective_1857, 
objective_1858, objective_1859, objective_186, objective_1860, objective_1861, objective_1862, objective_1863, objective_1864, objective_1865, objective_1866, objective_1867, objective_1868, objective_1869, objective_187, objective_1870, objective_1871, objective_1872, objective_1873, objective_1874, objective_1875, objective_1876, objective_1877, objective_1878, objective_1879, objective_188, objective_1880, objective_1881, objective_1882, objective_1883, objective_1884, objective_1885, objective_1886, objective_1887, objective_1888, objective_1889, objective_189, objective_1890, objective_1891, objective_1892, objective_1893, objective_1894, objective_1895, objective_1896, objective_1897, objective_1898, objective_1899, objective_19, objective_190, objective_1900, objective_1901, objective_1902, objective_1903, objective_1904, objective_1905, objective_1906, objective_1907, objective_1908, objective_1909, objective_191, objective_1910, objective_1911, objective_1912, objective_1913, objective_1914, objective_1915, objective_1916, objective_1917, objective_1918, objective_1919, objective_192, objective_1920, objective_1921, objective_1922, objective_1923, objective_1924, objective_1925, objective_1926, objective_1927, objective_1928, objective_1929, objective_193, objective_1930, objective_1931, objective_1932, objective_1933, objective_1934, objective_1935, objective_1936, objective_1937, objective_1938, objective_1939, objective_194, objective_1940, objective_1941, objective_1942, objective_1943, objective_1944, objective_1945, objective_1946, objective_1947, objective_1948, objective_1949, objective_195, objective_1950, objective_1951, objective_1952, objective_1953, objective_1954, objective_1955, objective_1956, objective_1957, objective_1958, objective_1959, objective_196, objective_1960, objective_1961, objective_1962, objective_1963, objective_1964, objective_1965, objective_1966, objective_1967, objective_1968, objective_1969, objective_197, objective_1970, objective_1971, objective_1972, objective_1973, objective_1974, objective_1975, objective_1976, objective_1977, objective_1978, objective_1979, objective_198, objective_1980, objective_1981, objective_1982, objective_1983, objective_1984, objective_1985, objective_1986, objective_1987, objective_1988, objective_1989, objective_199, objective_1990, objective_1991, 
objective_1992, objective_1993, objective_1994, objective_1995, objective_1996, objective_1997, objective_1998, objective_1999, objective_2, objective_20, objective_200, objective_2000, objective_2001, objective_2002, objective_2003, objective_2004, objective_2005, objective_2006, objective_2007, objective_2008, objective_2009, objective_201, objective_2010, objective_2011, objective_2012, objective_2013, objective_2014, objective_2015, objective_2016, objective_2017, objective_2018, objective_2019, objective_202, objective_2020, objective_2021, objective_2022, objective_2023, objective_2024, objective_2025, objective_2026, objective_2027, objective_2028, objective_2029, objective_203, objective_2030, objective_2031, objective_2032, objective_2033, objective_2034, objective_2035, objective_2036, objective_2037, objective_2038, objective_2039, objective_204, objective_2040, objective_2041, objective_2042, objective_2043, objective_2044, objective_2045, objective_2046, objective_2047, objective_2048, objective_2049, objective_205, objective_2050, objective_2051, objective_2052, objective_2053, objective_2054, objective_2055, objective_2056, objective_2057, objective_2058, objective_2059, objective_206, objective_2060, objective_2061, objective_2062, objective_2063, objective_2064, objective_2065, objective_2066, 
objective_2067, objective_2068, objective_2069, objective_207, objective_2070, objective_2071, objective_2072, objective_2073, objective_2074, objective_2075, objective_2076, objective_2077, objective_2078, objective_2079, objective_208, objective_2080, objective_2081, objective_2082, objective_2083, objective_2084, objective_2085, objective_2086, objective_2087, objective_2088, objective_2089, objective_209, objective_2090, objective_2091, objective_2092, objective_2093, objective_2094, objective_2095, objective_2096, objective_2097, objective_2098, objective_2099, objective_21, objective_210, objective_2100, objective_2101, objective_2102, objective_2103, objective_2104, objective_2105, objective_2106, objective_2107, objective_2108, objective_2109, objective_211, objective_2110, objective_2111, objective_2112, objective_2113, objective_2114, objective_2115, objective_2116, objective_2117, objective_2118, objective_2119, objective_212, objective_2120, objective_2121, objective_2122, objective_2123, objective_2124, objective_2125, objective_2126, objective_2127, objective_2128, objective_2129, objective_213, objective_2130, objective_2131, objective_2132, objective_2133, objective_2134, objective_2135, objective_2136, objective_2137, objective_2138, objective_2139, objective_214, objective_2140, objective_2141, objective_2142, objective_2143, objective_2144, objective_2145, objective_2146, objective_2147, objective_2148, objective_2149, objective_215, objective_2150, objective_2151, objective_2152, objective_2153, objective_2154, objective_2155, objective_2156, objective_2157, objective_2158, objective_2159, objective_216, objective_2160, objective_2161, objective_2162, objective_2163, objective_2164, objective_2165, objective_2166, objective_2167, objective_2168, objective_2169, objective_217, objective_2170, objective_2171, objective_2172, objective_2173, objective_2174, objective_2175, objective_2176, objective_2177, objective_2178, objective_2179, objective_218, objective_2180, objective_2181, objective_2182, objective_2183, objective_2184, objective_2185, objective_2186, objective_2187, objective_2188, objective_2189, objective_219, objective_2190, objective_2191, objective_2192, objective_2193, objective_2194, objective_2195, objective_2196, objective_2197, objective_2198, objective_2199, objective_22, objective_220, objective_2200, objective_2201, objective_2202, objective_2203, objective_2204, objective_2205, objective_2206, objective_2207, objective_2208, objective_2209, objective_221, objective_2210, objective_2211, objective_2212, objective_2213, objective_2214, objective_2215, objective_2216, objective_2217, objective_2218, objective_2219, objective_222, objective_2220, objective_2221, objective_2222, objective_2223, objective_2224, objective_2225, 
objective_2226, objective_2227, objective_2228, objective_2229, objective_223, objective_2230, objective_2231, objective_2232, objective_2233, objective_2234, objective_2235, objective_2236, objective_2237, objective_2238, objective_2239, objective_224, objective_2240, objective_2241, objective_2242, objective_2243, objective_2244, objective_2245, objective_2246, objective_2247, objective_2248, objective_2249, objective_225, objective_2250, objective_2251, objective_2252, objective_2253, objective_2254, objective_2255, objective_2256, objective_2257, objective_2258, objective_2259, objective_226, objective_2260, objective_2261, objective_2262, objective_2263, objective_2264, objective_2265, objective_2266, objective_2267, objective_2268, objective_2269, objective_227, objective_2270, objective_2271, objective_2272, objective_2273, objective_2274, objective_2275, objective_2276, objective_2277, objective_2278, objective_2279, objective_228, objective_2280, objective_2281, objective_2282, objective_2283, objective_2284, objective_2285, objective_2286, objective_2287, objective_2288, objective_2289, objective_229, objective_2290, objective_2291, objective_2292, objective_2293, objective_2294, objective_2295, objective_2296, objective_2297, objective_2298, objective_2299, objective_23, objective_230, objective_2300, objective_2301, objective_2302, objective_2303, objective_2304, objective_2305, objective_2306, objective_2307, objective_2308, objective_2309, objective_231, objective_2310, objective_2311, objective_2312, objective_2313, objective_2314, objective_2315, objective_2316, objective_2317, objective_2318, objective_2319, objective_232, objective_2320, objective_2321, objective_2322, objective_2323, objective_2324, objective_2325, objective_2326, objective_2327, objective_2328, objective_2329, objective_233, objective_2330, objective_2331, objective_2332, objective_2333, objective_2334, objective_2335, objective_2336, objective_2337, objective_2338, objective_2339, objective_234, objective_2340, objective_2341, objective_2342, objective_2343, objective_2344, objective_2345, objective_2346, objective_2347, objective_2348, objective_2349, objective_235, objective_2350, objective_2351, objective_2352, objective_2353, objective_2354, objective_2355, objective_2356, objective_2357, objective_2358, objective_2359, objective_236, 
objective_2360, objective_2361, objective_2362, objective_2363, objective_2364, objective_2365, objective_2366, objective_2367, objective_2368, objective_2369, objective_237, objective_2370, objective_2371, objective_2372, objective_2373, objective_2374, objective_2375, objective_2376, objective_2377, objective_2378, objective_2379, objective_238, objective_2380, objective_2381, objective_2382, objective_2383, objective_2384, objective_2385, objective_2386, objective_2387, objective_2388, objective_2389, objective_239, objective_2390, objective_2391, objective_2392, objective_2393, objective_2394, objective_2395, objective_2396, objective_2397, objective_2398, objective_2399, objective_24, objective_240, objective_2400, objective_2401, objective_2402, objective_2403, objective_2404, objective_2405, objective_2406, objective_2407, objective_2408, objective_2409, objective_241, objective_2410, objective_2411, objective_2412, objective_2413, objective_2414, objective_2415, objective_2416, objective_2417, objective_2418, objective_2419, objective_242, objective_2420, objective_2421, objective_2422, objective_2423, objective_2424, objective_2425, objective_2426, objective_2427, objective_2428, objective_2429, objective_243, objective_2430, objective_2431, objective_2432, objective_2433, objective_2434, objective_2435, objective_2436, objective_2437, objective_2438, objective_2439, objective_244, objective_2440, objective_2441, objective_2442, objective_2443, objective_2444, objective_2445, objective_2446, objective_2447, objective_2448, objective_2449, objective_245, objective_2450, objective_2451, objective_2452, objective_2453, objective_2454, objective_2455, objective_2456, objective_2457, objective_2458, objective_2459, objective_246, objective_2460, objective_2461, objective_2462, objective_2463, objective_2464, objective_2465, objective_2466, objective_2467, objective_2468, objective_2469, 
objective_247, objective_2470, objective_2471, objective_2472, objective_2473, objective_2474, objective_2475, objective_2476, objective_2477, objective_2478, objective_2479, objective_248, objective_2480, objective_2481, objective_2482, objective_2483, objective_2484, objective_2485, objective_2486, objective_2487, objective_2488, objective_2489, objective_249, objective_2490, objective_2491, objective_2492, objective_2493, objective_2494, objective_2495, objective_2496, objective_2497, objective_2498, objective_2499, objective_25, objective_250, objective_2500, objective_2501, objective_2502, objective_2503, objective_2504, objective_2505, objective_2506, objective_2507, objective_2508, objective_2509, objective_251, objective_2510, objective_2511, objective_2512, objective_2513, objective_2514, objective_2515, objective_2516, objective_2517, objective_2518, objective_2519, objective_252, objective_2520, objective_2521, objective_2522, objective_2523, objective_2524, objective_2525, objective_2526, objective_2527, objective_2528, objective_2529, objective_253, objective_2530, objective_2531, objective_2532, objective_2533, objective_2534, objective_2535, objective_2536, objective_2537, objective_2538, objective_2539, objective_254, objective_2540, objective_2541, objective_2542, objective_2543, objective_2544, objective_2545, objective_2546, objective_2547, objective_2548, objective_2549, objective_255, objective_2550, objective_2551, objective_2552, objective_2553, objective_2554, objective_2555, objective_2556, objective_2557, objective_2558, objective_2559, objective_256, objective_2560, objective_2561, objective_2562, objective_2563, objective_2564, objective_2565, objective_2566, objective_2567, objective_2568, objective_2569, objective_257, objective_2570, objective_2571, objective_2572, objective_2573, objective_2574, objective_2575, objective_2576, objective_2577, objective_2578, objective_2579, objective_258, objective_2580, objective_2581, objective_2582, objective_2583, objective_2584, objective_2585, objective_2586, objective_2587, objective_2588, objective_2589, objective_259, objective_2590, objective_2591, objective_2592, objective_2593, objective_2594, objective_2595, objective_2596, objective_2597, objective_2598, objective_2599, objective_26, objective_260, objective_2600, objective_2601, objective_2602, objective_2603, objective_2604, objective_2605, objective_2606, objective_2607, objective_2608, objective_2609, objective_261, objective_2610, objective_2611, objective_2612, objective_2613, objective_2614, objective_2615, objective_2616, objective_2617, objective_2618, objective_2619, objective_262, objective_2620, objective_2621, objective_2622, objective_2623, objective_2624, objective_2625, objective_2626, objective_2627, objective_2628, 
objective_2629, objective_263, objective_2630, objective_2631, objective_2632, objective_2633, objective_2634, objective_2635, objective_2636, objective_2637, objective_2638, objective_2639, objective_264, objective_2640, objective_2641, objective_2642, objective_2643, objective_2644, objective_2645, objective_2646, objective_2647, objective_2648, objective_2649, objective_265, objective_2650, objective_2651, objective_2652, objective_2653, objective_2654, objective_2655, objective_2656, objective_2657, objective_2658, objective_2659, objective_266, objective_2660, objective_2661, objective_2662, objective_2663, objective_2664, objective_2665, objective_2666, objective_2667, objective_2668, objective_2669, objective_267, objective_2670, objective_2671, objective_2672, objective_2673, objective_2674, objective_2675, objective_2676, objective_2677, objective_2678, objective_2679, objective_268, objective_2680, objective_2681, objective_2682, objective_2683, objective_2684, objective_2685, objective_2686, objective_2687, objective_2688, objective_2689, objective_269, objective_2690, objective_2691, objective_2692, objective_2693, objective_2694, objective_2695, objective_2696, objective_2697, objective_2698, objective_2699, objective_27, objective_270, objective_2700, objective_2701, objective_2702, objective_2703, objective_2704, objective_2705, objective_2706, objective_2707, objective_2708, objective_2709, objective_271, objective_2710, objective_2711, objective_2712, objective_2713, objective_2714, objective_2715, objective_2716, objective_2717, objective_2718, objective_2719, objective_272, objective_2720, objective_2721, objective_2722, objective_2723, objective_2724, objective_2725, objective_2726, objective_2727, objective_2728, objective_2729, objective_273, objective_2730, objective_2731, objective_2732, objective_2733, objective_2734, objective_2735, objective_2736, objective_2737, objective_2738, objective_2739, objective_274, objective_2740, objective_2741, objective_2742, objective_2743, objective_2744, objective_2745, objective_2746, objective_2747, objective_2748, objective_2749, objective_275, objective_2750, objective_2751, objective_2752, objective_2753, objective_2754, objective_2755, objective_2756, objective_2757, objective_2758, objective_2759, objective_276, objective_2760, objective_2761, objective_2762, 
objective_2763, objective_2764, objective_2765, objective_2766, objective_2767, objective_2768, objective_2769, objective_277, objective_2770, objective_2771, objective_2772, objective_2773, objective_2774, objective_2775, objective_2776, objective_2777, objective_2778, objective_2779, objective_278, objective_2780, objective_2781, objective_2782, objective_2783, objective_2784, objective_2785, objective_2786, objective_2787, objective_2788, objective_2789, objective_279, objective_2790, objective_2791, objective_2792, objective_2793, objective_2794, objective_2795, objective_2796, objective_2797, objective_2798, objective_2799, objective_28, objective_280, objective_2800, objective_2801, objective_2802, objective_2803, objective_2804, objective_2805, objective_2806, objective_2807, objective_2808, objective_2809, objective_281, objective_2810, objective_2811, objective_2812, objective_2813, objective_2814, objective_2815, objective_2816, objective_2817, objective_2818, objective_2819, objective_282, objective_2820, objective_2821, objective_2822, objective_2823, objective_2824, objective_2825, objective_2826, objective_2827, objective_2828, objective_2829, objective_283, objective_2830, objective_2831, objective_2832, objective_2833, objective_2834, objective_2835, objective_2836, objective_2837, objective_2838, objective_2839, objective_284, objective_2840, objective_2841, objective_2842, objective_2843, objective_2844, objective_2845, objective_2846, objective_2847, objective_2848, objective_2849, objective_285, objective_2850, objective_2851, objective_2852, objective_2853, objective_2854, objective_2855, objective_2856, objective_2857, objective_2858, objective_2859, objective_286, objective_2860, objective_2861, objective_2862, objective_2863, objective_2864, objective_2865, objective_2866, objective_2867, objective_2868, objective_2869, objective_287, objective_2870, objective_2871, objective_2872, objective_2873, objective_2874, objective_2875, objective_2876, objective_2877, objective_2878, objective_2879, objective_288, objective_2880, objective_2881, objective_2882, objective_2883, objective_2884, objective_2885, objective_2886, objective_2887, objective_2888, objective_2889, objective_289, objective_2890, objective_2891, objective_2892, objective_2893, objective_2894, objective_2895, objective_2896, objective_2897, objective_2898, objective_2899, objective_29, objective_290, objective_2900, objective_2901, objective_2902, objective_2903, objective_2904, objective_2905, objective_2906, objective_2907, objective_2908, objective_2909, objective_291, objective_2910, objective_2911, objective_2912, objective_2913, objective_2914, objective_2915, objective_2916, objective_2917, objective_2918, objective_2919, objective_292, objective_2920, objective_2921, 
objective_2922, objective_2923, objective_2924, objective_2925, objective_2926, objective_2927, objective_2928, objective_2929, objective_293, objective_2930, objective_2931, objective_2932, objective_2933, objective_2934, objective_2935, objective_2936, objective_2937, objective_2938, objective_2939, objective_294, objective_2940, objective_2941, objective_2942, objective_2943, objective_2944, objective_2945, objective_2946, objective_2947, objective_2948, objective_2949, objective_295, objective_2950, objective_2951, objective_2952, objective_2953, objective_2954, objective_2955, objective_2956, objective_2957, objective_2958, objective_2959, objective_296, objective_2960, objective_2961, objective_2962, objective_2963, objective_2964, objective_2965, objective_2966, objective_2967, objective_2968, objective_2969, objective_297, objective_2970, objective_2971, objective_2972, objective_2973, objective_2974, objective_2975, objective_2976, objective_2977, objective_2978, objective_2979, objective_298, objective_2980, objective_2981, objective_2982, objective_2983, objective_2984, objective_2985, objective_2986, objective_2987, objective_2988, objective_2989, objective_299, objective_2990, objective_2991, objective_2992, objective_2993, objective_2994, objective_2995, objective_2996, objective_2997, objective_2998, objective_2999, objective_3, objective_30, objective_300, objective_3000, objective_3001, objective_3002, objective_3003, objective_3004, objective_3005, objective_3006, objective_3007, objective_3008, objective_3009, objective_301, objective_3010, objective_3011, objective_3012, objective_3013, objective_3014, objective_3015, objective_3016, objective_3017, objective_3018, objective_3019, objective_302, objective_3020, objective_3021, objective_3022, objective_3023, objective_3024, objective_3025, objective_3026, objective_3027, objective_3028, objective_3029, objective_303, objective_3030, objective_3031, objective_3032, objective_3033, objective_3034, objective_3035, objective_3036, objective_3037, objective_3038, objective_3039, objective_304, objective_3040, objective_3041, objective_3042, objective_3043, objective_3044, objective_3045, objective_3046, objective_3047, objective_3048, objective_3049, objective_305, objective_3050, objective_3051, objective_3052, objective_3053, objective_3054, objective_3055, objective_3056, objective_3057, objective_3058, objective_3059, objective_306, objective_3060, objective_3061, objective_3062, objective_3063, objective_3064, objective_3065, objective_3066, objective_3067, objective_3068, objective_3069, objective_307, objective_3070, objective_3071, objective_3072, objective_3073, objective_3074, objective_3075, objective_3076, objective_3077, objective_3078, objective_3079, objective_308, objective_3080, objective_3081, objective_3082, objective_3083, objective_3084, objective_3085, objective_3086, objective_3087, objective_3088, objective_3089, objective_309, objective_3090, objective_3091, objective_3092, objective_3093, objective_3094, objective_3095, objective_3096, objective_3097, objective_3098, objective_3099, objective_31, objective_310, objective_3100, objective_3101, objective_3102, objective_3103, objective_3104, objective_3105, objective_3106, objective_3107, objective_3108, objective_3109, objective_311, objective_3110, objective_3111, objective_3112, objective_3113, objective_3114, objective_3115, objective_3116, objective_3117, objective_3118, objective_3119, objective_312, objective_3120, objective_3121, objective_3122, objective_3123, objective_3124, objective_3125, objective_3126, objective_3127, objective_3128, objective_3129, objective_313, objective_3130, 
objective_3131, objective_3132, objective_3133, objective_3134, objective_3135, objective_3136, objective_3137, objective_3138, objective_3139, objective_314, objective_3140, objective_3141, objective_3142, objective_3143, objective_3144, objective_3145, objective_3146, objective_3147, objective_3148, objective_3149, objective_315, objective_3150, objective_3151, objective_3152, objective_3153, objective_3154, objective_3155, objective_3156, objective_3157, objective_3158, objective_3159, objective_316, objective_3160, objective_3161, objective_3162, objective_3163, objective_3164, objective_3165, objective_3166, objective_3167, objective_3168, objective_3169, objective_317, objective_3170, objective_3171, objective_3172, objective_3173, objective_3174, objective_3175, objective_3176, objective_3177, objective_3178, objective_3179, objective_318, objective_3180, objective_3181, objective_3182, objective_3183, objective_3184, objective_3185, objective_3186, objective_3187, objective_3188, objective_3189, objective_319, objective_3190, objective_3191, objective_3192, objective_3193, objective_3194, objective_3195, objective_3196, objective_3197, objective_3198, objective_3199, objective_32, objective_320, objective_3200, objective_3201, objective_3202, objective_3203, objective_3204, objective_3205, objective_3206, objective_3207, objective_3208, objective_3209, objective_321, objective_3210, objective_3211, objective_3212, objective_3213, objective_3214, objective_3215, objective_3216, objective_3217, objective_3218, objective_3219, objective_322, objective_3220, objective_3221, objective_3225, objective_3226, objective_3227, objective_3228, objective_3229, objective_323, objective_3230, objective_3231, objective_3232, objective_3233, objective_3234, objective_3235, objective_3236, objective_3237, objective_3238, objective_3239, objective_324, objective_3240, objective_3241, objective_3242, objective_3243, objective_3244, objective_3245, objective_3246, objective_3247, objective_3248, objective_3249, objective_325, objective_3250, objective_3251, objective_3252, objective_3253, objective_3254, objective_3255, objective_3256, objective_3257, objective_3258, objective_3259, objective_326, objective_3260, objective_3261, objective_3262, objective_3263, objective_3264, objective_3265, objective_3266, objective_3267, objective_3268, objective_3269, objective_327, objective_3270, objective_3271, objective_3272, objective_3273, objective_3274, objective_3275, objective_3276, objective_3277, objective_3278, objective_3279, objective_328, objective_3280, objective_3281, objective_3282, objective_3283, objective_3284, objective_3285, objective_3286, objective_3287, objective_329, objective_33, objective_330, objective_331, objective_332, objective_333, objective_334, objective_335, objective_336, objective_337, objective_338, objective_339, objective_34, objective_340, objective_341, objective_342, objective_343, objective_344, objective_345, objective_346, objective_347, objective_348, objective_349, objective_35, objective_350, objective_351, objective_352, objective_353, objective_354, objective_355, objective_356, objective_357, objective_358, objective_359, objective_36, objective_360, objective_361, objective_362, objective_363, objective_364, objective_365, objective_366, objective_367, objective_368, objective_369, objective_37, objective_370, objective_371, objective_372, objective_373, objective_374, objective_375, objective_376, objective_377, objective_378, objective_379, objective_38, 
objective_380, objective_381, objective_382, objective_383, objective_384, objective_385, objective_386, objective_387, objective_388, objective_389, objective_39, objective_390, objective_391, objective_392, objective_393, objective_394, objective_395, objective_396, objective_397, objective_398, objective_399, objective_4, objective_40, objective_400, objective_401, objective_402, objective_403, objective_404, objective_405, objective_406, objective_407, objective_408, objective_409, objective_41, objective_410, objective_411, objective_412, objective_413, objective_414, objective_415, objective_416, objective_417, objective_418, objective_419, objective_42, objective_420, objective_421, objective_422, objective_423, objective_424, objective_425, objective_426, objective_427, objective_428, objective_429, objective_43, objective_430, objective_431, objective_432, objective_433, objective_434, objective_435, objective_436, objective_437, objective_438, objective_439, objective_44, objective_440, objective_441, objective_442, objective_443, objective_444, objective_445, objective_446, objective_447, objective_448, objective_449, objective_45, objective_450, objective_451, objective_452, objective_453, objective_454, objective_455, objective_456, objective_457, objective_458, objective_459, objective_46, objective_460, objective_461, objective_462, objective_463, objective_464, objective_465, objective_466, objective_467, objective_468, objective_469, objective_47, objective_470, objective_471, objective_472, objective_473, objective_474, objective_475, objective_476, objective_477, objective_478, objective_479, objective_48, objective_480, objective_481, objective_482, objective_483, objective_484, objective_485, objective_486, objective_487, objective_488, objective_489, objective_49, objective_490, objective_491, objective_492, objective_493, objective_494, objective_495, objective_496, objective_497, objective_498, objective_499, objective_5, objective_50, objective_500, objective_501, objective_502, objective_503, objective_504, objective_505, objective_506, objective_507, objective_508, objective_509, objective_51, objective_510, objective_511, objective_512, objective_513, objective_514, objective_515, objective_516, objective_517, objective_518, objective_519, objective_52, objective_520, objective_521, objective_522, objective_523, objective_524, objective_525, objective_526, objective_527, objective_528, objective_529, objective_53, objective_530, objective_531, 
objective_532, objective_533, objective_534, objective_535, objective_536, objective_537, objective_538, objective_539, objective_54, objective_540, objective_541, objective_542, objective_543, objective_544, objective_545, objective_546, objective_547, objective_548, objective_549, objective_55, objective_550, objective_551, objective_552, objective_553, objective_554, objective_555, objective_556, objective_557, objective_558, objective_559, objective_56, objective_560, objective_561, objective_562, objective_563, objective_564, objective_565, objective_566, objective_567, objective_568, objective_569, objective_57, objective_570, objective_571, objective_572, objective_573, objective_574, objective_575, objective_576, objective_577, objective_578, objective_579, objective_58, objective_580, objective_581, objective_582, objective_583, objective_584, objective_585, objective_586, objective_587, objective_588, objective_589, objective_59, objective_590, objective_591, objective_592, objective_593, objective_594, objective_595, objective_596, objective_597, objective_598, objective_599, objective_6, objective_60, objective_600, objective_601, objective_602, objective_603, objective_604, objective_605, objective_606, objective_607, objective_608, objective_609, objective_61, objective_610, objective_611, objective_612, objective_613, objective_614, objective_615, objective_616, objective_617, objective_618, objective_619, objective_62, objective_620, objective_621, objective_622, objective_623, objective_624, objective_625, objective_626, objective_627, objective_628, objective_629, objective_63, objective_630, objective_631, objective_632, objective_633, objective_634, objective_635, objective_636, objective_637, objective_638, objective_639, objective_64, objective_640, objective_641, objective_642, objective_643, objective_644, objective_645, objective_646, objective_647, objective_648, objective_649, objective_65, objective_650, objective_651, objective_652, objective_653, objective_654, objective_655, objective_656, objective_657, objective_658, objective_659, objective_66, objective_660, objective_661, objective_662, objective_663, objective_664, objective_665, objective_666, 
objective_667, objective_668, objective_669, objective_67, objective_670, objective_671, objective_672, objective_673, objective_674, objective_675, objective_676, objective_677, objective_678, objective_679, objective_68, objective_680, objective_681, objective_682, objective_683, objective_684, objective_685, objective_686, objective_687, objective_688, objective_689, objective_69, objective_690, objective_691, objective_692, objective_693, objective_694, objective_695, objective_696, objective_697, objective_698, objective_699, objective_7, objective_70, objective_700, objective_701, objective_702, objective_703, objective_704, objective_705, objective_706, objective_707, objective_708, objective_709, objective_71, objective_710, objective_711, objective_712, objective_713, objective_714, objective_715, objective_716, objective_717, objective_718, objective_719, objective_72, objective_720, objective_721, objective_722, objective_723, objective_724, objective_725, objective_726, objective_727, objective_728, objective_729, objective_73, objective_730, objective_731, objective_732, objective_733, objective_734, objective_735, objective_736, objective_737, objective_738, objective_739, objective_74, objective_740, objective_741, objective_742, objective_743, objective_744, objective_745, objective_746, objective_747, objective_748, objective_749, objective_75, objective_750, objective_751, objective_752, objective_753, objective_754, objective_755, objective_756, objective_757, objective_758, objective_759, objective_76, objective_760, objective_761, objective_762, objective_763, objective_764, objective_765, objective_766, objective_767, objective_768, objective_769, objective_77, objective_770, objective_771, objective_772, objective_773, objective_774, objective_775, objective_776, objective_777, objective_778, objective_779, objective_78, objective_780, objective_781, objective_782, objective_783, objective_784, objective_785, objective_786, objective_787, objective_788, objective_789, objective_79, objective_790, objective_791, objective_792, objective_793, objective_794, objective_795, objective_796, objective_797, objective_798, objective_799, objective_8, objective_80, objective_800, objective_801, objective_802, objective_803, objective_804, objective_805, objective_806, objective_807, objective_808, objective_809, objective_81, objective_810, objective_811, objective_812, objective_813, objective_814, objective_815, objective_816, objective_817, objective_818, 
objective_819, objective_82, objective_820, objective_821, objective_822, objective_823, objective_824, objective_825, objective_826, objective_827, objective_828, objective_829, objective_83, objective_830, objective_831, objective_832, objective_833, objective_834, objective_835, objective_836, objective_837, objective_838, objective_839, objective_840, objective_841, objective_842, objective_843, objective_844, objective_845, objective_846, objective_847, objective_848, objective_849, objective_850, objective_851, objective_852, objective_853, objective_854, objective_855, objective_856, objective_857, objective_858, objective_859, objective_860, objective_861, objective_862, objective_863, objective_864, objective_865, objective_866, objective_867, objective_868, objective_869, objective_870, objective_871, objective_872, objective_873, objective_874, objective_875, objective_876, objective_877, objective_878, objective_879, objective_880, objective_881, objective_882, objective_883, objective_884, objective_885, objective_886, objective_887, objective_888, objective_889, objective_890, objective_891, objective_892, objective_893, objective_894, objective_895, objective_896, objective_897, objective_898, objective_899, objective_9, objective_900, objective_901, objective_902, objective_903, objective_904, objective_905, objective_906, objective_907, objective_908, objective_909, objective_910, objective_911, objective_912, objective_913, objective_914, objective_915, objective_916, objective_917, objective_918, objective_919, objective_920, objective_921, objective_922, objective_923, objective_924, objective_925, objective_926, objective_927, objective_928, objective_929, objective_930, objective_931, objective_932, objective_933, objective_934, objective_935, objective_936, objective_937, objective_938, objective_939, objective_940, objective_941, objective_942, objective_943, objective_944, objective_945, objective_946, objective_947, objective_948, objective_949, objective_950, objective_951, objective_952, objective_953, objective_954, objective_955, objective_956, objective_957, objective_958, objective_959, objective_960, objective_961, objective_962, objective_963, objective_964, objective_965, objective_966, objective_967, objective_968, objective_969, objective_970, objective_971, objective_972, objective_973, objective_974, objective_975, objective_976, objective_977, objective_978, objective_979, objective_980, objective_981, objective_982, objective_983, 
objective_984, objective_985, objective_986, objective_987, objective_988, objective_989, objective_990, objective_991, objective_992, objective_993, objective_994, objective_995, objective_996, objective_997, objective_998, objective_999]