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