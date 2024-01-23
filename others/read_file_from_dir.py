import os

root_dir = "C:/Users/SurajVerma/Desktop/datablaze/db-common/src/main/java/com/rawcubes/datablaze/common"


def find_java_files(directory):
    print("hi")
    for root, dirs, files in os.walk(directory):
        print(root)
        for file in files:
            print(f" {file}")


find_java_files(root_dir)
