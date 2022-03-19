import heapq


class NodeQueue:

    def __init__(self):
        self.queue = []

        self.open_set = set()
        self.already_searched_set = set()

    def push(self, node):
        heapq.heappush(self.queue, node)
        self.open_set.add(str(node))

    def pop(self):
        node = heapq.heappop(self.queue)
        self.open_set.remove(str(node))
        return node

    def mark_as_searched(self, node):
        self.already_searched_set.add(str(node))

    def is_searchable(self, node):
        if str(node) in self.already_searched_set:
            return False
        if str(node) in self.open_set:
            return False
        return True


class NodeQueueList:

    def __init__(self):
        self.queue = []

        self.open_set = set()
        self.already_searched_set = set()

    def push(self, node):
        self.queue.append(node)
        self.open_set.add(str(node))

    def pop(self):
        node = self.queue.pop()
        self.open_set.remove(str(node))
        return node

    def mark_as_searched(self, node):
        self.already_searched_set.add(str(node))

    def is_searchable(self, node):
        if str(node) in self.already_searched_set:
            return False
        if str(node) in self.open_set:
            return False
        return True
