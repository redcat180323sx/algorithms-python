# algorithms-python

A personal collection of classic algorithms and data structures implemented in clean, readable Python.

## Features

- Sorting and searching algorithms
- Graph traversal and shortest-path algorithms
- Common data structures
- Dynamic programming examples
- Type hints and concise documentation
- Tests for correctness and edge cases

## Install

```bash
git clone https://github.com/your-username/algorithms-python.git
cd algorithms-python
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Import an implementation directly:

```python
from algorithms.sorting import quicksort

numbers = [8, 3, 1, 7, 4]
print(quicksort(numbers))
```

Run the test suite:

```bash
python -m pytest
```