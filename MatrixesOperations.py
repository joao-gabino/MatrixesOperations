import ArraysOperations as ao


def IsSquareMatrix(matrix):
    return bool(matrix) and all(len(row) == len(matrix) for row in matrix)


def LocateItemInMatrix(matrix, item):
    positions = []
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value == item:
                positions.append((row_index, col_index))
    return positions


def SumMatrix(matrix):
    return ao.SumArray([ao.SumArray(row) for row in matrix])


def AverageMatrix(matrix):
    return ao.AverageArray([value for row in matrix for value in row])


def SumLinesMatrix(matrix):
    return [ao.SumArray(row) for row in matrix]


def SumColumnsMatrix(matrix):
    return SumLinesMatrix(TransposeMatrix(matrix)) if matrix else []


def TransposeMatrix(matrix):
    if not matrix:
        return []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    return [[matrix[row][col] for row in range(num_rows)] for col in range(num_cols)]


def MultiplyMatrices(matrixA, matrixB):
    if not matrixA or not matrixB or len(matrixA[0]) != len(matrixB):
        raise ValueError("Incompatible matrices for multiplication.")

    num_rows_A = len(matrixA)
    num_cols_B = len(matrixB[0])
    num_cols_A = len(matrixA[0])

    result = [[0 for _ in range(num_cols_B)] for _ in range(num_rows_A)]

    for i in range(num_rows_A):
        for j in range(num_cols_B):
            result[i][j] = sum(matrixA[i][k] * matrixB[k][j] for k in range(num_cols_A))

    return result


def InvertMatrix(matrix):
    if not IsSquareMatrix(matrix):
        raise ValueError("Only square matrices can be inverted.")

    n = len(matrix)
    working = [list(map(float, row)) for row in matrix]
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    for i in range(n):
        factor = working[i][i]
        if factor == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")

        for j in range(n):
            working[i][j] /= factor
            identity[i][j] /= factor

        for k in range(n):
            if k != i:
                factor = working[k][i]
                for j in range(n):
                    working[k][j] -= factor * working[i][j]
                    identity[k][j] -= factor * identity[i][j]

    return identity


def DeterminantMatrix(matrix):
    if not IsSquareMatrix(matrix):
        raise ValueError("Only square matrices have a determinant.")

    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        submatrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * DeterminantMatrix(submatrix)

    return det


def IsSymmetricMatrix(matrix):
    if not IsSquareMatrix(matrix):
        return False

    n = len(matrix)
    return all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(i, n))


def IsIdentityMatrix(matrix):
    if not IsSquareMatrix(matrix):
        return False

    n = len(matrix)
    return all(
        (matrix[i][j] == 1 if i == j else matrix[i][j] == 0)
        for i in range(n)
        for j in range(n)
    )


def IsDiagonalMatrix(matrix):
    if not IsSquareMatrix(matrix):
        return False

    n = len(matrix)
    return all(matrix[i][j] == 0 for i in range(n) for j in range(n) if i != j)


def IsZeroMatrix(matrix):
    return all(value == 0 for row in matrix for value in row)


def IsOrthogonalMatrix(matrix):
    if not IsSquareMatrix(matrix):
        return False

    n = len(matrix)
    return all(
        ao.SumArray([matrix[i][k] * matrix[j][k] for k in range(n)]) == (1 if i == j else 0)
        for i in range(n)
        for j in range(n)
    )


def IsPositiveDefiniteMatrix(matrix):
    if not IsSymmetricMatrix(matrix):
        return False

    return all(matrix[i][i] > 0 for i in range(len(matrix)))


def IsNegativeDefiniteMatrix(matrix):
    if not IsSymmetricMatrix(matrix):
        return False

    return all(matrix[i][i] < 0 for i in range(len(matrix)))


def IsSingularMatrix(matrix):
    if not IsSquareMatrix(matrix):
        return False

    return DeterminantMatrix(matrix) == 0


def IsInvertibleMatrix(matrix):
    if not IsSquareMatrix(matrix):
        return False

    return not IsSingularMatrix(matrix)


def IsDiagonalizableMatrix(matrix):
    return IsSymmetricMatrix(matrix)


def IsOrthogonalizableMatrix(matrix):
    return IsSymmetricMatrix(matrix)


def IsSymmetricPositiveDefiniteMatrix(matrix):
    return IsPositiveDefiniteMatrix(matrix)


def IsSymmetricNegativeDefiniteMatrix(matrix):
    return IsNegativeDefiniteMatrix(matrix)


def IsSymmetricIndefiniteMatrix(matrix):
    if not IsSymmetricMatrix(matrix):
        return False

    n = len(matrix)
    has_positive = any(matrix[i][i] > 0 for i in range(n))
    has_negative = any(matrix[i][i] < 0 for i in range(n))

    return has_positive and has_negative


def IsSymmetricSingularMatrix(matrix):
    return IsSymmetricMatrix(matrix) and IsSingularMatrix(matrix)


def IsSymmetricInvertibleMatrix(matrix):
    return IsSymmetricMatrix(matrix) and IsInvertibleMatrix(matrix)


def IsSymmetricDiagonalizableMatrix(matrix):
    return IsSymmetricMatrix(matrix) and IsDiagonalizableMatrix(matrix)


def IsSymmetricOrthogonalizableMatrix(matrix):
    return IsSymmetricMatrix(matrix) and IsOrthogonalizableMatrix(matrix)

