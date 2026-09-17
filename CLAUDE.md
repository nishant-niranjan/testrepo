# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Small standalone prime-number checker implemented twice, independently:

- `prime_checker.py` — CLI version. `is_prime(n)` is the core logic (trial division up to √n, special-cased for n<2, 2, 3, and even numbers). `main()` reads one line of space-separated numbers and prints prime/not-prime for each.
- `index.html` — static, no-backend web UI with the same primality logic reimplemented in inline JavaScript (`isPrime()`). One number is entered/checked at a time via a text input + button (or Enter key), with results appended to a running list. Open the file directly in a browser; no build or server needed.

These two implementations are **not shared** — `is_prime` in Python and `isPrime` in JS are separate code paths. If the primality algorithm changes, update both.

## Commands

Install test dependency:
```
pip install -r requirements.txt
```

Run the test suite:
```
python3 -m pytest test_prime_checker.py -v
```

Run a single test case (by parametrized id, e.g. `n=97`):
```
python3 -m pytest test_prime_checker.py -v -k "97"
```

Run the CLI:
```
python3 prime_checker.py
```

## Testing notes

`test_prime_checker.py` only tests `is_prime` in `prime_checker.py` (imported directly, no I/O involved) via `pytest.mark.parametrize`. There is no test coverage for `index.html`'s JS or for `main()`'s I/O handling.
