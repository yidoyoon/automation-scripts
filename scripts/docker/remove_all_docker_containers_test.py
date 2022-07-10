import subprocess
import sys

import pytest
from remove_all_docker_containers import remove_containers


def setup():
    """Run a temporary container(busybox) to prevent the test from
    unexpected shutdown because there are no running containers.
    """
    try:
        subprocess.run(
            "docker run -it -d busybox",
            shell=True,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    except subprocess.CalledProcessError as e:
        print("Cannot run docker busybox.")
        sys.exit()


@pytest.fixture
def remain_containers_after_remove():
    """Count remain docker containers after running
    remove_all_docker_containers.
    """
    remove_containers()

    count = subprocess.run(
        "docker ps -q | wc -l",
        shell=True,
        stdout=subprocess.PIPE
    ).stdout
    return int(count)


def test_remove_all_docker_containers(remain_containers_after_remove):
    assert remain_containers_after_remove == 0
