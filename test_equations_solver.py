import unittest
import numpy.testing as npt
import numpy as np

from solver import get_solutions, evaluate_solver_equation


# class TestEquationsSolverRunAndEvaluation2D(unittest.TestCase):
#     def test_solver_runs_correctly(self) -> None:

#         x_data = np.array([
#             2.35237,
#             2.29363,
#             2.28363,
#             2.26098,
#             2.24592,
#             2.31062,
#             2.33417,
#             2.36682,
#             2.33781,
#             2.33164,
#             2.38865,
#             2.43849,
#             2.43161,
#             2.42777,
#             2.40816,
#             2.37814,
#             2.37278,
#             2.39401,
#             2.37794,
#             2.32952
#         ])

#         y_data = np.array([
#             38.714,
#             39.3818,
#             41.4955,
#             42.6163,
#             42.744,
#             42.3376,
#             40.0728,
#             38.894,
#             41.9369,
#             50.2641,
#             58.301,
#             60.2696,
#             61.3845,
#             61.3555,
#             57.6738,
#             49.666,
#             40.5432,
#             36.908,
#             39.4805,
#             45.4094
#         ])

#         solver_res = get_solutions({}, x_data, y_data, rows_count=1)

#         # должны быть найдено по одному решению для всех пяти типов функций
#         self.assertTrue(len(solver_res) == 5)

#         # должны быть получены значения по численному решению
#         test_x_values = np.array([
#             2.2,
#             2.22,
#             2.25,
#             2.3
#         ])

#         ref_square_values = [
#             (2.20, 34.348),
#             (2.22, 39.321),
#             (2.25, 42.412),
#             (2.30, 42.257)
#         ]

#         ref_sqrt_values = [
#             (2.20, 54.648),
#             (2.22, 49.61),
#             (2.25, 44.264),
#             (2.30, 40.423)
#         ]

#         ref_simple_values = [
#             (2.20, 42.1),
#             (2.22, 42.204),
#             (2.25, 42.304),
#             (2.30, 42.274)
#         ]

#         ref_ln_values = [
#             (2.20, 38.038),
#             (2.22, 40.863),
#             (2.25, 42.95),
#             (2.30, 42.805)
#         ]

#         ref_inv_values = [
#             (2.20, 53.172),
#             (2.22, 48.646),
#             (2.25, 44.267),
#             (2.30, 41.211)
#         ]
#         # print(solver_res)

#         # возьмем из результатов каждую подгруппу функций
#         res_formula_square = solver_res[0]['formula_with_coefficients']
#         res_formula_sqrt = solver_res[1]['formula_with_coefficients']
#         res_formula_simple = solver_res[2]['formula_with_coefficients']
#         res_formula_ln = solver_res[3]['formula_with_coefficients']
#         res_formula_inv = solver_res[4]['formula_with_coefficients']

#         formula_square_results = evaluate_solver_equation({}, res_formula_square, test_x_values)
#         formula_sqrt_results = evaluate_solver_equation({}, res_formula_sqrt, test_x_values)
#         formula_simple_results = evaluate_solver_equation({}, res_formula_simple, test_x_values)
#         formula_ln_results = evaluate_solver_equation({}, res_formula_ln, test_x_values)
#         formula_inv_results = evaluate_solver_equation({}, res_formula_inv, test_x_values)

#         # сравним значения и референс по каждой подгруппе
#         npt.assert_allclose(formula_square_results, ref_square_values, atol=0.001)
#         npt.assert_allclose(formula_sqrt_results, ref_sqrt_values, atol=0.001)
#         npt.assert_allclose(formula_simple_results, ref_simple_values, atol=0.001)
#         npt.assert_allclose(formula_ln_results, ref_ln_values, atol=0.001)
#         npt.assert_allclose(formula_inv_results, ref_inv_values, atol=0.001)


class TestEquationsSolverRunAndEvaluation3D(unittest.TestCase):
    def test_solver_runs_correctly(self) -> None:

        x_data = np.array([
            0.2357,
            0.2385,
            0.238,
            0.2355,
            0.2397,
            0.2441,
            0.2478,
            0.2536,
            0.2558,
            0.254,
            0.2499,
            0.2437,
            0.2387,
            0.2346,
            0.2263,
            0.2159,
            0.2242,
            0.2447,
            0.2515,
            0.2416,
        ])

        y_data = np.array([
            2.3878,
            2.3196,
            2.3012,
            2.3032,
            2.3088,
            2.3914,
            2.4479,
            2.4497,
            2.4178,
            2.448,
            2.3864,
            2.3485,
            2.4053,
            2.4863,
            2.4833,
            2.4739,
            2.5254,
            2.409,
            2.433,
            2.4087,
        ])

        z_data = np.array([
            96.5612,
            100.2544,
            99.7177,
            98.5717,
            104.0823,
            117.2733,
            127.875,
            131.7995,
            127.7468,
            115.2782,
            102.9339,
            97.4246,
            99.5319,
            102.1294,
            97.2883,
            93.2749,
            96.7599,
            103.353,
            105.3867,
            100.0734,

        ])

        solver_res = get_solutions({}, x_data, y_data, z_data, rows_count=1)
        print(solver_res)

        # должны быть найдено по одному решению для всех трех типов 3D функций тз файла 
        self.assertTrue(len(solver_res) == 3)

        # должны быть получены значения по численному решению
        test_x_values = np.array([
            2.2,
            2.22,
            2.25,
            2.3
        ])

        ref_square_values = [
            (2.20, 34.348),
            (2.22, 39.321),
            (2.25, 42.412),
            (2.30, 42.257)
        ]

        ref_sqrt_values = [
            (2.20, 54.648),
            (2.22, 49.61),
            (2.25, 44.264),
            (2.30, 40.423)
        ]

        ref_simple_values = [
            (2.20, 42.1),
            (2.22, 42.204),
            (2.25, 42.304),
            (2.30, 42.274)
        ]

        ref_ln_values = [
            (2.20, 38.038),
            (2.22, 40.863),
            (2.25, 42.95),
            (2.30, 42.805)
        ]

        ref_inv_values = [
            (2.20, 53.172),
            (2.22, 48.646),
            (2.25, 44.267),
            (2.30, 41.211)
        ]
        # print(solver_res)

        # возьмем из результатов каждую подгруппу функций
        res_formula_square = solver_res[0]['formula_with_coefficients']
        res_formula_sqrt = solver_res[1]['formula_with_coefficients']
        res_formula_simple = solver_res[2]['formula_with_coefficients']
        res_formula_ln = solver_res[3]['formula_with_coefficients']
        res_formula_inv = solver_res[4]['formula_with_coefficients']

        formula_square_results = evaluate_solver_equation({}, res_formula_square, test_x_values)
        formula_sqrt_results = evaluate_solver_equation({}, res_formula_sqrt, test_x_values)
        formula_simple_results = evaluate_solver_equation({}, res_formula_simple, test_x_values)
        formula_ln_results = evaluate_solver_equation({}, res_formula_ln, test_x_values)
        formula_inv_results = evaluate_solver_equation({}, res_formula_inv, test_x_values)

        print(formula_square_results)
        print()
        print(formula_sqrt_results)
        print()
        print(formula_simple_results)
        print()
        print(formula_ln_results)
        print()
        print(formula_inv_results)
        print()

        # сравним значения и референс по каждой подгруппе
        npt.assert_allclose(formula_square_results, ref_square_values, atol=0.001)
        npt.assert_allclose(formula_sqrt_results, ref_sqrt_values, atol=0.001)
        npt.assert_allclose(formula_simple_results, ref_simple_values, atol=0.001)
        npt.assert_allclose(formula_ln_results, ref_ln_values, atol=0.001)
        npt.assert_allclose(formula_inv_results, ref_inv_values, atol=0.001)


if __name__ == "__main__":
    unittest.main()
