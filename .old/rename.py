import glob
import os


def remove_string_from_file_name(file_path, string_to_remove, dry_run=False):
    path, file_name = os.path.split(file_path)
    new_name = file_name.replace(string_to_remove, '')
    new_path = os.path.join(path, new_name)
    if dry_run:
        print("Would rename {} to {}".format(file_path, new_path))
    else:
        os.rename(file_path, new_path)


def get_file_paths_with_a_string(dir_path, string_to_find):
    return glob.glob(
        os.path.join(dir_path, "*{}*".format(string_to_find))
    )

if __name__ == "__main__":
    string_to_remove = '_jpg'
    # current_dir = os.getcwd()
    current_dir = '/mnt/c/Users/Alexander Hunt/data/test/'
    file_paths = get_file_paths_with_a_string(current_dir, string_to_remove)
    for file_path in file_paths:
        remove_string_from_file_name(file_path, string_to_remove, dry_run=False)