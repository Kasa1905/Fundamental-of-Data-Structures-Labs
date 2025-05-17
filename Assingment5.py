'''
Write a Python program to store first year percentage of students in array. Write
function for sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores
'''

percentages = [55.6, 98.9, 52.3, 61.4, 88.5, 44.8, 91.2, 77.6, 89.4, 67.1]
# Selection Sort
def selection_sort(arr):
       n = len(arr)
       for i in range(n):
              min_index = i
              for j in range(i+1, n):
                     if arr[j] < arr[min_index]:
                            min_index = j
              arr[i], arr[min_index] = arr[min_index], arr[i]

# Bubble Sort
def bubble_sort(arr):
       n = len(arr)
       for i in range(n):
              for j in range(0, n-i-1):
                     if arr[j] > arr[j+1]:
                            arr[j], arr[j+1] = arr[j+1], arr[j]

# Display top five scores
def display_top_five(arr):
       print("Top five scores:")
       for i in range(min(5, len(arr))):
              print(arr[-(i+1)])

print("Using Selection Sort")
selection_sort(percentages)
print("Sorted percentages:", percentages)
print("\nUsing Bubble Sort:")
bubble_sort(percentages)
print("Sorted percentages:", percentages)
print()
display_top_five(percentages)
