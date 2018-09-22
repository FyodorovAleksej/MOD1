import matplotlib.pyplot as plt
import numpy as np


def gen_i(__ri: int, __m: int, __a: int):
    si = __a * __ri
    rn = si % __m
    return rn


def gen_list(__m: int, __a: int, __r0: int, __n: int):
    rn = gen_i(__r0, __m, __a)
    res = [rn / float(__m)]
    for _ in range(0, __n - 1):
        rn = gen_i(rn, __m, __a)
        res.append(rn / float(__m))
    return res


def mat_ozh(__res: list):
    return sum(__res) / float(len(__res))


def disp(__res: list, __x_mean: float):
    __temp = [(i - __x_mean) ** 2 for i in __res]
    n = len(__temp)
    d = sum(__temp) / float(len(__temp))
    return (d * n) / float(n - 1)


def period_length(__m: int, __a: int, __r0: int, __v: int):
    vList = gen_list(__m, __a, __r0, __v)
    lastValue = vList[-1]
    for i in range(0, len(vList)):
        if vList[i] == lastValue:
            for j in range(i + 1, len(vList)):
                if vList[j] == vList[i]:
                    return j - i
            return len(vList)
    return len(vList)


def sqrt(__x: float):
    return np.math.sqrt(__x)


def k_res(__res: list):
    k = 0
    i = 0
    while i < len(__res) - 1:
        xi = __res[i]
        xi1 = __res[i + 1]
        if ((xi ** 2) + (xi1 ** 2)) > 1:
            k += 1
        i += 2
    return (2 * k) / float(len(__res))


def showHist(__res: list):
    step = 1 / float(20)
    plt.hist(__res, bins=[i * step for i in range(0, 21)])
    plt.savefig("resultHist.png")
    plt.show()


def aperiod_length(p: int, __res: list):
    i = 0
    while i + p < len(__res):
        if not (__res[i] == __res[i + p]):
            i += 1
        else:
            return i + p
    return i + p


if __name__ == "__main__":
    a = 134279
    r0 = 1
    m = 337109
    n = 1000000
    histn = 20

    res = gen_list(m, a, r0, n)
    x__mean = mat_ozh(res)
    d = disp(res, x__mean)
    period = period_length(m, a, r0, 1000000)
    print("matozh = ", x__mean)
    print("disp = ", d)
    print("SKO = ", sqrt(d))
    print("K = ", k_res(res))
    print("period = ", period)
    print("aperiod = ", aperiod_length(period, res))
    showHist(res)
