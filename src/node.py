class Node:
    def __init__(self, elements, answer, g, parent=None):
        self.elements = elements
        self.answer = answer
        self.parent = parent

        self.g = g
        self.h = self.__get_heuristic(answer)

        self.child_nodes = []

    @property
    def f(self):
        return self.g + self.h

    def is_answer(self):
        return self.h == 0

    def __get_heuristic(self, answer: list):
        heuristic = 0
        for i, element in enumerate(self.elements):
            if element not in [0, answer[i]]:
                heuristic += 1
        return heuristic

    def get_new_node(self, i1, i2):
        new_elements = self.elements[:]
        new_elements[i1], new_elements[i2] = new_elements[i2], new_elements[i1]
        return Node(new_elements, self.answer, parent=self, g=self.g + 1)

    def expand(self):
        i = self.elements.index(0)
        if i not in [0, 3, 6]:
            self.child_nodes.append(self.get_new_node(i, i - 1))
        if i not in [0, 1, 2]:
            self.child_nodes.append(self.get_new_node(i, i - 3))
        if i not in [6, 7, 8]:
            self.child_nodes.append(self.get_new_node(i, i + 3))
        if i not in [2, 5, 8]:
            self.child_nodes.append(self.get_new_node(i, i + 1))

    def print(self):
        print(self.get_message().replace('<br>', '\n'))
        print()

    def get_message(self):
        return f"""f(n) = g(n) + h(n) = {self.g}  + {self.h}<br>{'<br>'.join(str(row) for row in [self.elements[:3], self.elements[3:6], self.elements[6:]])}"""

    def get_json(self, desc):
        description = {'trad': self.get_message()}
        if hasattr(self, 'mark'):
            description['styles'] = {'box-shadow': '0 0 15px 2px blue'}
        if self.is_answer():
            description['styles'] = {'box-shadow': '0 0 15px 2px red'}
        desc[str(id(self))] = description

        return {str(id(child)): child.get_json(desc) for child in self.child_nodes}

    def __str__(self):
        return ''.join(map(str, self.elements))

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def __gt__(self, other):
        return self.f > other.f

    def __ge__(self, other):
        return self.f >= other.f
