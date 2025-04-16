class MyQueue:
    def __unit__(self):
        self.items = []
    def enQueue(self, item):
        self.items.append()
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == []
    def front(self):
        return self.items[0]
    def show(self):
        print(self.items)
queue = MyQueue()
print(queue.isEmpty())
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.show()
print(f"antrian terdepan adalah: [Queue.front()]")
queue.deQueue()
print(f"antrian terdepan adalah: [Queue.front()]")