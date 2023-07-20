# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц

from matrix import Matrix

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
matrix_3 = Matrix([[12, 11, 10], [9, 8, 7], [6, 5, 4], [3, 2, 1]])
matrix_4 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print()
print(repr(matrix_1))

print()
print(matrix_2)
print(matrix_3)
print(matrix_4)

print(f'{matrix_1 == matrix_2=}')
print(f'{matrix_1 == matrix_2=}')
print(f'{matrix_2 == matrix_3=}')
print(f'{matrix_2 != matrix_3=}')
print(f'{matrix_3 != matrix_4=}')

print()
print(matrix_1 + matrix_2)
print(matrix_2 + matrix_3)

print(matrix_1 * matrix_2)
print(matrix_3 + matrix_4)

print()
print(matrix_1 * matrix_4)
print(matrix_4 * 5)