class CQueue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        return str(self.__queue)

    __repr__ = __str__

    def __len__(self):
        return len(self.__queue)

    def is_empty(self):
        return len(self.__queue) == 0

    def top(self):
        if not self.is_empty():
            return self.__queue[-1]
        else:
            raise IndexError("Queue is empty")

    def enqueue(self, value):
        self.__queue.insert(0, value)

    def dequeue(self):
        if not self.is_empty():
            self.__queue.pop(-1)
        else:
            raise IndexError("Queue is empty")
