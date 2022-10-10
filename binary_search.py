import logging

logging.basicConfig(filename="binary_search.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def binary_search(list1, key):
    """
    function for binary_search to find the target value or key value or user input value is in sorted list
    :param list1: defining list using parameter 'list1'
    :param key: taking value from user to find that value from list
    :return: return target value or key value
    """
    low = 0
    high = len(list1) - 1
    Found = False
    try:
        while low <= high and not Found:
            mid = (low + high) // 2
            if key == list1[mid]:
                Found = True
            elif key > list1[mid]:
                low = mid + 1
            else:
                high = mid - 1
        if Found == True:
            print(("key is Found"))
        else:
            print("key is not Found")
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    list1 = [23, 1, 4, 2, 3, 15, 12, 17, 11]
    print("Before sorting", list1)
    list1.sort()
    print("After sorting",list1)
    try:
        key = int(input("Enter the key"))
        binary_search(list1, key)
    except ValueError:
        logging.error("Enter numeric value only")
