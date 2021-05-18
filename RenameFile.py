import os
import os.path

#Get path from current directory and print
directory_path = os.getcwd()
print("My current directory is : " + directory_path)
folder_name = os.path.basename(directory_path)


#List all the files in the directory and print
directory_files=os.listdir(directory_path)
print(directory_files)
#Let the user know the files have been renamed and what directory they are under
print("All your files have been renamed under your current directory: " + folder_name)

#rename all the files in the directory
for path in directory_files:
    full_path = os.path.join(directory_path, path)
    if os.path.isfile(full_path):
        new_path = os.path.join(directory_path, "new_" + path)
        os.rename(full_path, new_path)
