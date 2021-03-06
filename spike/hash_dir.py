import os,time
import hashlib

def dfs_dir(path):
    content = os.listdir(path)
    dir_hash = "+"
    dir_hash += str(os.path.getmtime(path))
    for a in content:
        dir_hash += '-'
        if(os.path.isdir(os.path.join(path,a))):
            val = dfs_dir(os.path.join(path,a))
            dir_hash += val
        elif(os.path.isfile(os.path.join(path,a))):
            dir_hash += str(os.path.getmtime(os.path.join(path,a)))
    return dir_hash


def get_hash(path):
    dir_hash = dfs_dir(path)
    return hashlib.sha1(dir_hash.encode('utf-8')).hexdigest()


if __name__ == "__main__":
    path = './srb_test'
    import sys
    if(len(sys.argv)==2):
        path = sys.argv[1]
    dir_hash = get_hash(path)
    print(dir_hash)
