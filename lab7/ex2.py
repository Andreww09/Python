import os

try:

    dir = ".\\test_files"
    ext = "txt"
    assert (os.path.isdir(dir)), "Invalid directory"

    root, directories, files = next(os.walk(dir))

    cnt = 1
    for fileName in files:
        if fileName.endswith(ext):
            if fileName.startswith("file"):  # daca fisierul incepe deja cu file
                rest = fileName[4:-4]  # obtinem restul numelui fara "file" si extensie
                if rest.isnumeric() and cnt >= int(rest):  # daca numele este deja in ordinea corecta
                    cnt += 1
                    continue

            full_fileName = os.path.join(root, fileName)
            new_fileName = os.path.join(root, f"file{cnt}.txt")
            while os.path.isfile(new_fileName):  # cat timp exista deja fisiere cu numele nou
                cnt += 1
                new_fileName = os.path.join(root, f"file{cnt}.txt")
            try:
                os.rename(full_fileName, new_fileName)
            except PermissionError as e:
                print(f"You don't have the permission to rename this file: {e.filename}")
            cnt += 1

except FileNotFoundError as e:
    print(f"Unable to find file: {e.filename}")
except Exception as e:
    print(e)
