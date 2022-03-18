from src.node import Node
from src.node_queue import NodeQueue
from src.html_generator import HtmlGenerator


class Runner:

    def run(self, first, answer):
        node = Node(first, answer, g=0)

        # open 리스트
        open_queue = NodeQueue()
        open_queue.push(node)

        # 이미 탐색한 노드들을 저장하는 set
        while open_queue:
            node = open_queue.pop()  # OPEN 리스트의 앞에서 삭제
            # node.print()

            if node.is_answer():
                print("탐색 성공")
                break
            open_queue.mark_as_searched(node)

            node.expand()
            for child in node.child_nodes:
                if open_queue.is_searchable(child):
                    open_queue.push(child)  # OPEN 리스트의 끝에 추가

        return node


if __name__ == '__main__':
    first = [2, 8, 3,
             1, 6, 4,
             7, 0, 5]

    answer = [1, 2, 3,
              8, 0, 4,
              7, 6, 5]

    answer_node = Runner().run(first, answer)

    HtmlGenerator(answer_node).export()
