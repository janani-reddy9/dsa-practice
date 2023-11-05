# https://leetcode.com/problems/last-visited-integers/

def lastVisitedIntegers(words):
    """
    :type words: List[str]
    :rtype: List[int]
    """
    output = []
    numbers = []
    consec_prev = -1
    for word in words:
        if word == "prev":
            if len(numbers) + consec_prev >= 0:
                output.append(int(numbers[consec_prev]))
            else:
                output.append(-1)
            consec_prev -= 1
        else:
            consec_prev = -1
            numbers.append(word)
    return output


print(lastVisitedIntegers(["1", "2", "prev", "prev", "prev", 4, "prev", "prev", "prev", "prev", "prev"]))
