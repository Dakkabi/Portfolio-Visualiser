import os


def get_project_root_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..")

def get_resources_path():
    return os.path.join(get_project_root_path(), "backend", "resources")
