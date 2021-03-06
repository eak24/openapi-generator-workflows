from scripts.postprocess import process_openapi
import json
import subprocess
import os
import copy


def test_post_process():
    dir = os.getcwd()
    test_path = dir + '/tests/test-data/test-json-with-paths.json'
    config_path = dir + '/tests/test-data/postprocess_config.json'
    openapi = json.loads(open(test_path).read())
    assert process_openapi(copy.deepcopy(openapi), {"excludedOperationIds": ["pingGet"]}) == {'paths': {}}
    assert process_openapi(copy.deepcopy(openapi), {"excludedOperationIds": ["noExist"]}) == {'paths': {'/ping': {'get': {'operationId': 'pingGet'}}}}
    assert subprocess.run(f"python scripts/postprocess.py {test_path} {config_path} /tmp/openapi.json", shell=True).returncode == 0
    assert subprocess.run(f"python scripts/postprocess.py {test_path} bogus /tmp/openapi.json",
                          shell=True).returncode == 0