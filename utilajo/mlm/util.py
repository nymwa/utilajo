import sys
import yaml

def read_yaml():
    return yaml.safe_load(sys.stdin)

def print_yaml(data):
    yml = yaml.safe_dump(data, allow_unicode = True)
    print(yml)

