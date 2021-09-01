vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

# [8, 6, -18, 16, 12, -36, 24, 18, -54]
result = [x * y for x in vec1 for y in vec2]
print('--result0--', result)

# [6, 5, -7, 8, 7, -5, 10, 9, -3]
result = [x + y for x in vec1 for y in vec2]
print('--result1--', result)

# [8, 12, -54]
result = [vec1[i] * vec2[i] for i in range(len(vec1))]
print('--result2--', result)

# ['3.1', '3.14', '3.142', '3.1416', '3.14159']
result = [str(round(355 / 113, i)) for i in range(1, 6)]
print('--result3--', result)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
 ]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
result = [[row[i] for row in matrix] for i in range(4)]
print('--result4--', result)
