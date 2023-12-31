from typing import Callable
from random import seed, randint

# Define global comparisson counter
global comparissons


def quick_sort(
    array: list, start: int, end: int,
    choose_pivot: Callable[[list, int, int], int],
    count_comparisons=False
) -> None:
    """
    This function sorts an array using quicksort algorithm
    and a variable method for choosing the pivot.

    Args:
        * array: array to be sorted
        * choose_pivot_func: method for choosing the pivot
        * count_comparisons: whether to count comparisons or not

    Return:
        * If count_comparisons is False, return sorted array
        * If count_comparisons is True, return a tuple of
        sorted array and number of comparisons

    DocTests:

        >>> array = [1, 2, 3]
        >>> quick_sort(
        ...     array, 0, len(array) - 1, pivot_random,
        ...     count_comparisons=False
        ... )
        >>> array == [1, 2, 3]
        True

        >>> array =[6, 1, 2, 7]
        >>> quick_sort(
        ...     array, 0, len(array) - 1, pivot_random,
        ...     count_comparisons=False
        ... )
        >>> array == [1, 2, 6, 7]
        True

        >>> array = [5, 4, 3, 2, 1]
        >>> quick_sort(
        ...     array, 0, len(array) - 1, pivot_random,
        ...     count_comparisons=False
        ... )
        >>> array == [1, 2, 3, 4, 5]
        True

        >>> array = []
        >>> quick_sort(
        ...     array, 0, len(array) - 1, pivot_random,
        ...     count_comparisons=False
        ... )
        >>> array == []
        True

        >>> array = [45]
        >>> quick_sort(
        ...     array, 0, len(array) - 1, pivot_random,
        ...     count_comparisons=False
        ... )
        >>> array == [45]
        True

        >>> array = [78, 8]
        >>> quick_sort(
        ...     array, 0, len(array) - 1, pivot_random,
        ...     count_comparisons=False
        ... )
        >>> array == [8, 78]
        True

        >>> array = [28, 8, 44, 17, 9, 31, 60, 101, 82, 2]
        >>> quick_sort(
        ...     array, 0, len(array) - 1, pivot_random,
        ...     count_comparisons=False
        ... )
        >>> array == [2, 8, 9, 17, 28, 31, 44, 60, 82, 101]
        True

    """
    # Base case
    if start >= end:
        return

    pivot = choose_pivot(array, start, end)
    # Moves the pivot to the beggining of the partition
    swap(array, start, pivot)

    # Partition the array and gets new pivot index
    pivot = partition(array, start, end, count_comparisons)

    quick_sort(array, start, pivot - 1, choose_pivot,
               count_comparisons=count_comparisons)
    quick_sort(array, pivot + 1, end, choose_pivot,
               count_comparisons=count_comparisons)


def partition(array: list, start: int, end: int,
              count_comparisons: bool) -> int:
    """
    This function partitions an array around the first element.

    Args:
        * array: array to be partitioned
        * start: starting index of the array
        * end: ending index of the array

    Return:
        * index of the pivot element
    """

    # The boundary is the first element bigger than pivot.
    pivot = start
    partition_boundary = pivot + 1

    for current in range(start + 1, end + 1):
        if array[current] < array[pivot]:  # else do nothing
            swap(array, partition_boundary, current)
            # Restores partition invariant arounf pivot
            partition_boundary += 1

    # Update the comparisson counter
    if count_comparisons:
        global comparissons
        # comparissons += end - start
        comparissons += end - start

    # Places the pivot in the right place with a swap.
    swap(array, pivot, partition_boundary - 1)
    # Updates its index
    pivot = partition_boundary - 1

    return pivot


def swap(array: list, element1: int, element2: int):
    """
    This function swaps two elements in an array.

    Arguments:
        * array: array
        * element1: index of the first element
        * element2: index of the second element
    """
    array[element1], array[element2] = array[element2], array[element1]


def pivot_first(array: list, start: int, end: int) -> int:
    """
    This function partitions an array around the first element.
    """
    return start


def pivot_last(array: list, start: int, end: int) -> int:
    """
    This function partitions an array around the last element.

    """
    return end


def pivot_median_of_three(array, start, end):
    """
    This function partitions an array around the median of
    the first, middle, and last element using our logic.
    """
    first, last = start, end
    mid = first + (last - first) // 2

    # Determine which of the three is the median
    if (array[first] < array[mid] < array[last]
            or array[last] < array[mid] < array[first]):
        return mid
    elif (array[mid] < array[first] < array[last]
          or array[last] < array[first] < array[mid]):
        return first
    return last


def pivot_random(array: list, start: int, end: int) -> int:
    """
    This function partitions an array around a random element.
    """
    return randint(start, end)


def array_from_file(filename):
    """
    Helper function to create an array of integers from a text file.

    Parameters:
    filename (str): the name of the file containing the array of integers

    Returns:
    nums (list): a list of integers
    """

    with open(filename) as file:
        nums = [int(line) for line in file]

    return nums


def main():
    """
    This function runs the main program.
    """
    global comparissons

    big_array = array_from_file(
        "./04_data/Numbers_for_QuickSort.txt")

    # # Prints comparisson with pivot first
    # comparissons = 0
    # quick_sort(big_array, 0, len(big_array) - 1,
    #            pivot_first, count_comparisons=True)
    # print(f"It made {comparissons} using a pivot first.")

    # # Prints comparisson with pivot last
    # comparissons = 0
    # quick_sort(big_array, 0, len(big_array) - 1,
    #            pivot_last, count_comparisons=True)
    # print(f"It made {comparissons} using a pivot last")

    # Prints comparisson with pivot median of first, middle and last
    comparissons = 0
    quick_sort(big_array, 0, len(big_array) - 1,
               pivot_median_of_three, count_comparisons=True)
    print(f"It made {comparissons} pivot median of first, middle and last.")

    # # Prints comparisson with pivot median of first, middle and last
    # arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    #         12, 13, 14, 15, 16, 17, 18, 19, 20]
    # arr2 = [2, 20, 1, 15, 3, 11, 13, 6, 16,
    #         10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
    # comparissons = 0
    # quick_sort(arr1, 0, len(arr1) - 1,
    #            pivot_median_of_three, count_comparisons=True)
    # print(f"It made {comparissons} pivot median of first, middle and last.")

    # # Prints comparisson with random pivot
    seed(90652978357490)
    # comparissons = 0
    # quick_sort(big_array, 0, len(big_array) - 1,
    #            pivot_random, count_comparisons=True)
    # print(f"It made {comparissons} using a random pivot.")


if __name__ == "__main__":
    main()
