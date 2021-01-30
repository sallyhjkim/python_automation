import os
import sys
import shutil 

LINGODA_FOLDER_NAME = 'Desktop/Lingoda'
DOWNLOAD_DIR = os.path.dirname(os.path.abspath(__file__))
# DOWNLOAD_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(DOWNLOAD_DIR)
LANGUAGE = 'FR' # FOR french
lingda_files = []
lingoda_path =os.path.join(BASE_DIR, LINGODA_FOLDER_NAME)

for item in os.listdir(DOWNLOAD_DIR):
    if not os.path.isfile(os.path.join(DOWNLOAD_DIR, item)):
        continue
    file_src = str(DOWNLOAD_DIR + item)
    if not (file_src.endswith('pdf') and LANGUAGE in file_src):
        continue
    lingda_files.append(item)
    
    
for file_name in lingda_files:
    # e.g) A1_1042X_FR.pdf => Lingoda/A1/1.4/A1_1042X_FR.pdf
    lgd_format = file_name.split('_')
    if len(lgd_format) != 3:
        print('ERROR: invalid file name format!')
        continue
    lv = lgd_format[0]
    chapter = lgd_format[1]
    source_dir = os.path.join(DOWNLOAD_DIR, file_name)
    target_dir = os.path.join(lingoda_path, lv, f'{chapter[0]}.{chapter[2]}')
    os.makedirs(target_dir, exist_ok=True)
    shutil.copy(source_dir, target_dir)
    os.remove(source_dir)
print('Done!')
