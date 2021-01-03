import os

cnn = 0
cnnArts = 0
huffpost = 0
hpArts = 0
fox = 0
foxArts = 0
breitbart = 0
bbArts = 0

for filename in os.scandir(r'C:\Users\json1\Documents\Princeton\F2020\IW\src\cnn'):
    f = open(filename, "rb")
    cnn += len(f.read().split())
    cnnArts += 1
for filename in os.scandir(r'C:\Users\json1\Documents\Princeton\F2020\IW\src\huffpost'):
    f = open(filename, "rb")
    huffpost += len(f.read().split())
    hpArts += 1
for filename in os.scandir(r'C:\Users\json1\Documents\Princeton\F2020\IW\src\fox'):
    f = open(filename, "rb")
    fox += len(f.read().split())
    foxArts += 1
for filename in os.scandir(r'C:\Users\json1\Documents\Princeton\F2020\IW\src\breitbart'):
    f = open(filename, "rb")
    breitbart += len(f.read().split())
    bbArts += 1

print("cnn: " + str(cnn) + " words, " + str(cnnArts) + " articles")
print("huffpost: " + str(huffpost) + " words, " + str(hpArts) + " articles")
print("fox: " + str(fox) + " words, " + str(foxArts) + " articles")
print("breitbart: " + str(breitbart) + " words, " + str(bbArts) + " articles")
total = cnn + huffpost + fox + breitbart
print("total: " + str(total))
