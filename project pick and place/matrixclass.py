class Matrix:
    value = []
    def __init__(self,_value):
        self.value = _value

    def Zeros(i,j):
        matout = []
        for a in range(i):
            matout.append([])
            for b in range(j):
                matout[a].append(0.0)
        return Matrix(matout)


    def GetRowColumn(self):
        '''Returns the rows and column size (rows, columns)'''
        return  len(self.value), len(self.value[0])
    
    def Transpose(self):
        r, c = self.GetRowColumn()
        
        matout = Matrix.Zeros(c, r)

        for i in range(r):
            for j in range(c):
                matout.value[j][i] = self.value[i][j]

        return matout
    
    def Inverse(self):
        ##magic code
        matin = Matrix(self.value)

        r, c = self.GetRowColumn()
        if(r != c):
            raise Exception("Matrix Row and Column lenght are not the same")
        
        matout = Matrix.Zeros(r,c)

        for row in range(r):
            for col in range(c):
                matout.value[row][col] = (-matin.value[row][col])
        
        for i in range(r):

            if(matout.value[i][i] == 0.0):
                raise Exception("Matrix doesn't have an inverse")
                
            
            else:
                matout.value[i][i] = (-1/matout.value[i][i])

            for j in range(r):
                if(j != i):
                    matout.value[j][i] = matout.value[j][i] * matout.value[i][i]
            
            for j in range(r):
                if(j != i):
                    for k in range(r):
                        if(k != i):
                            matout.value[j][k] = matout.value[j][k] + matout.value[j][i] * matout.value[i][k]
            for j in range(r):
                if(j != i):
                    matout.value[i][j] = matout.value[i][j] * matout.value[i][i]
        
        return matout
    
    

    def __add__(self,other):
        raise NotImplemented("not yet implemented")
    
    def __mul__(self,_other):
        
        #checks of de matixen compatiable zijn
        if(self.GetRowColumn()[1] == _other.GetRowColumn()[0]):
            #good
            other = _other
        elif(self.GetRowColumn() == _other.GetRowColumn()):
            #transplose
            other = _other.Transpose()
                       
        else:
            raise Exception("Matrixes can't be multiplied")
        
        
        matout = Matrix.Zeros(self.GetRowColumn()[0],other.GetRowColumn()[1])
       
        
        for rA in range(self.GetRowColumn()[0]):
            for cB in range(other.GetRowColumn()[1]):
                temp = 0.0
                for cA in range(self.GetRowColumn()[1]):
                    temp += self.value[rA][cA] * other.value[cA][cB]
                matout.value[rA][cB] = temp

        return matout

    def __str__(self):
        
        r, c = self.GetRowColumn()
        output = ""
        
        hasNegative = 0

        temp = []
        for a in range(r):
            temp.append([])
            for b in range(c):
                _str = ("%.5f" % (self.value[a][b]))
                print(_str)
                temp[a].append(len(_str))
        
        maxValue = 0
        maxValueArray = []

        print(temp)

        for i in range(r):
            maxValueArray.append(max(temp[i]))

        maxValue = max(maxValueArray)
        print(maxValue)

        # print(temp)
       
       
        for row in range(r):
            output += "["
            for col in range(c):
               
                output += " " * (maxValue - temp[row][col])
                output += " %.5f " % (self.value[row][col]) 
            output += "] \n"
        
        return output







        

A = Matrix(
    [
    [100,100,1],
    [0,100,1],
    [-100,100,1],
    [100,0,1],
    [0,0,1],
    [-100,0,1],
    [100,-100,1],
    [0,-100,1],
    [-100,-100,1]
    ]
)

B = Matrix(
        [
            [-10,-1]
        ]

)


AT = A.Transpose()

ATA = AT*A

INVERSEATA = ATA.Inverse()

BANAAN = INVERSEATA*AT

print(A)










