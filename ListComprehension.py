nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]
]

even_squares = [x**2 for sublist in nums for x in sublist if x%2 == 0]
print(even_squares)