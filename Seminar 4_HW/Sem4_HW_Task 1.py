"""
1. Напишите функцию для транспонирования матрицы.
"""

def transposition_matrix(matrix: dict) -> int:
    """Функция транспонирования матрицы."""
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


if __name__ == '__main__':
    matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(transposition_matrix(matrix))
