class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError("Invalid Input")
        self._capacity = capacity
        self.cookies = 0


    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if n < 0 or not isinstance(n, int):
            raise ValueError("Invalid Input")
        if self.cookies + n > self._capacity:
            raise ValueError("Jar is already full")
        self.cookies += n

    def withdraw(self, n):
        if n < 0 or not isinstance(n, int):
            raise ValueError("Invalid Input")
        if self.cookies - n < 0:
            raise ValueError("Jar is already empty")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies


jar = Jar(12)
print(str(jar))
print(jar.capacity)
