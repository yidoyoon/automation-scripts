import sys
import subprocess


def ask_user(question):
    while True:
        print(question)
        answer = input("Continue? (y/N)")
        if any(answer.lower() == r for r in ['y']):
            remove_all_docker_containers()
            break
        elif any(answer.lower() == r for r in ['n', '']):
            break
        else:
            print("Please enter 'y' or 'n' ")


def remove_all_docker_containers():
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


ask_user("All of your docker containers on your host will be removed.")
