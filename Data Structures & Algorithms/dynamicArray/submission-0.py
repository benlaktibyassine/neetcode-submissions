class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.a = [0] * capacity

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
        value = self.a[self.size - 1]
        self.size -= 1
        return value

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_array = [0] * new_capacity

        for i in range(self.size):
            new_array[i] = self.a[i]

        self.a = new_array
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity