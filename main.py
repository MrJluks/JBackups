import os
import shutil
import getpass
import ast
import dearpygui.dearpygui as dpg
from jluksfiles import *
from Jlukscfg import *

# JBACKUPS by MrJluk
# V1.0.1

username = getpass.getuser()
JJFile = Jfile("D:\\storage\BACKUPS\\JBACKUPS\\cfg")
Jcfg= JJcfg(JJFile.path_to_dir)


def save_backup_dir():
    Jcfg.save_value(dpg.get_value("backup_input"),"data","backup_dir")

def add_path():
    path = dpg.get_value("Path Input")
    
    path_list_str = Jcfg.config.get("data", "path_list", fallback="")
    
    # преобразование строки в список ast.literal_eval
    path_list = ast.literal_eval(path_list_str) if path_list_str else []


    if path:
        path_list.append(path)

        Jcfg.config.set("data", "path_list", str(path_list))

        Jcfg.save_cfg()

        dpg.configure_item("path_list", items=path_list)
        dpg.set_value("Path Input", "")

    else:
        print("invalid path")

def remove_path():

    selected_item = dpg.get_value("path_list")
    
    if selected_item:
          # получение или создания списка директорий    
            path_list_str = Jcfg.config.get("data", "path_list", fallback="")
            
            # преобразование строки в список ast.literal_eval
            path_list = ast.literal_eval(path_list_str) if path_list_str else []  

            if selected_item in path_list:
                path_list.remove(selected_item)
                Jcfg.config.set("data", "path_list", str(path_list))
                print(str(path_list),"--------654+---------")
                Jcfg.save_cfg

                dpg.configure_item("path_list", items=path_list)
                #dpg.set_value("directory_input", "")

            else:
                print("can't find path")
    else:
        print("sd")

def update_data():
    path_list_str = Jcfg.config.get("data", "path_list", fallback="")
    
    # преобразование строки в список ast.literal_eval
    path_list = ast.literal_eval(path_list_str) if path_list_str else []

    backup_dir = Jcfg.get_value("data","backup_dir")

    dpg.configure_item("path_list", items=path_list)
    dpg.set_value(item="backup_input", value=backup_dir)


def copy_files():
    dest_folder = Jcfg.get_value("data", "backup_dir")
    path_list_str = Jcfg.config.get("data", "path_list", fallback="")
    path_list = ast.literal_eval(path_list_str) if path_list_str else []

    total_paths = len(path_list)

    for index, source_path in enumerate(path_list, start=1):
        source_path = source_path.strip()

        if source_path and os.path.exists(source_path):
            if os.path.isdir(source_path):
                source_dir_name = os.path.basename(source_path)
                dest_dir = os.path.join(dest_folder, source_dir_name)


                try:
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    dpg.set_value("progress_c",f"copying from {source_path}")
                    shutil.copytree(source_path, dest_dir, dirs_exist_ok=True)

                    print(f"Copied from {source_path} to {dest_dir}")
                    dpg.set_value("progress_c",f"Copied from {source_path} success")
                    
                except Exception as e:
                    print(f"Error copying {source_path}: {e}")
                    dpg.set_value("progress_c",f"Error copying {source_path}: {e}")
            else:
                print(f"Skipping {source_path} as it's not a directory")
                dpg.set_value("progress_c",f"Skipping {source_path} as it's not a directory")
        else:
            print(f"Source path {source_path} does not exist or is empty")
            dpg.set_value("progress_c",f"Source path {source_path} does not exist or is empty")

        

        dpg.set_value("progress_b", index / total_paths)

    print("All files copied")
    dpg.set_value("progress_c","All files copied!")




def restore_files():
    dest_folder = Jcfg.get_value("data", "backup_dir")
    path_list_str = Jcfg.config.get("data", "path_list", fallback="")
    path_list = ast.literal_eval(path_list_str) if path_list_str else []

    total_paths = len(path_list)

    for index, source_dir_name in enumerate(path_list, start=1):

        print(source_dir_name,"------987")

        source_dir_name = source_dir_name.strip()

        if source_dir_name:

            dest_dir = os.path.join(os.getcwd(), source_dir_name)

            try:

                source_dir_path = os.path.join(dest_folder, os.path.basename(dest_dir))

                print(source_dir_path)

                dpg.set_value("progress_c",f"Copying to {dest_dir}") 
                shutil.copytree(source_dir_path, dest_dir)

                print(f"Restored from {source_dir_path} to {dest_dir}")
                dpg.set_value("progress_c",f"Restored from {source_dir_path} to {dest_dir}")
            except Exception as e:
                print(f"Error restoring to {dest_dir}: {e}")
                dpg.set_value("progress_c",f"Error restoring to {dest_dir}: {e}")
        else:
            print("Skipping empty path")

        dpg.set_value("progress_b", index / total_paths)

    print("All files restored")
    dpg.set_value("progress_c","All files restored")

dpg.create_context()
with dpg.window(tag="window"):
    dpg.add_button(label = "copy files",callback=copy_files)
    dpg.add_button(label = "paste files",callback=restore_files)
    dpg.add_text("messange here",tag="progress_c")
    dpg.add_progress_bar(tag="progress_b",default_value=0)

    dpg.add_separator()

    dpg.add_text(default_value="",tag = "text_log")
    with dpg.group(horizontal=True):
        dpg.add_button(label = "add path", callback=add_path)
        dpg.add_button(label = "delete path", callback=remove_path)
    dpg.add_input_text(tag="Path Input")
    dpg.add_listbox(tag="path_list",items=[],num_items=10)
    dpg.add_separator()
    dpg.add_input_text(label="dir to backup folder",tag="backup_input",callback=save_backup_dir)
    
        
update_data()


dpg.create_viewport(title = "Jluk's backups 1.0.1", width=670, height=455)
dpg.set_primary_window("window",True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


