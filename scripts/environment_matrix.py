import sys
import json


def to_env_array(generator_repos: str):
    generator_repos = json.loads(generator_repos)
    print(json.dumps({"env": [{"GENERATOR_REPO": r} for r in generator_repos]}))


if __name__ == '__main__':
    to_env_array(sys.argv[1])