
import importlib
import oomp

part_types = []

def main(**kwargs):
    global part_types

    part_types.append("project_this")

    for type in part_types:    
        importlib.import_module(f'oomp_create_parts_{type}')

    load_parts(**kwargs)

def load_parts(**kwargs):
    global part_types
    print("loading parts from modules")
    filter = kwargs.get('filter', "")
    for type in part_types:
        if filter in type:            
            importlib.import_module(f'oomp_create_parts_{type}').load_parts(**kwargs)


def load_parts_from_yaml(**kwargs):
    print("loading parts from yaml")
    import yaml
    with open("parts.yaml", "r") as infile:
        parts = yaml.load(infile, Loader=yaml.FullLoader)
    oomp.parts = parts

import os

def load_parts_from_pickle(**kwargs):
    print("loading parts from pickle")
    import pickle
    file_pickle = "tmp/parts.pickle"
    if not os.path.exists(file_pickle):
        file_pickle = "c:/gh/oomlout_oomp_part_src/tmp/parts.pickle"
        if not os.path.exists(file_pickle):
            print(f"file {file_pickle} does not exist")
            return
    with open(file_pickle, "rb") as infile:
        parts = pickle.load(infile)
    oomp.parts = parts

def save_parts_to_yaml(**kwargs):
    print("saving parts to yaml")
    import yaml
    with open("parts.yaml", "w") as outfile:
        yaml.dump(oomp.parts, outfile, indent=4)

def save_parts_to_pickle(**kwargs):
    print("saving parts to pickle")
    import pickle
    file_pickle = "tmp/parts.pickle"
    with open(file_pickle, "wb") as outfile:
        pickle.dump(oomp.parts, outfile)

def save_parts_to_individual_yaml_files(**kwargs):
    print("saving parts to yaml")
    import yaml
    for part_id in oomp.parts:
        part = oomp.parts[part_id]
        del part['make_files']
        yaml_file = f"parts_source/{part_id}/working/working.yaml"
        with open(yaml_file, "w") as outfile:
            print(f"writing {yaml_file}")
            yaml.dump(part, outfile, indent=4)


#run if run independantly __main__
if __name__ == "__main__":
    kwargs = {}
    ##from_yaml=False, make_files=True, filter=filter
    kwargs['from_yaml'] = False
    kwargs['make_files'] = "parts_source"
    kwargs['filter'] = ""
    main(**kwargs)
    