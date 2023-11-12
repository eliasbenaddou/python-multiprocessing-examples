import multiprocessing
import time


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


def process_number(num: int, result_queue: multiprocessing.Queue) -> None:
    """Process a number, calculate sum of squares and check for perfection.

    Args:
        num (int): The number to process.
        result_queue (multiprocessing.Queue): The queue to store the result.
    """
    sum_result = sum_of_squares(num)
    perfect_result = is_perfect(num)
    result_queue.put((num, sum_result, perfect_result))


if __name__ == "__main__":
    start_range = 1
    end_range = 10000

    start_time = time.time()

    result_queue = multiprocessing.Queue()

    processes = []
    for num in range(start_range, end_range):
        process = multiprocessing.Process(
            target=process_number, args=(num, result_queue)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = []
    for _ in range(end_range - start_range):
        results.append(result_queue.get())

    end_time = time.time()

    for num, sum_result, perfect_result in results:
        print(f"Number: {num}, Sum of Squares: {sum_result}, Perfect: {perfect_result}")

    print(f"Done in {end_time - start_time:.4f} seconds")
