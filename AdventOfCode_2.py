def read():
    with open('Day2.txt') as text:
        matrix = [[int(x) for x in ln.split()] for ln in text]

    text.close
    return matrix

def calculate():
    matrix = read()
    su = 0

    for x in xrange(len(matrix)):
        mini = min(matrix[x])
        maxi = max(matrix[x])
        difference = maxi - mini
        su+=difference
    print su

def calculate_2():
    matrix = read()
    su = 0
    for x in xrange(len(matrix)):
        for y in xrange (len(matrix)):
            for k in xrange(len(matrix)):
                if (k != y):
                    if (matrix[x][y]%(matrix[x][k])==0):
                        su+=(matrix[x][y]/(matrix[x][k]))
    print len(matrix)/len(matrix[0])
    print su

calculate()
calculate_2()