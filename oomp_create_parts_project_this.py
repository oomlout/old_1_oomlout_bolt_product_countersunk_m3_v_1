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
        part_details["description_main"] = ""
        part_details["description_extra"] = ""        
        part_details["manufacturer"] = ""
        part_details["part_number"] = ""
        

        part_base = copy.deepcopy(part_details)
        
        # label
        if True:
            part_details = copy.deepcopy(part_base)
            part_details["description_main"] = "label"
            part_details["description_extra"] = "working_label_front_print"
            part_details["name_short"] = "m3_countersunk_tin_label_front"
            parts.append(part_details)

            part_details = copy.deepcopy(part_base)
            part_details["description_main"] = "label"
            part_details["description_extra"] = "working_label_inside_print"
            part_details["name_short"] = "m3_countersunk_tin_label_inside"
            parts.append(part_details)


            part_details = copy.deepcopy(part_base)
            part_details["description_main"] = "label"
            part_details["description_extra"] = "working_label_serial_number_print"
            part_details["name_short"] = "m3_countersunk_tin_label_serial_number"
            parts.append(part_details)

        #three d print
        if True:
            part_details = copy.deepcopy(part_base)
            part_details["description_main"] = "three_d_print"
            part_details["description_extra"] = "tin_spacer_t4066"
            part_details["name_short"] = "prototyping_tin_spacer_t4066"

            parts.append(part_details)

            part_details = copy.deepcopy(part_base)
            part_details["description_main"] = "three_d_print"
            part_details["description_extra"] = "tray_4_width_2.5_height_18_mm_depth"
            part_details["name_short"] = "prototyping_tin_tray_4_width_2.5_height_18_mm_depth"
            parts.append(part_details)

            



    oomp.add_parts(parts, **kwargs)


    
    