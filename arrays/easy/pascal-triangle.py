
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    output = [[0 for i in range(j)] for j in range(1, numRows+1)]
    for i in range(0, numRows):
        output[i][0] = 1
        col = 1
        while col <= i:
            if col == i:
                output[i][col] = 1
                break
            output[i][col] = output[i-1][col]+output[i-1][col-1]
            col += 1
    print(output)


print(generate(5))
