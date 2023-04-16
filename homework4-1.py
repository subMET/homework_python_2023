import copy


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = ' ')
        print()
    

def matrix_transpose(matrix):
    transpose = copy.deepcopy(matrix)
    for i in range(len(transpose)):
        for j in range(len(transpose[i])):
            transpose[j][i] = matrix[i][j]
    return transpose


matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
print_matrix(matrix_1)
matrix_2 = matrix_transpose(matrix_1)
print_matrix(matrix_2)