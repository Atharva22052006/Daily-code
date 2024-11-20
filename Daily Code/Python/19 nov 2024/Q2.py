# Lists and Loops:

# Given a list of integers, write a function to remove all duplicates and return the sorted list in ascending order. Use a loop to achieve this instead of using set().


numbers = [4, 2, 9, 4, 7, 2, 9, 1, 3, 3]
largest=max(numbers)

new_list=[]

for num in numbers:
    if num not in new_list:  
        new_list.append(num)
    
new_list.sort()

for num in new_list:
    print(num)
    
    
    

