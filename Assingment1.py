'''
In second year computer engineering class, group A student's play cricket, group B students play badminton and group C students play football. 
Write a Python program using functions to compute following: -
    a) List of students who play both cricket and badminton
    b) List of students who play either cricket or badminton but not both 
    c) Number of students who play neither cricket nor badminton 
    d) Number of students who play cricket and football but not badminton. 

(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)
'''
def intersection(I1,I2):
       res=[]
       for student in I1:
              if student in I2:
                     res.append(student)
       return res

def union(I1,I2):
       res=I2.copy()
       for student in I1:
              if not student in I2:
                     res.append(student)
       return res



def diff(I1,I2):
       res=[]
       for student in I1:
              if not student in I2:
                     res.append(student)
       return res


a=[1,2,3,4,5,6,7]
b=[2,3,6,7,9,10]
c=[2,4,6,8,10,12]
print(f"A={a}\nB={b}\nC={c}\n") 
print(f"a. {intersection(a,b)}")
print(f"b. {diff(union(a,b),intersection(a,b))}")
print(f"c. {diff(diff(c,b),a)}")
print(f"d. {diff(union(a,c),b)}")