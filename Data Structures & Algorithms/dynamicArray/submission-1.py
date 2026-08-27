class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.a = [None] * capacity

    def get(self, i: int) -> int:
        return self.a[i]

    def set(self, i: int, n: int) -> None:
        self.a[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.a[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        value = self.a[self.size]
        self.a[self.size] = None
        return value

    def resize(self) -> None:
        self.capacity *= 2
        new_a = [None] * self.capacity

        for i in range(self.size):
            new_a[i] = self.a[i]

        self.a = new_a

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity