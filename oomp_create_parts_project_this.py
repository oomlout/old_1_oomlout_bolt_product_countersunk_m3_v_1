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
            project_name = "oomlout_bolt_product_prototyping_tin_hardware_screw_countersunk_m3_black_hex_head_version_1"
            base_github = f"https://github.com/oomlout/{project_name}/blob/main"
            base_oomlout = f"C:\\gh\\{project_name}"

            part_details = copy.deepcopy(part_base)
            part_details["description_main"] = "label"
            part_details["description_extra"] = "label_front"
            part_details["name_short"] = "m3_countersunk_tin_label_front"

            file_name = "working_label_front_print.pdf"
            directory = "release/print"

            part_details["file_name"] = file_name
            part_details["link_github"] = f"{base_github}/{directory}/{file_name}"
            part_details["file_name_full_oomlout"] = f"{base_oomlout}/{directory}/{file_name}"
            parts.append(part_details)

            part_details = copy.deepcopy(part_base)
            part_details["description_main"] = "label"
            part_details["description_extra"] = "label_inside"
            part_details["name_short"] = "m3_countersunk_tin_label_inside"

            file_name = "working_label_inside_print.pdf"
            directory = directory

            part_details["file_name"] = file_name
            part_details["link_github"] = f"{base_github}/{directory}/{file_name}"
            part_details["file_name_full_oomlout"] = f"{base_oomlout}/{directory}/{file_name}"

            parts.append(part_details)


            part_details = copy.deepcopy(part_base)
            part_details["description_main"] = "label"
            part_details["description_extra"] = "label_serial"
            part_details["name_short"] = "m3_countersunk_tin_label_serial_number"

            parts.append(part_details)

        #three d print
        if True:
            part_details = copy.deepcopy(part_base)
            part_details["description_main"] = "tdpb"
            part_details["description_extra"] = "spacer"
            part_details["name_short"] = "prototyping_tin_spacer_t4066"
            
            file_name = "tin_spacer_quantity_1.stl"
            directory = "release\three_d_printer_files\hinged_tin_version"

            part_details["file_name"] = file_name
            part_details["link_github"] = f"{base_github}/{directory}/{file_name}"
            part_details["file_name_full_oomlout"] = f"{base_oomlout}/{directory}/{file_name}"

            parts.append(part_details)

            part_details = copy.deepcopy(part_base)
            part_details["description_main"] = "tdpb"
            part_details["description_extra"] = "tray42d518"
            part_details["name_short"] = "prototyping_tin_tray_4_width_2.5_height_18_mm_depth"

            file_name = "tray_4_width_2.5_height_18_mm_depth_quantity_4.stl"
            directory = directory

            part_details["file_name"] = file_name
            part_details["link_github"] = f"{base_github}/{directory}/{file_name}"
            part_details["file_name_full_oomlout"] = f"{base_oomlout}/{directory}/{file_name}"

            parts.append(part_details)

            



    oomp.add_parts(parts, **kwargs)


    
    