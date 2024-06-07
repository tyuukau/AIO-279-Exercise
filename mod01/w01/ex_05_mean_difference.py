def md_nre_one_sample(y: float, y_hat: float, n: int, p: int) -> float:
    return (y ** (1 / n) - y_hat ** (1 / n)) ** p


if __name__ == "__main__":
    assert round(md_nre_one_sample(y=100, y_hat=99.5, n=2, p=1), 6) == 0.025031
    print(md_nre_one_sample(y=100, y_hat=99.5, n=2, p=1))
