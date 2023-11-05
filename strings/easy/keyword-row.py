def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    rows = [['q','w','e','r','t','y','u','i','o','p'], ['a','s','d','f','g','h','j','k','l'], ['z','x','c','v','b','n','m']]
    output = []
    for word in words:
        lowercase_word = word.lower()
        row_value = 0
        for row in rows:
            if lowercase_word[0] in row:
                break
            row_value += 1
        for i in range(0, len(word)):
            if lowercase_word[i] not in rows[row_value]:
                break
        else:
            output.append(word)

findWords(["Hello","Alaska","Dad","Peace"])

