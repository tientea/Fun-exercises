# The exercise can be found at: http://www.practicepython.org/exercise/2014/11/11/20-element-search.html
#
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) 
# and another number. The function decides whether or not the given number is inside the list and returns (then prints) 
# an appropriate boolean. THIS TIME, WITH THE EXTRA: USING BINARY SEARCH.

# find is a function that takes an ordered list of numbers and another number,
# returning true or false whether the element appears in the list
# 
# l is a list ordered from smallest to largest
# element is the number to find in the original list
def find(a, n):
  start = 1
  end = len(a) - 1
    
  while True:
    middle_index = (end - start) // 2
    if middle_index < start or middle_index > end or middle_index < 0:
        return False
    
    middle = a[middle_index]
    if middle == n:
        return True
    elif middle < n:
        end = middle
    else:
        start = middle
        
if __name__=="__main__":
    a = [1, 3, 5, 30, 42, 43, 500]
    print(find(a, 6))
    print(find(a, 500))
    print(find(a, -1))
    print(find(a, 45))