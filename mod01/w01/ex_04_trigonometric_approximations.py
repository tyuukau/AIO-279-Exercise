def factorial(x: int) -> int:
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result


def approx_sin(x: float, n: int) -> float:
    result = 0
    for i in range(n):
        result += (-1) ** i * x ** (2 * i + 1) / factorial(2 * i + 1)
    return result


def approx_cos(x: float, n: int) -> float:
    result = 0
    for i in range(n):
        result += (-1) ** i * x ** (2 * i) / factorial(2 * i)
    return result


def approx_sinh(x: float, n: int) -> float:
    result = 0
    for i in range(n):
        result += x ** (2 * i + 1) / factorial(2 * i + 1)
    return result


def approx_cosh(x: float, n: int) -> float:
    result = 0
    for i in range(n):
        result += x ** (2 * i) / factorial(2 * i)
    return result


if __name__ == "__main__":
    assert round(approx_sin(x=3.14, n=10), 5) == 0.00159

    print("Approximation of sin(3.14):", approx_sin(x=3.14, n=10))
    print("Approximation of cos(3.14):", approx_cos(x=3.14, n=10))
    print("Approximation of sinh(3.14):", approx_sinh(x=3.14, n=10))
    print("Approximation of cosh(3.14):", approx_cosh(x=3.14, n=10))
