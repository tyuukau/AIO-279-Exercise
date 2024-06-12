from typing import Generator


def max_in_sliding_window(num_list: list[int], k: int) -> Generator[int | None, None, None]:
    """
    Generates the maximum value in a sliding window of size k over a given list of numbers.

    Args:
        num_list (list[int]): The list of numbers.
        k (int): The size of the sliding window.

    Yields:
        int | None: The maximum value in the current sliding window. If the maximum value is smaller than 1, None is yielded.

    Example:
        >>> num_list = [1, -1, -1, -3, 5, 3, 6, 7]
        >>> k = 3
        >>> window_generator = max_in_sliding_window(num_list, k)
        >>> next(window_generator)
        1
        >>> next(window_generator)
        None
        >>> next(window_generator)
        5
        >>> next(window_generator)
        5
        >>> next(window_generator)
        6
        >>> next(window_generator)
        7
    """
    if k < 1:
        raise ValueError("The window must be larger than 0.")
    if k > len(num_list):
        raise ValueError("The window must be smaller than the list.")

    for i in range(0, len(num_list) - k + 1):
        max_value = max([i for i in num_list[i : i + k]])
        yield max_value if max_value >= 1 else None
