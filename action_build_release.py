import os

def main(**kwargs):
    #update repos
    repos = []
    repo = {
            "url": "github.com/oomlout/oomlout_bolt_packaging_tin_hinged_lid_version_1"
            }    
    repos.append(repo)
    repo = {
            "url": "github.com/oomlout/oomlout_bolt_packaging_three_d_printed_version_3"
            }
    repos.append(repo)

    #clone all repos into temporary directory
    for repo in repos:
        url = repo["url"]
        #add https if not there
        if not url.startswith("https://"):
            url = f"https://{url}"
        repo_dir = url.split("/")[-1]
        repo_dir = f"temporary\\{repo_dir}"
        if not os.path.exists(repo_dir):            
            os.system(f"git clone {url}.git {repo_dir}")
        else:
            os.system(f"cd {repo_dir} && git pull")

    #   copy the files to release directory
    files_to_copy = []
    ## hinged version
    file = {
            "source": "oomlout_bolt_packaging_tin_hinged_lid_version_1\\scad_output\\oobb_test_main_spacer_08_10_01_ex_width_start_129_height_start_169_depth_start_19\\3dpr.stl",
            "destination": "release\\three_d_printer_files\\hinged_tin_version\\tin_spacer_quantity_2.stl"
            }
    files_to_copy.append(file)
    file = {
            "source": "\oomlout_bolt_packaging_three_d_printed_version_3\\scad_output\\oobb_oomlout_bolt_packaging_three_d_printed_version_1_tray_04_2d5_18\\3dpr.stl",
            "destination": "release\\three_d_printer_files\\hinged_tin_version\\tray_oobb_4_width_2-5_length_18_mm_depth_quantity_8.stl"
            }
    files_to_copy.append(file)

    ## three d printed version
    file = {
            "source": "oomlout_bolt_packaging_three_d_printed_version_3\\scad_output\\oobb_oomlout_bolt_packaging_three_d_printed_version_1_main_body_10_08_18\\3dpr.stl",
            "destination": "release\\three_d_printer_files\\three_d_printed_version\\case_bottom_quantity_1.stl"
            }
    files_to_copy.append(file)


    file = {
            "source": "oomlout_bolt_packaging_three_d_printed_version_3\\scad_output\\oobb_oomlout_bolt_packaging_three_d_printed_version_1_lid_10_08_02\\3dpr.stl",
            "destination": "release\\three_d_printer_files\\three_d_printed_version\\case_lid_quantity_1.stl"
            }
    files_to_copy.append(file)
    file = {
            "source": "\oomlout_bolt_packaging_three_d_printed_version_3\\scad_output\\oobb_oomlout_bolt_packaging_three_d_printed_version_1_tray_04_2d5_18\\3dpr.stl",
            "destination": "release\\three_d_printer_files\\three_d_printed_version\\tray_oobb_4_width_2-5_length_18_mm_depth_quantity_8.stl"
            }
    files_to_copy.append(file)


    


    for file in files_to_copy:
        source = file["source"]
        source = f"temporary\\{source}"
        destination = file["destination"]
        #make destination directory
        destination_dir = os.path.dirname(destination)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        #if source exists delete it
        if os.path.exists(destination):
            os.remove(destination)
        command = f"copy {source} {destination}"
        print(f"Copying {source} to {destination}")
        os.system(command)


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)