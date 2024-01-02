import os
import shutil
from datetime import datetime


class Location:
    def __init__(self, path):
        self.path = path

    def get_last_modified(self, file):
        modify_time = os.path.getmtime(self.path + "/" + file)
        modify_date = datetime.fromtimestamp(modify_time)
        return modify_date

    def get_list_of_files(self, location=""):
        """
        Get a list of files within the given location
        """
        filenames = os.listdir(self.path + "/" + location)
        return filenames

    def is_dir(self, file):
        """
        Checks if a file is a directory
        """
        return os.path.isdir(self.path + file)

    def create_dir(self, file):
        """
        Creates a directory
        """
        os.makedirs(self.path + "/" + file, exist_ok=True)

    def copy_file(self, src, dest):
        """
        Copies a file from source to destination
        """
        shutil.copy(src, self.path + "/" + dest)

    def delete_file(self, file):
        """
        Deletes the given file or directory including its contents
        """
        try:
            if self.is_dir(file):
                shutil.rmtree(self.path + file)
            else:
                os.remove(self.path + file)
        except FileNotFoundError:
            print(f"File '{file}' not found.")
        except PermissionError:
            print(f"Permission error while trying to delete '{file}'.")
        except Exception as e:
            print(f"An error occurred while deleting '{file}': {e}")

    def get_file_path(self, file):
        """
        Returns the path to the file
        """
        return self.path + "/" + file

    def save(self, src, dest):
        pass

    def save_all(self):
        pass

    def clear(self):
        pass
