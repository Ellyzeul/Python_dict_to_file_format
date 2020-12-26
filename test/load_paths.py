import sys, os


def load_paths():
    project_root = os.path.dirname(os.path.realpath(__file__)) + '\\..'

    sys.path.insert(1, project_root)
    sys.path.insert(1, project_root + '\\src')