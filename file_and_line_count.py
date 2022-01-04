
import os
import mmap

total_files = total_lines = 0

#inder here your lib folder path
dir = "G:/New folder/Spiro-Study-Flutter/lib"

def file_line_count(file_path):
    try:
        f = open(file_path, "r+")
        buf = mmap.mmap(f.fileno(), 0)
        lines = 0
        readline = buf.readline
        while readline():
            lines += 1
        return lines
    except e:
        print('file cant open', file_path, e)
        return 0

for root, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith(".dart"):
             total_files += 1
             temp_path = os.path.join(root, file)
             print(temp_path)

             total_lines += file_line_count(os.path.normpath(temp_path))

print("total file: %s, total lines %s"%(total_files, total_lines))