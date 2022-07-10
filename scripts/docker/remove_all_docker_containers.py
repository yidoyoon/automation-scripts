import sys
import subprocess


def remove_containers():
    print("Removing all docker containers.")
    try:
        subprocess.run(
            "docker stop $(docker ps -a -q)",
            shell=True,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        print("Cannot stop docker containers.")
        sys.exit()

    try:
        subprocess.run(
            "docker rm $(docker ps -a -q)",
            shell=True,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print("All docker containers are removed successfully.")
    except subprocess.CalledProcessError as e:
        print("Cannot remove docker containers.")
        sys.exit()


def ask_user():
    while True:
        print("All of your docker containers on your host will be removed.")
        answer = input("Continue? (y/N)")
        if any(answer.lower() == f for f in ['y']):
            remove_containers()
            break
        elif any(answer.lower() == f for f in ['n', '']):
            break
        else:
            print("Please enter 'y' or 'n' ")


ask_user()
