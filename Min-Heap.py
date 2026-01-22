class MinHeap:
    """
    Min Heap Data Structure (Array-based)

    Property:
        The value at each parent node is smaller than or equal to
        the values of its children.

    Storage:
        The heap is stored in a list.
        Index rules:
            parent(i) = (i - 1) // 2
            left(i)   = 2*i + 1
            right(i)  = 2*i + 2
    """

    def __init__(self):
        # List to store heap elements
        self.heap = []

    # ---------- Index helper methods ----------
    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    # ---------- Core operations ----------
    def insert(self, value):
        """
        Insert a value into the heap.

        Steps:
        1. Add value at the end of the list.
        2. Move it up (heapify up) until heap property is satisfied.
        """
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """
        Remove and return the minimum element (root).

        Steps:
        1. Save the root value.
        2. Move last element to root.
        3. Heapify down to restore heap property.
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def get_min(self):
        """
        Return the minimum element without removing it.
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    # ---------- Heapify operations ----------
    def heapify_up(self, index):
        """
        Move the element at index up until heap property holds.
        """
        while index > 0:
            parent_index = self.parent(index)

            if self.heap[index] < self.heap[parent_index]:
                # Swap child and parent
                self.heap[index], self.heap[parent_index] = \
                    self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        """
        Move the element at index down until heap property holds.
        """
        size = len(self.heap)

        while True:
            left_index = self.left(index)
            right_index = self.right(index)
            smallest = index

            if left_index < size and self.heap[left_index] < self.heap[smallest]:
                smallest = left_index

            if right_index < size and self.heap[right_index] < self.heap[smallest]:
                smallest = right_index

            if smallest != index:
                # Swap parent with smallest child
                self.heap[index], self.heap[smallest] = \
                    self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    # ---------- Utility methods ----------
    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def display(self):
        print(self.heap)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    h = MinHeap()
    h.insert(10)
    h.insert(5)
    h.insert(20)
    h.insert(2)

    h.display()          # Heap structure (not sorted)
    print(h.get_min())   # 2

    while not h.is_empty():
        print(h.extract_min())
