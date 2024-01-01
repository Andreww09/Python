import os
import shutil
import zipfile
from datetime import datetime

from Location import Location


class ZipLocation(Location):
    """
    Class representing a ZIP file location with additional functionality for file operations.
    """

    def __init__(self, path, id):
        """
         Initializes a ZipLocation object.

         Parameters:
         - path (str): The path to the ZIP file.
         - id (int): an identifier for the temporary intermediate location
         """
        # will store information about the files
        self.info = None
        # will store the name of the files as keys and whether they are directories as values
        self.changed = {}
        # will store the name of all deleted files
        self.deleted = set()

        current_directory = os.getcwd()
        full_path = os.path.join(current_directory, f"temp{id}")
        # deletes and recreates the temporary folder that will contain the extracted zip

        self.local_path = full_path
        self.clear()
        os.mkdir(full_path)
        super().__init__(path)
        self.extract()

    def extract(self):
        """
        Extracts the contents of the ZIP file to the local directory.
        """
        with zipfile.ZipFile(self.path, 'r') as zip_ref:
            self.info = zip_ref.infolist()
            zip_ref.extractall(self.local_path)

    def save_all(self):
        """
        Saves changes made to the files and directories back to the original ZIP file.
        """
        temp_zip = 'temp_zip.zip'

        with (zipfile.ZipFile(self.path, 'r') as zip):
            # Create a new in-memory zip file
            with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_DEFLATED) as new_zip:
                for item in zip.infolist():
                    # Copy existing items to the new zip file
                    name = '/' + item.filename
                    if name not in self.changed.keys() and name not in self.deleted:
                        data = zip.read(item.filename)
                        new_zip.writestr(item, data)

                for file_name, is_directory in self.changed.items():
                    file_name = file_name[1:]
                    if is_directory:
                        new_zip.writestr(file_name + '/', b'')
                    else:
                        with open(self.local_path + '/' + file_name, "rb") as file:
                            data = file.read()
                            new_zip.writestr(file_name, data)

        # Replace the original zip file with the updated one
        os.replace(temp_zip, self.path)

    def save(self, src, dest):
        """
        Marks the file as changed so that the original zip will update the file

        Parameters:
            - src (str): The path to the file to be saved.
            - dest (str): the name of the file from the content root
        """
        self.changed[dest] = False

    def get_last_modified(self, file):
        """
        Get the last modification time of a file within the ZIP location.

        Parameters:
        - file (str): The name of the file from content root.

        Returns:
        - datetime: A datetime object representing the last modification time of the specified file.

        Raises:
        - FileNotFoundError: If the specified file is not found within location.

        """
        file = file[1:]
        for file_info in self.info:
            if file_info.filename == file:
                modify_time = file_info.date_time
        modify_date = datetime(*modify_time)
        return modify_date

    def get_list_of_files(self, location=""):
        """
        Get a list of files within the given location
        """
        filenames = os.listdir(self.local_path + "/" + location)
        return filenames

    def is_dir(self, file):
        """
        Checks if a file is a directory
        """
        return os.path.isdir(self.local_path + "/" + file)

    def create_dir(self, file):
        """
        Creates a directory
        """
        os.makedirs(self.local_path + "/" + file, exist_ok=True)
        self.changed[file] = True

    def copy_file(self, src, dest):
        """
        Copies a file from source to destination
        """
        shutil.copy(src, self.local_path + "/" + dest)
        self.changed[dest] = False

    def delete_file(self, file):
        """
        Deletes the given file
        """
        self.deleted.add(file)

    def get_file_path(self, file):
        """
        Returns the path to the temporary intermediate location
        """
        return self.local_path + "/" + file

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

