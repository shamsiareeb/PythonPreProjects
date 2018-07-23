class FileManager:

    path = ''
    data = ''

    def __init__(self):
        pass

    def read_file(self, path):
        import os
        while True:
            if os.path.exists(path):
                file = open(path, "r")
                readdata = file.read()
                print(readdata)
                file.close()
                break
            else:
                print('Please enter a valid path!')

    def write_file(self, path):
        import os
        if os.path.exists(path):
            file = open(path, "w")
            print('Enter data to be written in file (press (space) to exit)>>')
            while True:
                data = input('>>')
                file.write(data)
                if data == " ":
                    break
            file.close()
        else:
            print('The path you entered does not exists!')
            reply = input('Would you like to create a new file?(reply with "yes" or "no")>>')
            if reply == "yes":
                #os.makedirs(path)
                file = open(path, "w+")
                while True:
                    data = input('>>')
                    file.write(data)
                    if data == " ":
                        break
                file.close()

    def display_file_details(self, path):
        import os
        from datetime import datetime
        os.chdir(path)
        content = os.listdir()
        files = []
        folders = []
        for item in content:
            if os.path.isfile(item):
                files.append(item)
            elif os.path.isdir(item):
                folders.append(item)
            else:
                print(f'{item} is an unknown file or folder')
        print('File Name\t\tAccess Time\t\tCreation Time\t\tSize')
        for item in files:
            accesstime = os.path.getatime(item)
            creationtime = os.path.getctime(item)
            bytes = os.path.getsize(item)
            atime = datetime.fromtimestamp(accesstime).strftime("%d-%m-%y %H:%M:%Y")
            ctime = datetime.fromtimestamp(creationtime).strftime("%d-%m-%y %H:%M:%Y")
            print(f'{item}\t\t{atime}\t\t{ctime}\t\t{bytes} bytes')
            print('-' * 60)
        print('\nFolder Name\t\tAccess Time\t\tCreation Time')
        for item in folders:
            accesstime = os.path.getatime(item)
            creationtime = os.path.getctime(item)
            atime = datetime.fromtimestamp(accesstime).strftime("%d-%m-%y %H:%M:%Y")
            ctime = datetime.fromtimestamp(creationtime).strftime("%d-%m-%y %H:%M:%Y")
            print(f'{item}\t\t{atime}\t\t{ctime}')
            print('-' * 90)

    def remove_file(self, path):
        import os
        if os.path.exists(path):
            print('Are you sure?')
            rep = input('Reply with "yes" or "no">> ')
            if rep == "yes":
                os.unlink(path)
        else:
            print('No file to delete!')

    def remove_folder(self, path):
        import os
        import shutil
        if os.path.exists(path):
            print('Are you sure?')
            rep = input('Reply with "yes" or "no">> ')
            if rep == "yes":
                shutil.rmtree(path)
        else:
            print('No folder to delete!')

    def copy_folder(self, src, dest):
        import os
        import shutil
        if not os.path.exists(src):
            print("no folder to copy")
        else:
            if os.path.exists(dest):
                print("Sorry, folder already exists")
            else:
                out = shutil.copytree(src, dest)
                print(f'successfully copied to {out}')

    def move_folder(self, src, dest):
        import os
        import shutil
        if not os.path.exists(src):
            print("no folder to move")
        else:
            if os.path.exists(dest):
                print("Sorry, folder already exists")
            else:
                out = shutil.copytree(src, dest)
                shutil.rmtree(src)
                print(f'successfully moved to {out}')

    def rename_folder(self, old, new):
        import os
        if not os.path.exists(old):
            print("no folder to rename")
        else:
            if os.path.exists(new):
                print("Sorry, folder name already taken")
            else:
                os.rename(old, new)
                print('Folder renamed successfully!')


    def working_directory(self):
        import os
        current = os.getcwd()
        print(f'Current Working Directory>> {current}')
        print('Would you like to see files and folders in this directory?')
        rep = input('Reply with "yes" or "no">> ')
        if rep == "yes":
            print(os.listdir())


if __name__ == '__main__':
    file_manager = FileManager()
    while True:
        print('\n\n')
        print('_' * 40)
        print("\n\t\t  FILE MANAGER (v1.1)\n  Select one of the following commands")
        print('_' * 40)
        print('')
        print('(1)\tRead File\n(2)\tWrite File\n(3)\tDisplay File/Folder Details\n(4)\tDelete File\n(5)\tDelete Folder\n(6)\tCopy Folder\n(7)\tMove Folder\n(8)\tRename Folder\n(9)\tCheck Current Directory\n(0)\tExit')
        print('_' * 40)
        print('')
        choice = input(">> ")
        print('_' * 40)
        if choice == "0":
            print('exiting.......Done!')
            break
        elif choice == "1":
            print('\n\nREAD FILE')
            print('-' * 40)
            path = input('Enter full path of file to read data>> ')
            file_manager.read_file(path)
        elif choice == "2":
            print('\n\nWRITE FILE')
            print('-' * 40)
            path = input('Enter full path of file to write data>> ')
            file_manager.write_file(path)
        elif choice == "3":
            print('\n\nDISPLAY FILE/FOLDER DETAILS')
            print('-' * 40)
            path = input('Enter full path of directory>> ')
            file_manager.display_file_details(path)
        elif choice == "4":
            print('\n\nDELETE FILE')
            print('-' * 40)
            path = input('Enter full path of file to delete>> ')
            file_manager.remove_file(path)
        elif choice == "5":
            print('\n\nDELETE FOLDER')
            print('-' * 40)
            path = input('Enter full path of folder to delete>> ')
            file_manager.remove_folder(path)
        elif choice == "6":
            print('\n\nCOPY FOLDER')
            print('-' * 40)
            print("Enter source and destination folder: ")
            src = input('Source(full path): ')
            dest = input("Destination(full path): ")
            file_manager.copy_folder(src, dest)
        elif choice == "7":
            print('\n\nMOVE FOLDER')
            print('-' * 40)
            print("Enter source and destination folder: ")
            src = input('Source(full path): ')
            dest = input("Destination(full path): ")
            file_manager.move_folder(src, dest)
        elif choice == "8":
            print('\n\nRENAME FOLDER')
            print('-' * 40)
            print("Enter old and new folder path: ")
            old = input('Old name(full path): ')
            new = input('New name(full path): ')
            file_manager.rename_folder(old, new)
        elif choice == "9":
            print('\n\nCURRENT WORKING DIRECTORY')
            print('-' * 40)
            file_manager.working_directory()
        else:
            print('Invalid Input!')
