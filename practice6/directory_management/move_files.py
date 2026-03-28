import os
import shutil
from pathlib import Path

os.makedirs("source", exist_ok=True)
os.makedirs("destination", exist_ok=True)

f = open("source/demofile.txt", "w")
f.write("Hello World!")
f.close()

f = open("source/demofile2.txt", "w")
f.write("Hello again!")
f.close()

shutil.move("source/demofile.txt", "destination/demofile.txt")
print(os.listdir("destination"))

for file in Path("source").glob("*.txt"):
    shutil.copy(file, "destination/" + file.name)
print(os.listdir("destination"))

shutil.copytree("source", "source_backup")
print(os.listdir("source_backup"))

shutil.rmtree("source")
shutil.rmtree("destination")
shutil.rmtree("source_backup")
