import os
import sys

try:
    assert (len(sys.argv) == 3), "Expected 2 arguments"

    dir = sys.argv[1]
    ext = sys.argv[2]
    assert (os.path.isdir(dir)), "Invalid directory"
    assert (ext.count(".") == 1), "Invalid extension"

    for (root, directories, files) in os.walk(dir):
        for fileName in files:
            if fileName.endswith(ext):
                full_fileName = os.path.join(root, fileName)
                print(f"{full_fileName}:")
                try:
                    f = open(full_fileName)
                    for line in f:
                        print(line.strip())
                    f.close()
                except FileNotFoundError as e:
                    print(f"Unable to find file: {e.filename}")
except Exception as e:
    print(e)
