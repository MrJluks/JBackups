import os
import shutil
import urllib.request
import wget
#import subprocess

class Jfile:
    def __init__(self,path_to_dir,):
        self.path_to_dir = path_to_dir
        # self.existing_files = [] TODO

        if not os.path.exists(self.path_to_dir):
            os.makedirs(path_to_dir)
    

    def download_file(self, url, destination):
        try:
            urllib.request.urlretrieve(url, destination)
            print(f"JFILE downloaded file from {url} to {destination}")
            return(["fine",0])
        except Exception as e:
            print(f"JFILE failed to download file from {url}: {e}")
            return(["error",e])


    def download_from_git(self,url,destination):
        try:
            wget.download(url, out=destination)
            print(f"JFILE downloaded {url} to {destination} correctly")
            return(["fine",0])
        except Exception as e:
            print(f"JFILE failed to download file from {url} to {destination}:{e}")
            return(["error",e])


    # def start_process(self,dir_to_exe:str):
    #     subprocess.run(dir_to_exe)
    #     pass


    def delete_file(self,file_path):
        try:
            os.remove(file_path)
            return(["fine",0])
        except Exception as e:
            print(f"JFILE failed to delete file {file_path}: {e}")
            return(["error",e])
    

    def move_file(self,source,destination):
        try:
            shutil.move(source, destination)
            print(f"Moved file from {source} to {destination}")
            return(["fine",0])
        except Exception as e:
            print(f"JFILE failed to move file from {source} to {destination}: {e}")
            return(["error",e])
    

    def delete_dir_content(self, directory:str,mode:bool,rest:bool = True):
        try:
            shutil.rmtree(directory,mode)
            if rest:
                os.makedirs(directory)
            return(["fine",0])
        except Exception as e:
            print(f"JFILE failed to delete content from {directory}: {e}")
            return(["error",e])


    def extract_zip(self, zip_path:str, extract_path:str):
        try:
            shutil.unpack_archive(zip_path, extract_path)
            print(f"Extracted ZIP file from {zip_path} to {extract_path}")
            return(["fine",0])
        except Exception as e:
            print(f"JFILE failed to extract ZIP file from {zip_path} to {extract_path}: {e}")
            return(["error",e])
    

    def create_archive(self, source_folder, target_archive):
        try:
            shutil.make_archive(target_archive, 'zip', source_folder)
            print(f"JFILE created archive from {source_folder} to {target_archive}")
            return ["fine", 0]
        except Exception as e:
            print(f"JFILE failed to create archive: {e}")
            return ["error", e]    

    

        









