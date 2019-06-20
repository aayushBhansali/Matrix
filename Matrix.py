import random

class Matrix:

    # Constructor
    def __init__(self, rows, columns):
        self.matrix = []
        self.rows = rows
        self.columns = columns

        for i in range(rows):
            self.matrix.append([])

    # User Input
    def accept(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i].append(int(input()))

    # Randomize
    def randomize(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i].append(random.choice([-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]))

    # Display the matrix
    def display(self):
        for i in range(self.rows):
            print(self.matrix[i], end="\n")


    @staticmethod
    def subtract_stat(first, second):
        temp = Matrix(first.rows, first.columns)
        try:
            if not first.rows == second.rows:
                raise ValueError
            elif not first.columns == second.columns:
                raise ValueError
            else:
                for i in range(first.rows):
                    for j in range(first.columns):
                        temp.matrix[i].append(first.matrix[i][j] - second.matrix[i][j])
                return temp

        except ValueError as error:
            print("Matrix Dimensions Not Same")


    # Subtract a given matrix from original matrix
    def subtract(self, second):
        try:
            if not second.rows == self.rows:
                raise ValueError
            elif not second.columns == self.columns:
                raise ValueError
            else:
                for i in range(self.rows):
                    for j in range(self.columns):
                        self.matrix[i].append(self.matrix[i].pop(0) - second.matrix[i][j])


        except ValueError as error:
            print("Matrix Dimensions Not Same ")

    # Add second matrix to original matrix
    def add(self, second):
        try:
            if not second.rows == self.rows:
                raise ValueError
            elif not second.columns == self.columns:
                raise ValueError
            else:
                for i in range(self.rows):
                    for j in range(self.columns):
                        self.matrix[i].append(self.matrix[i].pop(0) + second.matrix[i][j])

        except ValueError as error:
            print("Matrix Dimensions Not Same ")


    def element_wise_multiply(self, mat):
        temp = Matrix(mat.rows, mat.columns)
        for i in range(mat.rows):
            for j in range(mat.columns):
                temp.matrix[i].append(self.matrix[i][j] * mat.matrix[i][j])
        return temp


    def multiply(self, second):
        sum = 0
        try:
            if not self.columns == second.rows:
                print(str(self.columns) + " " + str(second.rows))
                raise ValueError
            else:
                temp = Matrix(self.rows, second.columns)

                for i in range(self.rows):
                    for j in range(second.columns):
                        for k in range(second.rows):
                            sum += self.matrix[i][k] * second.matrix[k][j]
                        temp.matrix[i].append(sum)
                        sum = 0
                return temp

        except ValueError:
            print("Cannot Multiply Matrix")

    def scalar(self, x):
        temp = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                temp.matrix[i].append(self.matrix[i][j] * x)
        return temp


    @staticmethod
    def map(matrix, method):
        temp = Matrix(matrix.rows, matrix.columns)
        for i in range(matrix.rows):
            for j in range(matrix.columns):
                temp.matrix[i].append(method(matrix.matrix[i][j]))
        return temp

    def apply_to_all(self, method):
        temp = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                temp.matrix[i].append(method(self.matrix[i][j]))
        return temp

    def transpose(self):
        mat = Matrix(self.columns, self.rows)
        for i in range(self.columns):
            for j in range(self.rows):
                mat.matrix[i].append(self.matrix[j][i])
        return mat

    @staticmethod
    def fromArray(input):
        ip = Matrix(len(input), 1)
        for i in range(len(input)):
            ip.matrix[i].append(input[i])
        return ip