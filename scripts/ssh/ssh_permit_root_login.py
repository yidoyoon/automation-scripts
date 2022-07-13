import sys

ssh_path = sys.argv[1]
root_no = "# PermitRootLogin no"
root_yes = "PermitRootLogin yes"


def valid(target, data):
    if target in data:
        return True
    else:
        if root_yes in data:
            print("SSH root login is already enabled. ")
    return False


def enable_ssh_root(ssh_path):
    try:
        fin = open(ssh_path, 'rt')
        data = fin.read()
        if valid(root_no, data):
            print("SSH root login enabled. ")
            data = data.replace(root_no, root_yes, 1)
        else:
            print("Nothing to replace. ")
            fin.close()
            exit()

        fin.close()

        fin = open(ssh_path, 'wt')
        fin.write(data)
        fin.close()
    except FileNotFoundError:
        print(f"No file named {ssh_path}.")
        exit()


if __name__ == '__main__':
    enable_ssh_root(ssh_path)
