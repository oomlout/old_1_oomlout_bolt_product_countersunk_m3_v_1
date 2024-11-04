import oomp
import copy

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    
    parts = []
    
    # base
    if True:
        part_details = {}
        part_details["classification"] = "project"
        part_details["type"] = "github"
        part_details["size"] = "oomlout"
        part_details["color"] = "oomlout_bolt_product_prototyping_tin_hardware_screw_countersunk_m3_black_hex_head_version_1"
        
        part_base = copy.deepcopy(part_details)
        
        part_details = copy.deepcopy(part_base)
        part_details["description_main"] = "base"
        part_details["description_extra"] = ""
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        parts.append(part_details)



    oomp.add_parts(parts, **kwargs)


    
    