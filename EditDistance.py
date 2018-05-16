from random import *

Gene_list = ["A","T","G","C"]

def Get_Gene(list):
   G_len = randint(15,31) # size of Gene
   for i in range(G_len):
       G_Type = randint(0,3) # Gene's type
       list.append(Gene_list[G_Type])

def T_Min(A,B,C): # A = left, B = diagonal, C = upper
    if(B <= A and B <= C):
        return 2
    elif(A <= B and A <= C):
        return 1
    else:
        return 3

def EditDistance(A,B,T): # A -> Big size, B -> Small size, T -> Table
    for i in range(1,len(B)+1):
        for j in range(1,len(A)+1):
            data = T_Min(T[i][j-1],T[i-1][j-1],T[i-1][j])
            if(data == 2):
                if(A[j-1] == B[i-1]):
                    T[i][j] = T[i-1][j-1]
                else:
                    T[i][j] = T[i-1][j-1]+1
            elif(data == 1):
                T[i][j] = T[i][j-1]+1
            else:
                T[i][j] = T[i-1][j] + 1
    return T[len(B)][len(A)]

# Main
Sum_EditDistance = 0
Sum_Similarity = 0
for count in range(50):
    Table = []
    X = []
    Y = []
    Get_Gene(X)
    Get_Gene(Y)

    if(len(X) > len(Y)):
        Table = [[0 for i in range(len(X)+1)]for j in range(len(Y)+1)]
    else:
        Table = [[0 for i in range(len(Y)+1)]for j in range(len(X)+1)]

    if(len(X) > len(Y)):
        for i in range(len(X)+1):
            Table[0][i] = i
        for i in range(len(Y)+1):
         Table[i][0] = i
    else:
        for i in range(len(Y)+1):
            Table[0][i] = i
        for i in range(len(X)+1):
            Table[i][0] = i
    
    if(len(X) > len(Y)):
        result = EditDistance(X,Y,Table)
    else:
        result = EditDistance(Y,X,Table)
    
    print(count+1,'. A = ',X )


    if(len(X) > len(Y)):
        similarity = len(X) - result
    else:
        similarity = len(Y) - result
    Sum_EditDistance += result
    Sum_Similarity += similarity
    if(count+1 <10):
        print('    B = ',Y)
        print('    EditDitance = ',result,'   Similarity = ',similarity)
    else:
         print('     B = ',Y)
         print('     EditDitance = ',result,'   Similarity = ',similarity)
    print()

print('=============================================')
print('평균 유사도 = ',Sum_Similarity/50,' 평균 편집거리 = ',Sum_EditDistance/50)