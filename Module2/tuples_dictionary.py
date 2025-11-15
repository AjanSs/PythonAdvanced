grades = {
    ("John","Math"): 5,
    ("Alice","Biology"): 3,
    ("Eve","Music"): 4,
    ("John","English"): 5
}

john_math = grades[("John","Math")]
print("John's grade in math is",john_math)

grades[("Florjon","Edukat Fizike")] = 5

print(grades)

keys = list(grades.keys())
print(keys)

student, subject = keys[0]
print(student, "'s grade in", subject, "is", john_math)