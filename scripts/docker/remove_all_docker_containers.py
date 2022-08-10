import subprocess
import sys

import click


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


@click.command()
@click.option('--action', prompt="You can choose 'stop' or 'remove'",
              help="""stop: Stops all running docker containers.\
              remove: Removes all running docker containers after stop
              These actions are irreversible.""")
def ask_user(action):
    if action == 'stop':
        action = 'stopped'
    elif action == 'remove':
        action = 'removed'

    running, not_running = count_container()

    while True:
        print("----------------------------------------------------------")
        print(f"Running Containers: {bcolors.OKGREEN}{running}{bcolors.ENDC}\n"
              f"Not running containers: {bcolors.FAIL}{not_running}{bcolors.ENDC}")
        print(f"All of these containers on your system will be "
              f"{bcolors.BOLD}{action}{bcolors.ENDC}.")
        print("----------------------------------------------------------")
        answer = input("Continue? (y/N):\n")
        if any(answer.lower() == f for f in ['y']):
            if action == 'stopped':
                stop_containers()
            elif action == 'removed':
                remove_containers()
        elif any(answer.lower() == f for f in ['n', '']):
            print("exit")
            sys.exit()
        else:
            print("Please enter 'y' or 'n'")


def count_container():
    status_running = subprocess.run(
        "docker ps -q | wc -l",
        shell=True,
        stdout=subprocess.PIPE
    ).stdout

    status_any = subprocess.run(
        "docker ps -aq | wc -l",
        shell=True,
        stdout=subprocess.PIPE
    ).stdout

    return int(status_running), int(status_any) - int(status_running)


def stop_containers():
    try:
        subprocess.run("docker stop $(docker ps -a -q)", shell=True, check=True,
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print("Cannot stop docker containers.")
        sys.exit()

    print("All docker containers are stopped successfully.")


def remove_containers():
    stop_containers()
    try:
        subprocess.run("docker rm $(docker ps -a -q)", shell=True, check=True,
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print("Cannot remove docker containers.")
        sys.exit()

    print("All docker containers are removed successfully.")


if __name__ == '__main__':
    ask_user()
