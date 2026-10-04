# MLOps Lab 1 – GitHub Actions (CI/CD)

![Pytest](https://github.com/DiyaKaswa11/First_Lab/actions/workflows/pytest_action.yml/badge.svg)
![Unittest](https://github.com/DiyaKaswa11/First_Lab/actions/workflows/unittest_action.yml/badge.svg)

Based on Lab 1 (Github_Labs) of the MLOps course (IE7305). A simple Python calculator module tested automatically with **pytest** and **unittest** through **GitHub Actions** on every push and pull request.

## Project Structure

    .
    ├── .github/workflows/
    │   ├── pytest_action.yml      # Pytest CI (Python version matrix + coverage)
    │   └── unittest_action.yml    # Unittest CI
    ├── data/
    ├── src/
    │   └── calculator.py          # Calculator functions
    ├── test/
    │   ├── test_pytest.py         # Original pytest tests
    │   ├── test_unittest.py       # Original unittest tests
    │   └── test_new_functions.py  # Tests for the new functions
    ├── requirements.txt
    └── .gitignore

## My Modifications

### 1. New calculator functions (src/calculator.py)

| Function | Description |
|---|---|
| `power(x, y)` | Returns x raised to the power y |
| `factorial(n)` | Returns n! for a non-negative integer; raises `ValueError` for negative numbers or decimals |
| `sigmoid(x)` | Returns 1 / (1 + e^-x), the activation function used in logistic regression; output is always between 0 and 1 and it stays stable for very large or very small inputs |

All three raise `ValueError` for non-numeric inputs.

### 2. New test file (test/test_new_functions.py)

5 new pytest tests covering normal cases, edge cases (0! = 1, sigmoid(0) = 0.5, very large and very small sigmoid inputs), and invalid inputs. Total tests: **13** (8 original + 5 new).

### 3. Upgraded CI/CD pipeline (.github/workflows/)

- **Fixed workflow location:** moved workflows from `workflows/` to `.github/workflows/`, the only folder GitHub Actions reads.
- **Updated deprecated actions:** `actions/checkout@v2` → `v4`, `actions/setup-python@v2` → `v5`, `actions/upload-artifact@v2` → `v4` (v2 is retired and fails on GitHub).
- **Python version matrix:** pytest now runs on Python 3.10, 3.11 and 3.12 in parallel (Python 3.8 is end-of-life).
- **Code coverage:** added `pytest-cov` to report test coverage of `src/`.
- **Per-version test reports:** JUnit XML reports uploaded as artifacts for each Python version.
- **More triggers:** workflows run on push and pull requests to `main`, and can be triggered manually (`workflow_dispatch`).

## How to Run Locally

    python3 -m venv lab_01
    source lab_01/bin/activate
    pip install -r requirements.txt
    pytest

## Results

All workflows pass on GitHub Actions: 3 pytest jobs (one per Python version) and 1 unittest job. See the **Actions** tab for run details.
