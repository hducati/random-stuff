import os
from winreg import *


def sid_user(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, "SOFWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" + '\\' + sid)
        (value, type) = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user

    except Exception as e:
        print(e)
        return sid


def return_dir():
    # lista contendo o caminho da lixeira dos SO's
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
    for recycle_dir in dirs:
        if os.path.isdir(recycle_dir):
            return recycle_dir
    return None


def find_recycled(recycle_dir):
    dir_list = os.listdir(recycle_dir)

    for sid in dir_list:
        files = os.listdir(recycle_dir + sid)
        user = sid_user(sid)
        print('[*] Files for users: ' + str(user))

        for file in files:
            print('[+] Found file: ' + str(file))


def main():
    recycled_dir = return_dir()
    find_recycled(recycled_dir)


if __name__ == '__main__':
    main()
