import os

path = str(input("""Enter the catalog tree to create
(example: "D:\\temp\\year\\2021\\Sept\\02"):\n"""))


def create_nested_catalog(path_as_string):
    """
    Takes path as string, turns it to list of folders and recursively creates catalog tree.
    :param path_as_string: directories catalog profile
    :type path_as_string: str
    :return: True if created, False if not created
    """
    path_as_list = path_as_string.replace("\"", "").replace("\\", "/").split("/")
    if path_as_list[0].endswith(":"):
        path_as_list[0] = path_as_list[0] + "\\"

    next_nested_folder = ''
    for folder in path_as_list:
        next_nested_folder = os.path.join(next_nested_folder, folder)
        if os.path.exists(next_nested_folder):
            if os.path.isdir(next_nested_folder):
                print(f"Creation of the directory skipped: \"{next_nested_folder}\" already exists")
            else:
                print("Invalid input")
                return False
        else:
            try:
                os.mkdir(next_nested_folder)
            except OSError:
                print(f"Creation of the directory \"{next_nested_folder}\" failed")
                return False
            print(f"\"{next_nested_folder}\" created")
    return True


if __name__ == "__main__":
    create_nested_catalog(path)
