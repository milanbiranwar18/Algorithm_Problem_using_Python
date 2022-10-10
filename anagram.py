import logging

logging.basicConfig(filename="anagram.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def anagram(str1, str2):
    '''
    fuction for anagram it will check that two words that it is anagram or not
    :param: using parameter str1 and str2 to take user input to check they both are anagram or not
    :return: return given two input are anagram or not
    '''
    try:
        count = 0
        if len(str1) == len(str2):
            for i in str1:
                for j in str2:
                    if i == j:
                        count += 1
                        str1.replace(i,'',1)
                        str2.replace(j,'',1)
                        break
        if count == len(str1):
            print("Given words are anagram")
        else:
            print("Given words are not anagram")
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    try:
        str1 = input("Enter first word to check it is anagram or not")
        str2 = input("Enter another word to compare and check that it is anagram or not")
        anagram(str1, str2)
    except ValueError:
        logging.error("Enter word only")
