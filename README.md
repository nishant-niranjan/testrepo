# Prime Number Checker

A simple prime number checker, available as both a CLI script and a static web UI.

## Contents

- `prime_checker.py` — command-line version.
- `index.html` — static, no-backend web UI (open directly in a browser).
- `test_prime_checker.py` — pytest suite for the core primality logic.

## CLI

Run:

```
python3 prime_checker.py
```

**Input:** one line of space-separated integers, e.g.

```
Enter numbers separated by spaces: 2 3 4 17 91
```

**Output:** one line per number:

```
2 is a prime number
3 is a prime number
4 is not a prime number
17 is a prime number
91 is not a prime number
```

A token that isn't a valid integer prints:

```
abc is not a valid integer
```

## Web UI

Open `index.html` in a browser. No build step or server required.

**Input:** one integer at a time, typed into the text box and submitted with the "Check" button or the Enter key.

**Output:** a new result line is appended below the input box each time, e.g.:

```
7 is a prime number
```

Prime results are shown in green, non-prime results in gray. Entering something that isn't a valid integer (e.g. `abc`) shows an inline message like `"abc" is not a valid integer` instead of adding a result line.

## Tests

Install the test dependency and run the suite:

```
pip install -r requirements.txt
python3 -m pytest test_prime_checker.py -v
```
