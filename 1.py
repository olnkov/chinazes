import math
def f(x):
    return math.sin(10*x - 20) * math.exp(5) / (x-2)**2
def df(x):
    e5 = math.exp(5)
    term1 = 10 * math.cos(10*x - 20) * (x - 2)
    term2 = 2 * math.sin(10*x - 20)
    return e5 * (term1 - term2) / (x - 2)**3

def ddf(x):
    e5 = math.exp(5)
    dx = x - 2
    # Числитель второй производной
    term_sin = (6 - 100 * dx**2) * math.sin(10*x - 20)
    term_cos = 40 * dx * math.cos(10*x - 20)
    return e5 * (term_sin - term_cos) / dx**4

'''метод бисекции'''


def bisec(a, b, eps, max_it=100):
    iter = 0
    if f(a) * f(b) >= 0:
        print("отрезок не подходит")
        return None, iter, None

    while abs(b - a) > eps and iter < max_it:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter += 1

    x = (a + b) / 2
    res = abs(f(x))
    return x, iter, res

'''метод хорд и касательных'''


def chorde(a, b, eps=0.001, max_iter=100):
    iter = 0
    if df(a) * ddf(a) < 0:
        while b - a > 2 * eps and iter < max_iter:
            d = a - f(a) / df(a)
            c = b - f(b) * (b - a) / (f(b) - f(a))

            a, b = d, c
            iter += 1
    else:
        while b - a > 2 * eps and iter < max_iter:
            c = a - f(a) * (b - a) / (f(b) - f(a))
            d = b - f(b) / df(b)

            a, b = c, d
            iter += 1

    x = (a + b) / 2
    res = abs(f(x))
    return x, iter, res

"""метод итераций """


def iteration(a, b, eps=0.001, max_iter=100):
    x0 = (a + b) / 2

    h = 0.0001
    df_approx = (f(x0 + h) - f(x0)) / h

    # Выбираем lambda так, чтобы |1 - lambda * df_approx| < 1
    if abs(df_approx) > 0:
        lam = 1 / df_approx
        # Корректируем знак для обеспечения сходимости
        if (1 - lam * df_approx) > 0:
            lam = -lam
    else:
        lam = 0.1

    # Итерационный процесс
    x_prev = x0
    iter = 0

    for iter in range(max_iter):
        # Итерационная функция phi(x) = x - lambda * f(x)
        x_next = x_prev - lam * f(x_prev)

        # Проверка сходимости
        if abs(x_next - x_prev) < eps:
            break

        x_prev = x_next

    x = x_next
    res = abs(f(x))
    return x, iter + 1, res

a = float(input("введите a: "))
b = float(input("введите b: "))
eps = float(input("введите точность: "))

print("метод бисекции:", bisec(a, b, eps))
print("метод хорд и касательных:", chorde(a, b))
print("метод итераций:", iteration(a, b))