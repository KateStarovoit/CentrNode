class MyQueue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        if len(self.__queue) != 0:
            return str(self.__queue[-1])
        else:
            return '"queue is empty"'

    __repr__ = __str__

    def is_empty(self):
        return len(self.__queue) == 0

    def top(self):
        return self.__queue[-1]

    def enqueue(self, value):
        self.__queue.insert(0, value)

    def dequeue(self):
        return self.__queue.pop(-1)


qwe = MyQueue()
qwe.enqueue(1)
qwe.enqueue(2)
qwe.enqueue(4)
qwe.enqueue(6)
print(qwe)
