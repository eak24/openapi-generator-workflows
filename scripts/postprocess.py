import json
import sys


def process_openapi(openapi, post_process_config):
    return OpenApiVisitor(post_process_config["excludedOperationIds"]).visit_openapi(openapi)


def post_process(openapi_file_path: str, post_process_file_path: str, destination_file_path: str):
    with open(openapi_file_path, 'r') as openapi_file:
        openapi = json.load(openapi_file)
        try:
            with open(post_process_file_path) as post_process_file:
                post_process_config = json.load(post_process_file)
                openapi = process_openapi(openapi, post_process_config)
        except FileNotFoundError as e:
            print(f"No postprocess config file here: {post_process_file_path}, exists - skipping postprocessing!")
            return
    with open(destination_file_path, 'w') as destination_file:
        json.dump(openapi, destination_file)


class OpenApiVisitor:

    def __init__(self, operation_ids_to_remove):
        self.operation_ids_to_remove = operation_ids_to_remove

    def visit_openapi(self, openapi):
        paths = {}
        for k, v in openapi["paths"].items():
            p = self.visit_path(v)
            if p and len(p) > 0:
                paths[k] = p
        openapi["paths"] = paths
        return openapi

    def visit_path(self, path):
        result = {}
        for k, v in path.items():
            o = self.visit_operation(v)
            if o and len(o) > 0:
                result[k] = o
        return result

    def visit_operation(self, operation):
        if operation["operationId"] in self.operation_ids_to_remove:
            return None
        return operation


if __name__ == '__main__':
    post_process(sys.argv[1], sys.argv[2], sys.argv[3])
