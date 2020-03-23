# Problem #17 [Hard]
# Suppose we represent our file system by a string in the following manner:
#
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
#
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
#
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
# second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing
# a file file2.ext.
#
# We are interested in finding the longest (number of characters) absolute path to a file within our file system.
# For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
# and its length is 32 (not including the double quotes).
#
# Given a string representing the file system in the above format, return the length of the longest absolute path to a
# file in the abstracted file system. If there is no file in the system, return 0.
#
# Note:
#
# The name of a file contains at least a period and an extension.
# The name of a directory or sub-directory will not contain a period.


# decided to do classes for directories and files, thought that like this would be harder
# a directory can have subdirectories and files, it also has a name
class Directory:
    def __init__(self, name):
        self.sub = list()
        self.files = list()
        self.name = name

class File:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension

# a file system that has always at least a root directory
class FileSystem:
    def __init__(self):
        self.root = Directory("dir")

    # create all the directory/file tree
    def initializeDirectories(self, directoriesString):
        # split on \n to get all folders/files
        path = directoriesString.split("\n")

        def createFileSystem(pathStrings, root):
            for i in range(len(pathStrings)):
                path = pathStrings[i]
                # if it is a folder
                if "\t" not in path[1:] and "." not in path:
                    newDirectory = Directory(path[1:])
                    root.sub.append(newDirectory)
                    subFolder = list()
                    # get the only the folders inside the actual folder
                    for j in range(i+1, len(pathStrings)):
                        subpath = pathStrings[j]
                        if "\t" not in subpath[1:]:
                            break
                        if "\t" in subpath[1:]:
                            subFolder.append(subpath[1:])
                    # and create them
                    createFileSystem(subFolder, newDirectory)
                # if it is a file
                if "\t" not in path[1:] and "." in path:
                    fileName = path[1:].split(".")
                    newFile = File(fileName[0], fileName[1])
                    root.files.append(newFile)

        createFileSystem(path[1:], self.root)

    # I get the whole path, not only count
    def longestAbsolutePath(self, root=None):
        if root is None:
            root = self.root
        path = root.name
        longestPath = ""
        longestFile = ""
        # i look for all the files inside the directory
        for file in root.files:
            # try to get the longest file name, since they all are in the same folder
            if len(file.name) + len(file.extension) + 1 > len(longestFile):
                longestFile = file.name + "." + file.extension
        else:
            # take the longest file name and add to the path, check if it is the longest path
            subfile = path + "/" + longestFile
            if len(subfile) > len(longestPath) and len(longestFile) >= 1:
                longestPath = subfile
        # go on all directories
        for dir in root.sub:
            subpath = root.name
            # get the longest path inside this directory
            subpath += "/" + self.longestAbsolutePath(dir)
            # see if this folder path is the longest path
            if len(subpath) > len(longestPath):
                longestPath = subpath
        return longestPath

fileSystem = FileSystem()
fileSystem.initializeDirectories("dir\n\tsubdir1\n\t\tf.ext\n\tsubdir2\n\t\tfile.ext")
longFile = fileSystem.longestAbsolutePath()
print(longFile, len(longFile))

fileSystem = FileSystem()
fileSystem.initializeDirectories("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
longFile = fileSystem.longestAbsolutePath()
print(longFile, len(longFile))

# cool problem, but today was a really different day, didnt had the time to sit and do it from beginning to end,
# had to stop multiple times and that made my progress much slower, wil try to finish it tomorrow before getting the
# next problem.
# Today I finished the longestAbsolutePath function, it took me today around 20 30 minutes, separating file and folder
# make it harder to get the path. I cant estimate with precision how long i work on it yesterday, maybe around 2 hours,
# but less than 1 hour was actual work
