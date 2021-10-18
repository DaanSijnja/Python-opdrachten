def inverse(matin,rowCols):
    matout = []
    for i in range(rowCols):
        matout.append([])
        for j in range(rowCols):
            matout[i].append(0.0)


    for i in range(rowCols):
        for j in range(rowCols):
            matout[i][j] = (- matin[i][j])
    
    for i in range(rowCols):
        
        if(matout[i][i] == 0.0):
            print('error')
            break
        else:
            matout[i][i] = (-1/matout[i][i])

        for j in range(rowCols):
            if(j != i):
                matout[j][i] = matout[j][i] * matout[i][i]

        for j in range(rowCols):
            if(j != i):
                for k in range(rowCols):
                    if(k != i):
                        matout[j][k] = matout[j][k] + matout[j][i] * matout[i][k]

        for j in range(rowCols):
            if(j != i):
                matout[i][j] = matout[i][j] * matout[i][i]
    return matout

def multiply(matL,matR,rowsL,colsR,cLrR):
    matout = []
    for i in range(cLrR):
        matout.append([])
        for j in range(cLrR):
            matout[i].append(0.0)

    for i in range(rowsL):
        for j in range(colsR):
            temp = 0.0
            for k in range(cLrR):
                temp += matL[i][k] * matR[k][j]
            matout[i][j] = temp
    return matout

def transpose(matin,ColsOut,RowsOut):
    matout = []
    for i in range(RowsOut):
        matout.append([])
        for j in range(ColsOut):
            matout[i].append(0.0)


    for i in range(ColsOut):
        for j in range(RowsOut):
            matout[j][i] = matin[i][j]

    return matout

def print_matrix(matin):
    for r in matin:
        print(str(r))

Z = [[268,0,0,0,0,0,0,0,0],
     [267,0,0,0,0,0,0,0,0],
     [269,0,0,0,0,0,0,0,0],
     [268,0,0,0,0,0,0,0,0],
     [268,0,0,0,0,0,0,0,0],
     [264,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]
     ]

A = [[65,112.6,1,0,0,0,0,0,0],
     [130,0,1,0,0,0,0,0,0],
     [65,-112.6,1,0,0,0,0,0,0],
     [-65,-112.6,1,0,0,0,0,0,0],
     [-130,0,1,0,0,0,0,0,0],
     [-65,112.6,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]
     ]

AT = transpose(A,6,6)
print('AT')
print_matrix(AT)
ATA = multiply(AT,A,6,6,6)
print('ATA')
print_matrix(ATA)
ATA_INVERS = inverse(ATA,6)
print('ATA_invers')
print_matrix(ATA_INVERS)
ATA_AT = multiply(ATA_INVERS,AT,6,6,6)
print('ATA_AT')
print_matrix(ATA_AT)

F = multiply(ATA_AT,Z,6,6,6)
print('F')
print_matrix(F)
