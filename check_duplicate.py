import os
import filecmp as fc


# location - the directory you suspect which may have dupilicate file; you can go for an entire drive
# file_name - original file

def search(location, file_name):
    dupilicate_locations = []
    for root, _, files in os.walk(location):
        for file in files:
            compare_path=os.path.join(root, file)
            if fc.cmp(file_name, compare_path):
                dupilicate_locations.append(compare_path)

        original_file = os.path.join(root,file_name)
        if original_file in dupilicate_locations:
            dupilicate_locations.remove(original_file)

    return dupilicate_locations
