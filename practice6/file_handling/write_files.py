f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()

f = open("myfile.txt", "x")
f.write("Created a new file!")
f.close()

f = open("myfile.txt", "r")
print(f.read())
f.close()
