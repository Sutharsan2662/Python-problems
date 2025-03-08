#rotation of a matrix

#by 90 degree
 #int(input("enter the size of the matrix = "))
def rot_mat(input):
    n = len(input)
    mat = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):

            mat[i][j] = input[n-j-1][i]
    return mat

matrix = [[1,2,3], [4,5,6], [7,8,9]]

print(rot_mat(matrix))
# print(matrix)

#by 180 degree
def rot_mat_180(input):
    n = len(input)
    mat = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):

            mat[i][j] = input[i][n-j-1]
    return mat

print(rot_mat_180(matrix))

#by 270 degree
def rot_mat_270(input):
    n = len(input)
    mat = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):

            mat[i][j] = input[n-i-1][n-j-1]
    return mat

print((rot_mat_270(matrix)))

#first row to the third coloumn
def rot_mat_row(input):
    n = len(input)
    mat = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):

            mat[i][j] = input[n-i-1][j]
    return mat

print(rot_mat_row(matrix))

def rotation(input):
    n = len(input)
    mat = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):

            mat[i][j] = input[n,-1][j]
    return mat

print(rotation(matrix))