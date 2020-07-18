import os
rootDir = "/Users/rahuls-mac/Desktop/Devops_Project/"

#Print tree strcuture for the files and subdirectories under root directory
for dirname, subdirlist, filelist in os.walk(rootDir):
    print("Found Directory: %s" % dirname)
    for fname in filelist:
        print("\t%s" %fname)


#print absolute path for each file in the dir and subdirs
for root, dirs, fnames in os.walk(rootDir):
    for dir in dirs:
        print(os.path.join(root,dir))
    for fname in fnames:
        print(os.path.join(root, fname))


#Print list of all empty directories
empty = []
for root, dirs, files in os.walk(rootDir):
    if not len(dirs) and not len(files):
        empty.append(root)
for value in empty:
    print("Empty Dirs: {}".format(value))


#Check if dir is empty
dir = os.listdir(rootDir)
if not len(dir):
    print("Empty")
else:
    print("Not Empty")
