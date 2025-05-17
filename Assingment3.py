import numpy as np
def matrix():
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
def class_percent():
       def input_percentage():
              perc = []
              number_of_students = int(input("Enter the number of Students : "))
              for i in range(number_of_students):
                     perc.append(float(input("Enter the percentage of Student {0} : ".format(i+1))))
              return perc
       def print_percentage(perc):
              for i in range(len(perc)):
                     print(perc[i],sep = "\n")
       def percentage_partition(perc,start,end):
              pivot = perc[start]
              lower_bound = start + 1
              upper_bound = end
              while True:
                     while lower_bound <= upper_bound and perc[lower_bound] <= pivot:
                            lower_bound += 1
                     while lower_bound <= upper_bound and perc[upper_bound] >= pivot:
                            upper_bound -= 1
                     if lower_bound <= upper_bound:
                            perc[lower_bound],perc[upper_bound] = perc[upper_bound],perc[lower_bound]
                     else:
                            break
              perc[start],perc[upper_bound] = perc[upper_bound],perc[start]
              return upper_bound
       def Quick_Sort(perc,start,end):
              while start < end:
                     partition = percentage_partition(perc,start,end)
                     Quick_Sort(perc,start,partition-1)
                     Quick_Sort(perc,partition+1,end)
                     return perc
       def display_top_five(perc):
              print("Top Five Percentages are : ")
              if len(perc) < 5:
                     start, stop = len(perc) - 1, -1
              else:
                     start, stop = len(perc) - 1, len(perc) - 6
              for i in range(start, stop, -1):
                     print(perc[i],sep = "\n")
       unsorted_percentage = []
       sorted_percentage = []
       flag = 1
       while flag == 1:
              print("\n--------------------MENU--------------------")
              print("1. Accept the Percentage of Students")
              print("2. Display the Percentages of Students")
              print("3. Perform Quick Sort on the Data")
              print("4. Exit")
              ch = int(input("Enter your choice (from 1 to 4) : "))
              if ch == 1:
                     unsorted_percentage = input_percentage()
              elif ch == 2:
                     print_percentage(unsorted_percentage)
              elif ch == 3:
                     print("Percentages of Students after performing Quick Sort : ")
                     sorted_percentage = Quick_Sort(unsorted_percentage,0,len(unsorted_percentage)-1)
                     print_percentage(sorted_percentage)
                     a = input("Do you want to display the Top 5 Percentages of Students (yes/no) : ")
                     if a == 'yes':
                            display_top_five(sorted_percentage)
              elif ch == 4:
                     print("Thanks for using this program!!")
                     flag = 0
              else:
                     print("Invalid Choice!!")

def pLaying():
       def cp(cktp,badp):
              cmp=[]
              for pc in cktp:
                     for pb in badp:
                            if pc==pb:
                                   cmp.append(pc)
                                   break
                     return cmp
              
              def uncommon(cktp,badp):
                     for i in cktp:
                            for j in badp:
                                   if i==j:
                                          cktp.remove(i)
                                          badp.remove(j)
                                          continue
                     print("The list of players play only cricket:",cktp)
                     print("The list of players who only play badminton:",badp)
              def non(cp,bp,ALL):
                     l=[]
                     for i in cp:
                            for j in ALL:
                                   if i==j:
                                          ALL.remove(i)
                                          continue
                     for i in ALL:
                            for j in bp:
                                   if i==j:
                                          ALL.remove(i)
                                          continue
                     print(len(ALL))
              def onlu(ckp,bap,fop):
                     l1=[]
                     for i in ckp:
                            for j in bap:
                                   if i==j:
                                          ckp.remove(i)
                                   continue
                     for i in fop:
                            for j in ckp:
                                   if i==j:
                                          l1.append(j)
                     print(l1)
              

              ckt=[]
              bad=[]
              fot=[]
              alls=[]
              n=int(input("Enter the number of students in the class"))
              for j in range(0,n):
                     p=input("Enter the name of the student").lower()
                     alls.append(p)
                     print(alls)    
                     nc=int(input("Enter the number of student playing cricket:"))
              for i in range(0,nc):
                     pc=input("Enter the name of the player").lower()
                     ckt.append(pc)
                     print(ckt)
                     nb=int(input("Enter the number of students playing badminton"))
              for j in range(0,nb):
                     ph=input("Enter the name of the player").lower()
                     bad.append(ph)
                     print(bad)
                     nf=int(input("Enter the number of students playing football"))
              for j in range(0,nf):
                     pf=input("Enter the name of the player").lower()
                     fot.append(pf)
                     print(fot)
                     print("Players who play both the sports: ",cp(ckt,bad))
              uncommon(ckt,bad)
              non(alls,ckt,bad)
              onlu(ckt,bad,fot)
                                   
def all_sort():
       def bubble_sort(arr):
              n = len(arr)
              for i in range(n):
                     for j in range(0, n - i - 1):
                            if arr[j] > arr[j + 1]:
                                   arr[j], arr[j + 1] = arr[j + 1], arr[j]
              return arr

       def selection_sort(arr):
              for i in range(len(arr)):
                     min_idx = i
                     for j in range(i + 1, len(arr)):
                            if arr[min_idx] > arr[j]:
                                   min_idx = j
                     arr[i], arr[min_idx] = arr[min_idx], arr[i]
              return arr

       def insertion_sort(arr):
              for i in range(1, len(arr)):
                     key = arr[i]
                     j = i - 1
                     while j >= 0 and key < arr[j]:
                            arr[j + 1] = arr[j]
                            j -= 1
              arr[j + 1] = key
              return arr

       def quick_sort(arr):
              if len(arr) <= 1:
                     return arr
              pivot = arr[len(arr) // 2]
              left = [x for x in arr if x < pivot]
              middle = [x for x in arr if x == pivot]
              right = [x for x in arr if x > pivot]
              return quick_sort(left) + middle + quick_sort(right)
       arr = list(map(int, input("Enter the array elements separated by space: ").split()))
       print("Original array:", arr)
       print("Bubble sort:", bubble_sort(arr.copy()))
       print("Selection sort:", selection_sort(arr.copy()))
       print("Insertion sort:", insertion_sort(arr.copy()))
       print("Quick sort:", quick_sort(arr.copy()))
       
       
print("Welcome to the program \n-->1.]Matrix operations \n-->2.]Calculating the class percentages \n-->3.]Sorting students according to the sports they play \n-->4.]All types of sorting on a single array")
choice=int(input("Enter you choice(between 1 to 4): "))
if choice==1:
       matrix()
elif choice==2:
       class_percent()
elif choice==3:
       pLaying()
elif choice==4:
       all_sort()
else:
       print("Wrong choice.")
print("\nThanks for using this program!!")