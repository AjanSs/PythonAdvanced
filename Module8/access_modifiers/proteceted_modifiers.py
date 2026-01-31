class Square:
    def __init__(self):
        self._length = "This variable is with length 5"
    def _area(self,length):
        return self.length * self.length

square = Square()
print(square._length)

