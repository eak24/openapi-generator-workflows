import os
import shlex
import subprocess
import sys


def get_configs():
    for root, dirs, files in os.walk(os.getcwd(), topdown=True):
        if 'configs' in dirs:
            dirs[:] = ['configs']
        if 'configs' == root.split('/')[-1]:
            print(f'Collecting configs from: {root}')
            return [f'{root}/{f}' for f in files]


def generate(url):
    print(f"Generating from: {url}")
    commands = [f"openapi-generator-cli generate -c {config} -i {url}" for config in get_configs()]
    configs = get_configs()
    print(f'Generating files: {configs}')
    processes = []
    for command in commands:
        processes.append(subprocess.Popen(shlex.split(command)))
    for p in processes:
        p.wait()


if __name__ == "__main__":
    generate(sys.argv[1])
