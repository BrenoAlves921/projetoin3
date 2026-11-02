
def is_root(r: float, a: float, b: float, c: float) -> bool:
    return a * r**2 + b * r + c == 0


def main():
    print(is_root(0.0, 1.0, -3.0, 2.0))
    print(is_root(1.0, 1.0, -3.0, 2.0))


main()