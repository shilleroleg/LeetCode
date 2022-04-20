class MyHashSet:
    def __init__(self):
        self.hash_set = {}

    def add(self, key: int) -> None:
        if self.contains(key):
            self.hash_set[key] += 1
        else:
            self.hash_set[key] = 1

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hash_set.pop(key)

    def contains(self, key: int) -> bool:
        if key in self.hash_set.keys():
            return True
        else:
            return False


class MyHashMap:

    def __init__(self):
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        return self.hash_map.get(key, -1)

    def remove(self, key: int) -> None:
        self.hash_map.pop(key, -1)


if __name__ == "__main__":

    obj = MyHashSet()

    obj.add(1)
    print(obj.hash_set)
    obj.add(2)
    obj.add(2)
    print(obj.hash_set)
    print(obj.contains(2))
    obj.remove(2)
    print(obj.hash_set)
    print(obj.contains(2))

    obj2 = MyHashMap()
    obj2.put(1, 1)
    obj2.put(2, 2)
    print(obj2.hash_map)
    print(obj2.get(1))
    print(obj2.get(3))
    obj2.put(2, 1)
    print(obj2.get(2))
