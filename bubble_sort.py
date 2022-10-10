import logging

logging.basicConfig(filename="bubble_sort.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def bubble_sort(data):
    """
    function for bubble_sort to sort the list
    :param data: using parameter 'num' to define list
    :return: it will sort the list
    """
    num=data
    try:
        for i in range(len(num) - 1, 0, -1):
            for j in range(i):
                if num[j] > num[j + 1]:
                    temp = num[j]
                    num[j] = num[j + 1]
                    num[j + 1] = temp
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    numlist = [5, 3, 8, 6, 7, 2]
    print("Before sorting",numlist)
    bubble_sort(numlist)
    print("After sorting", numlist)
