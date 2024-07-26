# Leetcode problems

My solutions for several leetcode problems

## Problems solved so far

- [fibonacci-number](https://leetcode.com/problems/fibonacci-number/)
- [reverse-string](https://leetcode.com/problems/reverse-string/)
- [suffle-the-array](https://leetcode.com/problems/shuffle-the-array/)
- [valid-sudoku-board](https://leetcode.com/problems/valid-sudoku/)
- [binary-search](https://leetcode.com/problems/binary-search/)
- [maximum-count-of-positive-integer-and-negative-integer](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/submissions/)

## Activating the `virtual env`

This project is developed on a very simple manner, using `poetry` basics, for now. So to activate the virtual env, please run the following

- Activate
```zsh
poetry shell 
```

- Deactivate
```zsh
deactivate
```

## Running the unit tests

1. On the root of the python implementation folder (👀 _tech debt_ 👀), run

```python
poetry run python -m unittest tests/**/test*.py
```

or, you can alternatively:

2. Also on the root folder, use the following

```python
poetry run python -m tests.module_a.test_module_b
```