colorBase = ["greenyellow", "lightgoldenyellow", "lightyellow", "yellow", "yellowgreen"]


def findColor(search):
    flag = 0
    i = 0
    while i < len(colorBase):
        if flag:
            i -= 1
            flag = 0
        if colorBase[i] != search:
            print(f"element：{colorBase[i]}")
            colorBase.pop(i)
            flag = 1
            print(f"current list:{colorBase}")
        i += 1
    return colorBase


print(findColor('yellow'))

# def findColor(search):
#     for color in colorBase:
#         if color != search:
#             print(f"element：{color}")
#             colorBase.remove(color)
#             print(f"current list:{colorBase}")
#     return colorBase
