from src.node import Node
from src.node_queue import NodeQueue, NodeQueueList
from src.html_generator import HtmlGenerator


class Runner:

    def run(self, first, answer):
        node = Node(first, answer, g=0)

        # open 리스트
        open_queue = NodeQueueList()
        open_queue.push(node)

        # 이미 탐색한 노드들을 저장하는 set
        while open_queue:
            # print(len(open_queue.queue)) # queue에 남아있는 항목들 리스트
            node = open_queue.pop()  # OPEN 리스트의 앞에서 삭제
            # node.print() # 현재 선택된 Node

            if node.is_answer(): # 현재 Node가 정답과 같으면 While문 탈출
                print("탐색 성공")
                break

            # 이후에 다른 Node들이 현재 Node와 같은 숫자 배열을 가질때
            # 그냥 넘어가기 위해 이미 탐색된 Node라고 마킹해주는 부분
            open_queue.mark_as_searched(node)

            # 0 을 다른위치로 옮겨서 확인하기위해 상하좌우로 펄치는 부분
            node.expand()

            for child in node.child_nodes:
                # 0이 움직일수 있는지 확인해서 움직일 수 있다면 Queue에 삽입
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
