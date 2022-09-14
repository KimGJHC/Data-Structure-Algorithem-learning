"""
609. Find Duplicate File in System
Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"
"""

from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        valuePath = defaultdict(list)

        for path in paths:
            folders = path.split(' ')
            directory = folders[0]
            files = folders[1:]

            for file in files:
                fileInfo = file.split('(')

                fileName = fileInfo[0]
                fileContent = fileInfo[1][:-1]
                filePath = directory + '/' + fileName
                valuePath[fileContent].append(filePath)

        res = [DuplicateFile for DuplicateFile in valuePath.values() if len(DuplicateFile) > 1]
        return res
# time: O(nm) where n = len(paths) and m = max(length of paths)
# space: O(vfm) where f is number of files and v is number of unique file content