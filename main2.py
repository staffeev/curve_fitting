from pandas import read_excel
from scipy.optimize import curve_fit
import numpy as np
from numpy import log
import timeit
import asyncio
import threading 

import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())


def objective(x, a, b, c, d, e, f):
	return a + b / log(x) + c / (log(x) ** 2) + d / (log(x) ** 3) + e / (log(x) ** 4) + f / (log(x) ** 5)


async def main():
    dataframe = read_excel("points.xls", dtype=np.float64)
    x, y = dataframe["X"], dataframe["Y"]
    results = await asyncio.gather(
         curve_fit(objective, x, y)
    )
    print(len(results))


def test():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        loop.run_until_complete(loop.shutdown_asyncgens())
    finally:
        loop.close()


dataframe = read_excel("points.xls", dtype=np.float64)
x, y = dataframe["X"], dataframe["Y"]
pool = mp.Pool(mp.cpu_count())
pool.apply(curve_fit, args=(objective, x, y))

# results = [pool.apply(curve_fit, args=(objective, x, y)) for _ in range(10)]
pool.close()
# print(results)
# a = [threading.Thread(target=curve_fit, args=(objective, x, y)) for _ in range(1000)]
# [x.start() for x in a]
# print("AA")

