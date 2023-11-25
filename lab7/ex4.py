import os
import sys

try:
    assert (len(sys.argv) == 2), "Expected 1 argument"

    dir = sys.argv[1]
    assert (os.path.isdir(dir)), "Invalid directory"
    assert (len(os.listdir(dir)) > 0), "Empty directory"

    ext_count = {}

    root, directories, files = next(os.walk(dir))

    for fileName in files:
        ext = ""
        poz = fileName.find(".")
        if poz != -1:
            ext = fileName[poz:] # se obtine extensia
        if ext in ext_count:
            ext_count[ext] += 1
        else:
            ext_count[ext] = 1

    for key, value in ext_count.items():
        print(f"The extension {key} appears {value} times")

except PermissionError as e:
    print(f"You don't have the permission to read this directory")
except Exception as e:
    print(e)
