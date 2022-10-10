import logging

logging.basicConfig(filename="binary_search.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def insertion_sort(num):
    """
     function to sort the list
     :param num: using parameter 'num' to define list
     :return: it will sort the list
    """
    try:
        for i in range(1, len(num)):
            temp = num[i]
            j = i
            while num[j - 1] > num[j] and j > 0:
                num[j] = num[j - 1]
                j = j - 1
                num[j] = temp
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    num = [2, 6, 5, 1, 3, 4]
    print("Before sorting", num)
    insertion_sort(num)
    print("After sorting", num)
