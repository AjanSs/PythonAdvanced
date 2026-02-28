with open('example.txt','r') as file:
    for line in file:
        cleaned_lines = line.strip() # removes whitespace
        print(cleaned_lines)

#Splitting lines into words

with open('example.txt','r') as file:
    for line in file:
        words = line.strip().split() #
        print(words)

        
name = "Alice"
age = 30
with open('output.txt','w') as file:
    file.write("Name:" + name + "\n")
    file.write("Age:" + str(age) + "\n")