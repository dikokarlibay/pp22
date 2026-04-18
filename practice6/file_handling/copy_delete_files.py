
import os
import shutil
from pathlib import Path

f = open("demofile.txt", "w")
f.write("Hello World!")
f.close()

shutil.copy("demofile.txt", "demofile_backup.txt")

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("File deleted")
else:
    print("The file does not exist")

os.mkdir("myfolder")
os.rmdir("myfolder")
print("Folder deleted")

os.remove("demofile_backup.txt")
