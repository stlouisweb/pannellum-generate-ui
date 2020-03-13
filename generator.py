import generate
import os
from pathlib import Path


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def some_func(filepath):
    print (filepath)
    name = Path(filepath).stem
    print(desktop + "/" + name)
    print(name)
    generate.file(filepath, desktop + "/" + name)

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    some_func()