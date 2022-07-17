import shutil
import tempfile

from pathlib2 import Path

"""Remove automatically generated annotations when you use
`Leetcode Editor` plugin(https://github.com/shuzijun/leetcode-editor)
in Jetbrains IDE. Only the code(solution) part will be left.
"""


def find_range(file_name):
    begin_string = "//leetcode submit region begin(Prohibit modification and deletion)"
    end_string = "//leetcode submit region end(Prohibit modification and deletion)"
    idxs = []
    with open(file_name, 'r') as fr:
        lines = fr.readlines()
        for i, line in enumerate(lines):
            if line.strip('\n') == begin_string:
                idxs.append(i)
            if line.strip('\n') == end_string:
                idxs.append(i)

    return idxs


def trim_solution(file_name, begin_idx, end_idx):
    with tempfile.TemporaryFile(mode='w+', delete=False) as fw, open(file_name, 'r') as fr:
        lines = fr.readlines()[begin_idx + 1:end_idx]
        fw.writelines(lines)
    shutil.move(fw.name, file_name)


if __name__ == '__main__':
    for path in Path.cwd().rglob('*.cpp'):
        idxs = find_range(path)
        try:
            trim_solution(path, idxs[0], idxs[1])
        except IndexError as e:
            pass
