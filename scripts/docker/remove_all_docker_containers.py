import sys
import subprocess


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


remove_all_docker_containers()
