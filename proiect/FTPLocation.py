import os
from datetime import datetime
from ftplib import FTP
import ftplib
import shutil
import ftputil

from Location import Location


class FTPLocation(Location):
    """
    Class representing an FTP location with additional functionality for file operations.
    """

    def __init__(self, address, id):
        """
        Initializes an FTPLocation object.

        Parameters:
        - address (str): FTP address in the format "user:password@host:port/path".
        - id (int): an identifier for the temporary intermediate location
        """
        try:
            # get the components from the ftp address
            components = FTPLocation.get_components(address)
            assert len(components) == 5, "Invalid ftp address"
            self.user, self.password, self.host, self.port, self.path = components

            # path to the temporary location
            current_directory = os.getcwd()
            full_path = os.path.join(current_directory, f"temp{id}")

            self.local_path = full_path
            # deletes the temporary location if already exists and recreate the folder
            self.clear()
            os.mkdir(full_path)
            super().__init__(self.path)
        except Exception as e:
            print(e)

    @staticmethod
    def get_components(text):
        """
        Extracts components (user, password, host, port, path) from an FTP address.

        Parameters:
        - text (str): FTP address in the format "user:password@host:port/path".

        Returns:
        - list: List of FTP components.
        """
        credentials, location = text.split('@')
        comp = credentials.split(':')
        poz1 = location.find('/')
        address = location[:poz1]
        poz2 = address.rfind(':')

        # add port 0 if missing
        if poz2 == -1:
            comp.append(address)
            comp.append("0")
        else:
            comp.append(address[:poz2])
            comp.append(address[poz2 + 1:])

        comp.append(location[poz1:])
        return comp

    def connect(self):
        """
        Establishes an FTP connection.

        Returns:
        - FTPHost: An FTPHost object representing the FTP connection.
        """
        ftp = ftputil.FTPHost(self.host, self.user, self.password, self.port)
        return ftp

    def retrieve(self, file):
        """
        Retrieves a specific file from the FTP server and saves it locally. A file is only retrieved when needed

        Parameters:
        - file (str): The name of the file to retrieve.
        """
        ftp = self.connect()
        ftp.download(self.path + "/" + file, self.local_path + "/" + file)
        ftp.close()

    def get_last_modified(self, file):
        """
        Get the last modification time of a file within the FTP location.

        Parameters:
        - file (str): The name of the file from the ftp content root

        Returns:
        - datetime: A datetime object representing the last modification time of the specified file.
        """
        ftp = self.connect()
        # time = ftp.sendcmd(f"MDTM {self.path}")
        # modify_date = datetime.strptime(time[4:], "%Y%m%d%H%M%S.%f")
        stat_result = ftp.stat(self.path + "/" + file)
        modify_time = stat_result.st_mtime
        modify_date = datetime.fromtimestamp(modify_time)
        ftp.close()
        return modify_date

    def get_list_of_files(self, location=""):
        ftp = self.connect()
        filenames = ftp.listdir(self.path + "/" + location)
        ftp.close()
        return filenames

    def create_dir(self, file):
        """
        Creates a directory both in the intermediate location and the ftp location
        """
        ftp = self.connect()
        os.makedirs(self.local_path + "/" + file, exist_ok=True)
        ftp.makedirs(self.path + "/" + file)
        ftp.close()

    def copy_file(self, src, dest):
        ftp = self.connect()
        ftp.upload(src, self.path + "/" + dest)
        ftp.close()

    def delete_file(self, file):
        ftp = self.connect()
        try:
            ftp.remove(self.path + '/' + file)
        except Exception as e:
            print(e)
        ftp.close()

    def get_file_path(self, file):
        """
        Returns the path to the temporary intermediate location
        """
        self.retrieve(file)
        return self.local_path + "/" + file

    def is_dir(self, file):
        """
        Checks if a file is a directory. If true the directory will be created at the intermediate location if not
        already present
        """
        ftp = self.connect()
        if ftp.path.isdir(self.path + "/" + file):
            os.makedirs(self.local_path + "/" + file, exist_ok=True)
            ftp.close()
            return True
        ftp.close()
        return False

    def save(self, src, dest):
        """
        Saves the file to the ftp location
        """
        self.copy_file(src, dest)

    def clear(self):
        """
        Deletes the intermediate location
        """
        if os.path.exists(self.local_path):
            try:
                shutil.rmtree(self.local_path)
            except FileNotFoundError:
                print(f"Directory '{self.local_path}' not found.")
            except PermissionError:
                print(f"Permission error while trying to delete directory '{self.local_path}'.")

