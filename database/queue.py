class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def queue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None  # Можете выбрать другой способ обработки пустого стека

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    def clean(self):
        self.items = []


no_subs = Queue()


