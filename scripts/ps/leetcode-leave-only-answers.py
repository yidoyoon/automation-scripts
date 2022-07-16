from pathlib2 import Path

begin = "//leetcode submit region begin(Prohibit modification and deletion)"
end = "//leetcode submit region end(Prohibit modification and deletion)"


def leave_only_solution(file_name) -> None:
    """Remove automatically generated annotations when you use
    `Leetcode Editor` plugin(https://github.com/shuzijun/leetcode-editor)
    in Jetbrains IDE. It deletes the first line including the top comment,
    and then deletes it to the end including the bottom comment. In the end,
    only the complete code(solution) part is left.
    """
    with open(file_name, 'r') as fr:
        flag = False
        lines = fr.readlines()
        with open(file_name, 'w') as fw:
            for line in lines:
                if line.strip('\n') == begin:
                    flag = True
                    continue
                if line.strip('\n') == end:
                    flag = False
                if flag:
                    fw.write(line)
    print(f"{file_name} is ready to commit")


if __name__ == '__main__':
    for path in Path.cwd().rglob('*.cpp'):
        leave_only_solution(path)
