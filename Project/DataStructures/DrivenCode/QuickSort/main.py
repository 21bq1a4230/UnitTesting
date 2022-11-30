def partition(array, low, high):
    """ your code
    for partition"""


def QuickSort(array, low, high):
    """your code for quick sort"""


def startQuickSort(array):
    low = 0
    high = len(array) - 1
    QuickSort(array, low, high)
    return array


if __name__ == "__main__":
    l = [67, 16, 21, 70, 88, 92, 46, 64, 73, 75, 65, 90, 9, 80, 36, 6, 97, 39, 4, 72, 43, 69, 49, 47, 23, 95, 41, 14,
         31, 13]

    print(startQuickSort(l))
