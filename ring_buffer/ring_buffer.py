class RingBuffer:
    ''' 
        Attributes:
            self.capacity = Capacity of the buffer
            self.oldest_elem_index = Index to kep track of the oldest elements
            self.buffer = The storage
        Append:
            Attributes:
            Step 1: Check if the legnth of the buffer is equal to 5. If it is  then we want to first remove the oldest element 
            Step 2: insert the new Item into the oldest elements position 
            Step 3: Update the oldest elements index to point to the next oldest elements
            Step 4: Check if we have arrive at the last element of the buffer, if so we have updated all the elements in the buffer 
                    and now we want to reset the oldest elements index to point to the first element in the buffer
            Step 5: Is the else case just adding items in  the buffer when it is still empty/Not yet full

        Get:
            basically just return the current elements in the buffer

    '''

    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest_elem_index = 0
        self.buffer = []
        pass

    def append(self, item):

        if len(self.buffer) == self.capacity:
            self.buffer.pop(self.oldest_elem_index)
            self.buffer.insert(self.oldest_elem_index, item)
            self.oldest_elem_index += 1

            if self.oldest_elem_index == 5:
                self.oldest_elem_index = 0
        else:
            self.buffer.append(item)

        pass

    def get(self):

        return self.buffer
