import os
import urllib.request

DOWNLOAD_URL = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
DWD_DIR_NAME = "dataset"
FILE_NAME = "housing.csv"
DWD_PATH = os.path.join(DWD_DIR_NAME, FILE_NAME)

if not os.path.isdir(DWD_DIR_NAME):
	os.makedirs(DWD_DIR_NAME)
urllib.request.urlretrieve(DOWNLOAD_URL, DWD_PATH)
print("Download Complete...")
