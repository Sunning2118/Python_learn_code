# 情况1：在一个数组里， 寻找包含‘ron’的string, 字母【r】【o】【n】可以不连续，可以不按照相对顺序存在， 比如：
# 有效string：'brown' -> valid: b[r][o]w[n] ：
# 有效string: 'cornflowerblue' -> valid: c[o][r][n]flowerblue

colorBase1 = ['cornfloweblue', 'saddlebown']


def findColorPerWord(color, search):
    searchList = []

    for letter in search:
        if letter not in searchList:
            searchList.append(letter)

    for sl in searchList:
        if sl not in color:
            return False

    return True


def findColor(search):
    ret = []

    for color in colorBase1:  #
        if findColorPerWord(color, search):
            ret.append(color)

    return ret


if __name__ == '__main__':
    print(findColor(colorBase1))

#
# # 情况2: search = 'roon'
# def findColorPerWord(color, search):
#     colorMap = {}
#
#     for c in color:
#         if c in colorMap:
#             colorMap[c] += 1
#         else:
#             colorMap[c] = 1
#
#     for letter in search:
#         if letter in colorMap:
#             colorMap[letter] -= 1
#             if colorMap[letter] < 0:
#                 return False
#         else:
#             return False
#
#     return True
#
#
# colorBase1 = ['cornflweblue', 'saddlebroown']
#
#
# def findColor(search):
#     ret = []
#     for color in colorBase1:
#         if findColorPerWord(color, search):
#             ret.append(color)
#
#     return ret
#
#
# # 情况3: search = 'ron'，其他要求同上，不同要求为： 要求相对顺序一样，比如：
# # 有效string = 'brown' -> valid: b[r][o]w[n] // valid
# # 无效string = 'cornflowerblue' -> valid: c[o][r][n]flowerblue // not valid
#
# # 'ron'
# colorBase2 = ['cornflweblue', 'saddlebroown']
#
#
# # no repeating value
# def findColorPerWord(color, search):
#     searchList = []
#
#     for letter in search:
#         if letter not in searchList:
#             searchList.append(letter)
#
#     for element in searchList:
#         if element not in color:
#             return False
#
#     return True
#
#
# def findColor(search):
#     ret = colorBase2.copy()
#     searchList = []
#
#     for letter in search:
#         if letter not in searchList:
#             searchList.append(letter)
#
#     for color in colorBase2:
#         indexList = []
#         if findColorPerWord(color, search):
#             print(f"{color} has all the letters")
#             for element in searchList:
#                 indexList.append(color.index(element))
#
#             print(f"indexList for {color} is: {indexList}")
#
#             for index in range(len(indexList) - 1):
#                 if indexList[index + 1] < indexList[index]:
#                     print(f"{color} is not in required sequence")
#                     ret.remove(color)
#                     break
#         else:
#             ret.remove(color)
#
#     return ret
