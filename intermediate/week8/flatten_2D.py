# Author: Melissa Perez
# Date: --/--/--
# Description:


def flatten_matrix(mat):
    # only works where n = m
    if not mat:
        return mat
    rows = len(mat)
    cols = len(mat[0])
    new_list_length = rows * cols
    flattened = [None] * new_list_length

    for i in range(rows):
        for j in range(cols):
            # row index * number of col + col index
            flattened[i * cols + j] = mat[i][j]

    return flattened


if __name__ == "__main__":
    some_mat = [
        [2, 1],
        [1, 1]
    ]
    print(some_mat)
    print(flatten_matrix(some_mat))