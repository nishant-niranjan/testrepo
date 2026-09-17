"""Check whether numbers entered by the user are prime."""


def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, int(n ** 0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def main():
    raw = input("Enter numbers separated by spaces: ")
    for token in raw.split():
        try:
            n = int(token)
        except ValueError:
            print(f"{token} is not a valid integer")
            continue
        result = "is a prime number" if is_prime(n) else "is not a prime number"
        print(f"{n} {result}")


if __name__ == "__main__":
    main()
