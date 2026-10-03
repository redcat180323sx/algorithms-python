"""Shared helper functions for algorithm implementations."""

from typing import Callable, Iterable, Iterator, MutableSequence, Optional, Tuple, TypeVar

T = TypeVar("T")
K = TypeVar("K")


def swap(items: MutableSequence[T], first: int, second: int) -> None:
    """Swap two elements of a mutable sequence in place.

    Args:
        items: Sequence containing the elements to exchange.
        first: Index of the first element.
        second: Index of the second element.

    Raises:
        IndexError: If either index is outside the sequence.
    """
    items[first], items[second] = items[second], items[first]


def is_sorted(
    items: Iterable[T],
    *,
    key: Optional[Callable[[T], K]] = None,
    reverse: bool = False,
) -> bool:
    """Return whether items are ordered monotonically.

    Args:
        items: Values to inspect.
        key: Optional function used to extract each comparison key.
        reverse: Check descending order when true; ascending order otherwise.

    Returns:
        True when the iterable is sorted or contains fewer than two items.
    """
    iterator = iter(items)

    try:
        previous_item = next(iterator)
    except StopIteration:
        return True

    previous = key(previous_item) if key is not None else previous_item

    for item in iterator:
        current = key(item) if key is not None else item
        if (previous < current) if reverse else (previous > current):
            return False
        previous = current

    return True


def chunked(items: Iterable[T], size: int) -> Iterator[Tuple[T, ...]]:
    """Yield consecutive fixed-size chunks from an iterable.

    The final chunk may contain fewer than ``size`` elements.

    Args:
        items: Values to divide into chunks.
        size: Maximum number of elements in each chunk.

    Yields:
        Tuples containing up to ``size`` consecutive elements.

    Raises:
        ValueError: If ``size`` is not positive.
    """
    if size <= 0:
        raise ValueError("size must be greater than zero")

    chunk = []
    for item in items:
        chunk.append(item)
        if len(chunk) == size:
            yield tuple(chunk)
            chunk.clear()

    if chunk:
        yield tuple(chunk)


def clamp(value: T, lower: T, upper: T) -> T:
    """Constrain a comparable value to an inclusive range.

    Args:
        value: Value to constrain.
        lower: Inclusive lower bound.
        upper: Inclusive upper bound.

    Returns:
        ``lower`` when value is too small, ``upper`` when it is too large,
        or the original value when it is within the range.

    Raises:
        ValueError: If the lower bound is greater than the upper bound.
    """
    if lower > upper:
        raise ValueError("lower bound must not exceed upper bound")
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value