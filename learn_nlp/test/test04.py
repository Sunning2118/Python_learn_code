search = "ron"
wordList = ['bron', 'brrrron', 'brrrrorn', 'brrrrrrrno', 'bbbbbbnrnoon']


def searchRon(search, wordList):
    wordList_result = []
    for word in wordList:  # 提取出主串
        i = 0  # 主串标志
        search_letter_num = 0  # 子串标志
        len_search = len(search)  # 子串长度
        len_word = len(word)  # 主串长度
        while search_letter_num < len_search:  # 子串字母挨个比较
            while i < len_word:  # 扫主串
                if search[search_letter_num] == word[i]:  # 找到匹配的了
                    if search_letter_num == len_search - 1:  # 如果子串走到头了，则append
                        wordList_result.append(word)
                    search_letter_num += 1  # 找到了，子串、主串都前进
                    i += 1
                    break
                i += 1  # 未找到，子串不动，主串前进
            if i == len(word):
                break
    return wordList_result


print(searchRon(search, wordList))
