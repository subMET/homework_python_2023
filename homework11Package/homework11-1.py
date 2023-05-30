from math import sqrt 

class Matrix():

    def __init__(self, table):
        self.matrix = table

    def __str__(self):
        result = '\n'
        for i in range(len(self.matrix)):
            result += '|'
            for j in range(len(self.matrix[i])):
                result += f' {str(self.matrix[i][j])}'   
            result += ' |\n'
        return result
    
    def norm(self):
        norm_pow = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                norm_pow += self.matrix[i][j]**2
        return sqrt(norm_pow)
    
    def __eq__(self, other) -> bool:
        return self.norm() == other.norm()
    
    def __ne__(self, other) -> bool:
        return self.norm() != other.norm()
    
    def __gt__(self, other) -> bool:
        return self.norm() > other.norm()
    
    def __ge__(self, other) -> bool:
        return self.norm() <= other.norm()
    
    def __lt__(self, other) -> bool:
        return self.norm() < other.norm()
    
    def __le__(self, other) -> bool:
        return self.norm() >= other.norm()
    
    def __add__(self, other):
        buffer = self.matrix
        if range(len(self.matrix)) == range(len(other.matrix)) and \
        range(len(self.matrix[0])) == range(len(other.matrix[0])):  
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    buffer[i][j] += other.matrix[i][j]
        else:
            raise ValueError('Матрицы имеют разные размеры. Их невозможно складывать.')
        return Matrix(buffer)
        
    def __mul__(self,other):
        buffer_matrix = []
        buffer = 0
        if range(len(self.matrix[0])) == range(len(other.matrix)):
            for i in range(len(self.matrix)):
                buffer_matrix.append([])
                for j in range(len(other.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        buffer += self.matrix[i][k] * other.matrix[k][j]
                    buffer_matrix[i].append(buffer)
                    buffer = 0
        else:
            raise ValueError("""Для умножения матриц необходимо чтобы количество столбцов первой 
                             совпадало с количеством строк второй""")
        return Matrix(buffer_matrix)
    
    def transpose(self):
        buffer = []
        for i in range(len(self.matrix[0])):
            buffer.append([])
            for j in range(len(self.matrix)):
                buffer[i].append(self.matrix[j][i])
        return Matrix(buffer)

m = Matrix([[1,2,3],[4,5,6],[9,0,8]])
g = Matrix([[1,2,3],[4,5,6],[1,0,8],[0,0,0]])
print(m)
print(g < m)
z = m + m
print(z)
# j = g + m         # Ошибка

A = Matrix([[1,2,3],[4,5,6]])
B = Matrix([[7,8],[9,1],[2,3]])
C = A * B
print(C)
Atr = A.transpose()
print(Atr)