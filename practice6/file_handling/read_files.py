f = open("demofile.txt", "w")
f.write("Hello! Welcome to demofile.txt\nThis file is for testing.\nGood Luck!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()

f = open("demofile.txt", "r")
print(f.readline())
f.close()

f = open("demofile.txt", "r")
print(f.readlines())
f.close()

f = open("demofile.txt", "r")
for line in f:
    print(line)
f.close()
