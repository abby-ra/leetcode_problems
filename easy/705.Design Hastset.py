class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.data = [[] for _ in range(self.size)]

    def get_index(self, key):
        return key % self.size

    def add(self, key):
        i = self.get_index(key)
        if key not in self.data[i]:
            self.data[i].append(key)

    def remove(self, key):
        i = self.get_index(key)
        if key in self.data[i]:
            self.data[i].remove(key)

    def contains(self, key):
        i = self.get_index(key)
        return key in self.data[i]
