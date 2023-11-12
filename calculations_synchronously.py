import time
from typing import List, Tuple


def sum_of_squares(n: int) -> int:
    """Calculate the sum of squares for a given number.

    Args:
        n (int): The input number.

    Returns:
        int: The sum of squares.
    """
    return sum(i**2 for i in range(1, n + 1))


def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number.

    Args:
        n (int): The input number.

    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    sum_factors = sum(i for i in range(1, n) if n % i == 0)
    return sum_factors == n


def process_number(num: int) -> Tuple[int, int, bool]:
    """Process a number, calculate sum of squares and check for perfection.

    Args:
        num (int): The number to process.

    Returns:
        Tuple[int, int, bool]: The processed result containing the number, sum of squares, and perfection status.
    """
    sum_result = sum_of_squares(num)
    perfect_result = is_perfect(num)
    return num, sum_result, perfect_result


def process_range(start: int, end: int) -> List[Tuple[int, int, bool]]:
    """Process a range of numbers and return the results.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        List[Tuple[int, int, bool]]: List of processed results.
    """
    results = [process_number(num) for num in range(start, end)]
    return results


if __name__ == "__main__":
    start_range = 1
    end_range = 10000

    start_time = time.time()

    results = process_range(start_range, end_range)

    end_time = time.time()

    for num, sum_result, perfect_result in results:
        print(f"Number: {num}, Sum of Squares: {sum_result}, Perfect: {perfect_result}")

    print(f"Done in {end_time - start_time:.4f} seconds")
