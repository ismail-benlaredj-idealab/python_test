# def remove_zeros(matrix):
#     new_matrix = []
#     for row in matrix:
#         # Filter out the zeros in the current row
#         filtered_row = [cell for cell in row if cell != 0]
#         # Only add the row to the new matrix if it has non-zero elements
#         if filtered_row:
#             new_matrix.append(filtered_row)
#     return new_matrix

# # Example usage
# original_matrix = [
#     [1, 0, 3, 4],
#     [0, 0, 0, 0],
#     [2, 3, 0, 5],
#     [0, 0, 0, 6]
# ]

# new_matrix = remove_zeros(original_matrix)
# print(new_matrix)


def print_indexes(matrix):
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            print(f"Element at index ({i}, {j})")

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_indexes(matrix)
