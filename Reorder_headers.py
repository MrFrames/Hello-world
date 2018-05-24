import difflib
from openpyxl import *


def get_ratio(str1,str2):
    result = difflib.SequenceMatcher(lambda x: x==" ", str1, str2)
    return result.ratio()

def get_inputEmpty(dict, overflow):
    print("Please enter the {} new fields: ".format(overflow))
    n = 1
    overflow_count = overflow
    while True:
        input_column = str(input("column {}:".format(n)))
        if input_column in dict.keys():
            dict[input_column] = (1, 0, None)
            n += 1
            overflow_count = overflow_count -1
            if overflow_count == 0:
                break
            print (overflow_count)
        else:
            print("Column not recognised, be sure to type in lowercase only")
    return dict

def get_highestRatio(list1, str2):
    highest_ratio = 0
    highest_str = ""
    for str1 in list1:
        test_ratio = get_ratio(str1,str2)
        if test_ratio > highest_ratio:
            highest_ratio = test_ratio
            highest_str = str1
    return (highest_ratio, list1.index(highest_str), highest_str)

def find_leastDiffIndex(list1, list2):
    overflow = len(list2) - len(list1)
    list1 = list(i.lower() for i in list1)
    list2 = list(i.lower() for i in list2)
    new_dict = {}
    for i2 in range(0, len(list2)):
        str2 = list2[i2]
        if list2[i2] in list1:
            same_strIndex = list1.index(list2[i2])
            new_dict [str2] = (1,same_strIndex,list2[i2])
        else:
            new_dict[str2] = get_highestRatio(list1,list2[i2])

    print (new_dict)

    added_emptyHeadings = get_inputEmpty(new_dict,overflow)
    for string in list2:
        print (string + ": " + str(added_emptyHeadings.get(string)))
    return (new_dict)

def get_reorderedList(shuffleDict, toList, type):
    reorderedList = []
    for string in toList:
        direction = shuffleDict.get(string.lower())
        print (direction)
        if type == "name":
            reorderedList.append(direction[2])
        elif type == "index" and direction[2] == None:
            reorderedList.append(None)
        else:
            reorderedList.append(direction[1])
    return reorderedList


