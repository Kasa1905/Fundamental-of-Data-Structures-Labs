'''
Write a Python program to store second year percentage of students in array. Write
function for sorting array of floating point numbers in ascending order using
a) Insertion sort
b) Shell Sort and display top five scores
'''

second_year_percentage=[76.5,57.5,98.5,97.6,74.4,65.54]
# Insertion Sort
def insertion_sort(arr):
       for i in range(1, len(arr)):
              key = arr[i]
              j = i - 1
              while j >= 0 and key < arr[j]:
                     arr[j + 1] = arr[j]
                     j -= 1
              arr[j + 1] = key
       return arr

# Shell Sort
def shell_sort(arr):
       n = len(arr)
       gap = n // 2
       while gap > 0:
              for i in range(gap, n):
                     temp = arr[i]
                     j = i
                     while j >= gap and arr[j - gap] > temp:
                            arr[j] = arr[j - gap]
                            j -= gap
                     arr[j] = temp
              gap //= 2
       return arr

# Display top five scores
def display_top_five(arr):
       print("Top five scores:")
       for i in range(1, 6):
              print(f"{i}. {arr[-i]}")

print("Using Insertion Sort")
insertion_sort(second_year_percentage)
print("Sorted percentages:", second_year_percentage)
print("\nUsing Shell Sort:")
shell_sort(second_year_percentage)
print("Sorted percentages:", second_year_percentage)
print()
display_top_five(second_year_percentage)
