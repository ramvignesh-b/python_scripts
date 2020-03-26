import os
import shutil
import copy

r = []
src = r"C:\Users\ramvi\Downloads\Test"
general = r"E:\General"
video = r"E:\Videos"
program = r"E:\Programs"
document = r"E:\\Documents"
picture = r"E:\\Pictures"


def move(fname, file):
    if not os.path.exists(file):
        r.append(shutil.copy(fname, file))
        print("Successfully moved [%s]!" % file)
    else:
        print("[%s] already exists!" % file)


file_list = os.listdir(src)
for file in file_list:
    if file.endswith(".mkv") or file.endswith(".mp4"):
        move(src + "\\" + file, video + "\\" + file)
    elif file.endswith(".txt") or file.endswith(".docx") or file.endswith(".pdf") or file.endswith(".pptx") or \
            file.endswith(".xls") or file.endswith(".indd"):
        move(src + "\\" + file, document + "\\" + file)
    elif file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png") or file.endswith(".psd") or \
            file.endswith(".svg"):
        move(src + "\\" + file, picture + "\\" + file)
    elif file.endswith(".exe") or file.endswith(".msi"):
        move(src + "\\" + file, program + "\\" + file)
    else:
        move(src + "\\" + file, general + "\\" + file)
