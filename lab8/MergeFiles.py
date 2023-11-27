def merge(dest, delimiter="\n", *argv):
    """merges all the given files in a new file with a custom delimiter in between

        :param str dest the name of the final file

        :param str delimiter the custom delimiter added after each file, default is \' \\\\n \'

        :param str *argv the names of the files to be merged
    """
    try:
        output = open(dest, "w")
        for name in argv:
            with open(name, "r") as file:
                content = file.read()
                output.write(content)
                output.write(delimiter)
        output.close()
    except:
        raise Exception(f"An error occurred while trying to open file {dest}")
