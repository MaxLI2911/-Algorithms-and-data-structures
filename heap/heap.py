#parent(i) = (i-1)//arn
#children(i) = (i*arn+1, i*arn+2, i*arn+arn...)

class Heaps:
    def __init__(self, arnosc):
        self.arnosc = arnosc
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        child_index = len(self.heap)-1
        while True:
            parent_index = (child_index-1)//self.arnosc

            if parent_index >= 0 and self.heap[child_index] > self.heap[parent_index]:
                self.heap[parent_index], self.heap[child_index] = self.heap[child_index], self.heap[parent_index]
                child_index = parent_index
            else:
                break

    def delete_peak(self):
        leng = len(self.heap)-1
        if leng < 0:
            return None
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        parent_index = 0
        largest_index = 0
        while True:
            for i in range(1, self.arnosc+1):
                child_index = parent_index * self.arnosc + i
                if child_index < leng and self.heap[child_index] > self.heap[largest_index]:
                    largest_index = child_index

            if largest_index != parent_index:
                self.heap[parent_index], self.heap[largest_index] = self.heap[largest_index], self.heap[parent_index]
                parent_index = largest_index
            else:
                break

    def display(self):
        level = 0
        index = 0
        while index < len(self.heap):
            end_index = index + self.arnosc ** level
            print(" ".join(map(str, self.heap[index:end_index])))
            index = end_index
            level += 1
