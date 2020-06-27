class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest_elem_index = 0
        self.storage = []
        pass

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage.pop(self.oldest_elem_index)
            self.storage.insert(self.oldest_elem_index, item)
            self.oldest_elem_index += 1
            if self.oldest_elem_index == 5:
                self.oldest_elem_index = 0
        else:
            self.storage.append(item)

        pass

    def get(self):

        return self.storage
