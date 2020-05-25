import os, shutil, datetime
from pathlib import Path

home_path = str(Path.home())
print(home_path)

path = home_path + "/desktops/"

try:
    os.mkdir(home_path + "/desktops")

except FileExistsError:
    pass

desktop = os.path.expanduser("~/Desktop/")
save_desktop = os.path.expanduser(path )

os.chdir(desktop)
arr = os.listdir(desktop)


for i in arr:
    if "ini" in i:
        continue
    elif "$" in i:
        continue
    print(i)
    src = desktop+i
    print(src)
    dst = save_desktop+i
    print(dst)
    shutil.move(src, dst)

