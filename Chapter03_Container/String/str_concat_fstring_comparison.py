from timeit import timeit

import matplotlib.pyplot as plt


n = 1000000000

setup = """\
a = [1 for _ in range({l})]
b = [1 for _ in range({l})]
"""

fstr_stmt = """\
f'{a}{b}'
"""

concat_stmt = """\
str(a)+str(b)
"""

str_lens = [10, 100, 1000, 2000]
fstr_t = []
concat_t = []
for l in str_lens:  # noqa: E741
    n_iters = n // l
    fstr_t.append(
        timeit(setup=setup.format(l=l), stmt=fstr_stmt, number=n_iters)
        / n_iters
    )
    concat_t.append(
        timeit(
            setup=setup.format(l=l),
            stmt=concat_stmt,
            number=n_iters,
        )
        / n_iters
    )
    ratio = fstr_t[-1] / concat_t[-1]
    print(
        f"For two strings of length {l:7d}, concatenation is "
        f"{ratio:.5f} times faster than f-strings"
    )
plt.plot(str_lens, fstr_t, "r*-")
plt.plot(str_lens, concat_t, "c*-")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("String length (log scale)")
plt.ylabel("Seconds per iteration (log scale)")
plt.grid()
plt.show()
