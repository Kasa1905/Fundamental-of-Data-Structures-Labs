# Write a Python program to compute following computation on matrix:
# a) Addition of two matrices b) Subtraction of two matrices
# c) Multiplication of two matrices d) Transpose of a matrix
import numpy as np

def Add(n1,n2):
    if r1!=r2 or c1!=c2:
        s="Error!! Check your rows and columns! "
        return s
    c=[]
    for i in range(r1):    
        a = []
        for j in range(c1):   
            a.append(0)
        c.append(a)
    for i in range(0,r1):
        for j in range(0,c1):
            c[i][j]=m1[i][j]+m2[i][j]
    return c

def Sub(n1,n2):
    if r1!=r2 or c1!=c2:
        s="Error!! Check your rows and columns! "
        return s
    c=[]
    for i in range(r1):    
        a = []
        for j in range(c1):   
            a.append(0)
        c.append(a)
    for i in range(0,r1):
        for j in range(0,c1):
            c[i][j]=m1[i][j]-m2[i][j]
    return c

def Mul(n1,n2):
    if c1==r2:
        c=[]
        for i in range(r1):    
            a = []
            for j in range(c2):   
                a.append(0)
            c.append(a)
        c = np.dot(n1,n2)
        return c
    else:
        s="Error!! Check your rows and columns! "
        return s








r1=int(input("Enter number of rows for 1st matrix: "))
c1=int(input("Enter number of columns for 1st matrix: "))
m1=[]
print("Enter elements: ")
for i in range(r1):    
    a = []
    
    for j in range(c1):   
        a.append(int(input()))
    m1.append(a)
print("-----------------------------------------------------------------")
r2=int(input("Enter number of rows for 2nd matrix: "))
c2=int(input("Enter number of columns for 2nd matrix: "))
m2=[]
print("Enter elements: ")
for i in range(r2):    
    a = []
    for j in range(c2):   
        a.append(int(input()))
    m2.append(a)
print("---------------------------------------------------")
print("Your matrices are:")
print("m1: ",m1,"\n&\n","m2: ",m2,"\n",sep="",end="")

print("Addition of m1 and m2:\n",Add(m1,m2))
print("Subraction of m2 from m1:\n",Sub(m1,m2))
print("Subraction of m1 from m2:\n",Sub(m2,m1))
print("multiplication of m1 and m2:\n",Mul(m1,m2))