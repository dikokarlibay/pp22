
import os
from pathlib import Path

print(os.getcwd())

os.mkdir("mydir")

os.makedirs("mydir/sub/deep", exist_ok=True)

f = open("mydir/file1.txt", "w")
f.write("Hello")
f.close()

f = open("mydir/file2.txt", "w")
f.write("World")
f.close()

print(os.listdir("mydir"))

for file in Path("mydir").glob("*.txt"):
    print(file.name)

os.chdir("mydir")
print(os.getcwd())
os.chdir("..")

os.rmdir("mydir/sub/deep")
os.rmdir("mydir/sub")

import shutil
shutil.rmtree("mydir")
