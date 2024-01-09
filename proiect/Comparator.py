import datetime
import hashlib
from datetime import datetime
from ftplib import error_perm

from FTPLocation import FTPLocation
from Location import Location
from ZipLocation import ZipLocation


class Comparator:

    def __init__(self, text1, text2):
        """
        Initializes a Comparator object.

        Parameters:
        - text1 (str): A string of format type:location
        - text2 (str): A string of format type:location
        """

        self.type1, self.loc1 = type_and_location(text1)
        self.type2, self.loc2 = type_and_location(text2)
        # these will be used to check if a file was present last time the location has been checked
        self.last_files1 = []
        self.last_files2 = []
        # stores the time of the last checking
        self.last_timestamp = None

    def run(self, init):
        """
        Starting point for comparing two locations
        Parameters:
            - init (bool): whether this is the first call or not

        """
        done = False
        # retrying to compare if the files have been deleted during synchronization
        while done is False:
            try:
                self.compare(init)
                done = True
            except error_perm as e:
                print(f"FTP Permission Error: {e}\nThe file might have changed during synchronization. Retrying...")
            except FileNotFoundError as e:
                print(f"File Not Found Error: {e}\nThe file might have changed during synchronization. Retrying...")

    def compare(self, init):
        """
        Prepares the necessary before comparing two locations
        Parameters:
            - init (bool): whether this is the first call or not
        """
        self.last_timestamp = datetime.now()
        file1 = get_file(self.type1, self.loc1, 1)
        file2 = get_file(self.type2, self.loc2, 2)
        last_added1 = []
        last_added2 = []
        self.compare_locations(init, file1, file2, last_added1, last_added2)
        self.last_files1 = last_added1.copy()
        self.last_files2 = last_added2.copy()
        file1.save_all()
        file2.save_all()
        file1.clear()
        file2.clear()

    def is_changed(self, t):
        """
        Checks if a file has been modified since the last checking
        """
        return t > self.last_timestamp

    def compare_locations(self, init, loc1, loc2, last_added1, last_added2, parent=''):
        """
        Compares two locations recursively
        Parameters:
            - init (bool): whether this is the first call or not
            - loc1 (Location): First Location object
            - loc2 (Location): Second Location object
            - file1 (str): the name of the current file from the content root of the first location
            - file2 (str): the name of the current file from the content root of the second location
        """
        files1 = loc1.get_list_of_files(parent)
        files2 = loc2.get_list_of_files(parent)
        print("Found files:\n", files1, files2)
        for file in files1:
            # full path to the content root
            file_path = parent + "/" + file
            last_added1.append(file_path)
            if file not in files2:
                # if a file hasn't been modified since last checking, but it's missing from one location then
                # it has been deleted
                if init is True and file_path in self.last_files2:
                    loc1.delete_file(file_path)
                else:
                    # if a new file is found in one location, it is copied to the other
                    if loc1.is_dir(file_path):
                        loc2.create_dir(file_path)
                        last_added2.append(file_path)
                        # compare the contents of directories
                        self.compare_locations(init, loc1, loc2, last_added1, last_added2, file_path)
                    else:
                        loc2.copy_file(loc1.get_file_path(file_path), file_path)
                        # add the new file in the future list of files for the second location
                        last_added2.append(file_path)

            else:
                # if both directories are present then check the contents
                if loc1.is_dir(file_path) and loc2.is_dir(file_path):
                    self.compare_locations(init, loc1, loc2, last_added1, last_added2, file_path)
                else:
                    time1 = loc1.get_last_modified(file_path)
                    time2 = loc2.get_last_modified(file_path)
                    # copy from the newer file to the older
                    if time1 > time2:
                        if compare_files(loc1.get_file_path(file_path),
                                         loc2.get_file_path(file_path)):
                            loc2.save(loc1.get_file_path(file_path), file_path)
                    else:
                        if compare_files(loc2.get_file_path(file_path),
                                         loc1.get_file_path(file_path)):
                            loc1.save(loc2.get_file_path(file_path), file_path)
        # add files not found in the first location from second location
        for file in files2:
            file_path = parent + "/" + file
            last_added2.append(file_path)
            if file not in files1:
                if init is True and file_path in self.last_files1:
                    loc2.delete_file(file_path)
                else:
                    if loc2.is_dir(file_path):
                        loc1.create_dir(file_path)
                        last_added1.append(file_path)
                        self.compare_locations(init, loc1, loc2, last_added1, last_added2, file_path)
                    else:
                        loc1.copy_file(loc2.get_file_path(file_path), file_path)
                        # add the new file in the future list of files for the first location
                        last_added1.append(file_path)


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


def type_and_location(text):
    """
    Find components of the arguments
    """
    poz = text.find(':')
    return text[0:poz], text[poz + 1:]


def get_file(kind, path, n):
    if kind == "ftp":
        return FTPLocation(path, n)
    if kind == "zip":
        return ZipLocation(path, n)
    return Location(path)
