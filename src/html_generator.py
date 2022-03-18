import os
import datetime
import webbrowser
from pathlib import Path
from os.path import dirname, join


class HtmlGenerator:
    output_dir = join(dirname(dirname(Path(__file__).absolute())), 'output')
    template_file = join(dirname(dirname(Path(__file__).absolute())), 'template', 'sample.html')

    TOKEN = '###HERE###'

    def __init__(self, node):
        while node.parent:
            node = node.parent
            node.mark = True

        description_dict = {}

        self.tree = str({str(id(node)): node.get_json(description_dict)})
        self.params = str(description_dict)

    def get_data_lines(self):
        return f'''
                let tree = {self.tree}
                let params = {self.params}
                '''

    def export(self):
        os.makedirs(self.output_dir, exist_ok=True)

        time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

        with open(self.template_file, 'r', encoding='utf-8') as template_file:
            templates_lines = template_file.readlines()

        output_file_name = join(self.output_dir, time + '.html')
        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            for line in templates_lines:
                if self.TOKEN in line:
                    line = line.replace(self.TOKEN, self.get_data_lines())
                output_file.write(line)

        webbrowser.open(f'file://{output_file_name}', new=2)
        print('###################################')
        print('#######     결과 저장 성공    #######')
        print('###################################')
        print()
        print(f'결과 위치:')
        print(f'> {output_file_name}')
        print(f'>')
        print(f'> 위 파일을 브라우저에서 열어 확인해주세요')
