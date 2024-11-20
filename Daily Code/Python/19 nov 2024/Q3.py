# Dictionaries and Strings

# Write a program to count the frequency of each character in a string (case-insensitive) and print the results in descending order of frequency. For example, for "Hello World"

a="Hello World"

a=a.lower()

a=a.replace(" ", "")

count={}

for char in a:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
        
    
    
for char, freq in count.items():
    print(f"{char}: {freq}")


