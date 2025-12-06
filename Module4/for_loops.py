names = ["Alice","Bob","David","Charlie"]
for name in names:
    print(name)

sentence = "Hello, world!"

for ch in sentence:
    if ch.isalpha():
        print(ch)

for number in range(1,6):
    print(number)

numbers=[12,43,5,7,65]

max = numbers[0]

for num in numbers:
    if num > max:
        max = num
print("Maksimumi eshte:", max)

count = 1
while count <=5:
    print("Rrite vleren per nje: ",count)
    count+=1

numbers = [1,2,3,4,5,6]
target = 4

for number in numbers:
    print(number)
    if number == target:
        print("Target found")
        break

scores = [68,42,55,76,35,87,89,55]
total = 0
count = 0

for score in scores:
    if score<50:
        continue
    total+=score
    count+=1

mesatarja = total/count
print("Mesatarja ka qene:",mesatarja)

while True:
    user_input=input("Shtyp nje numer pozitiv:")
    if user_input.isnumeric():
        number = int(user_input)
        if number > 0:
            break
    print("invalid. try again")
print("You enter a positive number")

while True:
    user_input=input("Shtyp nje numer qift:")
    if user_input.isnumeric():
        number = int(user_input)
        if number %2==0:
            break
    print("invalid. Numri tek")
print("You enter a qift number")