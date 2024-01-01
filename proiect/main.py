import datetime
import sys
import time
import os
import hashlib

from FTPLocation import FTPLocation
from Location import Location
from ZipLocation import ZipLocation
from datetime import datetime, timedelta

# the timer for rechecking the given locations
DELAY = 5


# used in comparing 2 files
def checksum(text):
    sha256 = hashlib.sha256()
    sha256.update(text)
    return sha256.hexdigest()


def compare_files(file1, file2):
    """
    Compares two given files and modifies them when needed
    """
    # break the content into chunks before comparing them
    block_size = 4
    changed = False
    with open(file1, 'rb') as file:
        data1 = file.read()
    with open(file2, 'rb') as file:
        data2 = file.read()

    blocks1 = [data1[i:i + block_size] for i in range(0, len(data1), block_size)]
    blocks2 = [data2[i:i + block_size] for i in range(0, len(data2), block_size)]

    # only the modified blocks will be overwritten
    with (open(file2, 'rb+') as file):
        for i in range(0, len(blocks1)):
            if i >= len(blocks2) or checksum(blocks1[i]) != checksum(blocks2[i]):
                changed = True
                start = i * block_size
                file.seek(start)
                file.write(blocks1[i])
        # in case of deletions, delete the rest of the modified file
        if len(data1) < len(data2):
            changed = True
            file.truncate(len(data1))

    return changed


def is_changed(t):
    """
    Checks if the date given is within the DELAY window. This will be used to check if a file has been modified since
    the last checking
    """
    current_time = datetime.now()
    diff = current_time - t
    threshold = timedelta(seconds=DELAY)

    return diff <= threshold


def compare_locations(init, loc1, loc2, file1='', file2=''):
    """
    Compares two locations recursively
    Parameters:
        - init (bool): whether this is the first call or not
        - loc1 (Location): First Location object
        - loc2 (Location): Second Location object
        - file1 (str): the name of the current file from the content root of the first location
        - file2 (str): the name of the current file from the content root of the second location
    """
    files1 = loc1.get_list_of_files(file1)
    files2 = loc2.get_list_of_files(file2)

    for file in files1:
        if file not in files2:
            if loc1.is_dir(file1 + "/" + file):
                loc2.create_dir(file2 + "/" + file)
                # compare the contents of directories
                compare_locations(init, loc1, loc2, file1 + "/" + file, file2 + "/" + file)
            else:
                # if a file hasn't been modified since last checking, but it's missing from one location then
                # it has been deleted
                if init is True and is_changed(loc1.get_last_modified(file1 + "/" + file)) is False:
                    loc1.delete_file(file1 + "/" + file)
                else:
                    # if a file has been created in one location it is copied to the other
                    loc2.copy_file(loc1.get_file_path(file1 + "/" + file), file2 + "/" + file)

        else:
            # if both directories are present then check the contents
            if loc1.is_dir(file1 + "/" + file) and loc2.is_dir(file2 + "/" + file):
                compare_locations(init, loc1, loc2, file1 + "/" + file, file2 + "/" + file)
            else:
                time1 = loc1.get_last_modified(file1 + "/" + file)
                time2 = loc2.get_last_modified(file2 + "/" + file)
                # copy from the newer file to the older
                if time1 > time2:
                    if compare_files(loc1.get_file_path(file1 + "/" + file), loc2.get_file_path(file2 + "/" + file)):
                        loc2.save(loc1.get_file_path(file1 + "/" + file), file2 + "/" + file)
                else:
                    if compare_files(loc2.get_file_path(file2 + "/" + file), loc1.get_file_path(file1 + "/" + file)):
                        loc1.save(loc2.get_file_path(file2 + "/" + file), file1 + "/" + file)
    # add files not found in the first location from second location
    for file in files2:
        if file not in files1:
            if loc2.is_dir(file2 + "/" + file):
                loc1.create_dir(file1 + "/" + file)
                compare_locations(init, loc1, loc2, file1 + "/" + file, file2 + "/" + file)
            else:
                if init is True and is_changed(loc2.get_last_modified(file2 + "/" + file)) is False:
                    loc2.delete_file(file2 + "/" + file)
                else:
                    loc1.copy_file(loc2.get_file_path(file2 + "/" + file), file1 + "/" + file)


def type_and_location(text):
    """
    Find components of the arguments
    """
    poz = text.find(':')
    return text[0:poz], text[poz + 1:]


def get_file(type, path, id):
    if type == "ftp":
        return FTPLocation(path, id)
    if type == "zip":
        return ZipLocation(path, id)
    return Location(path)


def check_locations(init, text1, text2):
    """
    Parses the arguments, creates the Location objects and compares them
    """
    type1, loc1 = type_and_location(text1)
    type2, loc2 = type_and_location(text2)
    file1 = get_file(type1, loc1, 1)
    file2 = get_file(type2, loc2, 2)
    compare_locations(init, file1, file2)
    file1.save_all()
    file2.save_all()
    file1.clear()
    file2.clear()


try:
    assert len(sys.argv) == 3, f"Invalid number of arguments, expected 3, got{len(sys.argv)}"
    check_locations(False, sys.argv[1], sys.argv[2])
    while True:
        time.sleep(DELAY)
        check_locations(True, sys.argv[1], sys.argv[2])
except Exception as e:
    print(e)
