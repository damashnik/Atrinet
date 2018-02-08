import os

# Define global variables
list_vobs = []
file_name = "config_spec"

def scan_dirs (root_dir):
    #Solution in one line:
    for filename in glob.iglob(root_dir + '**/*', recursive=True):
        print(filename)
    #################################################################

    #Solution more complicated but very important:
    import os
    import sys

    rootdir = sys.argv[1]

    for folder, subs, files in os.walk(rootdir):
        with open(os.path.join(folder, 'python-outfile.txt'), 'w') as dest:
            for filename in files:
                with open(os.path.join(folder, filename), 'r') as src:
                    dest.write(src.read())


    # Or one more solution:
    import os
    import sys

    walk_dir = sys.argv[1]

    print('walk_dir = ' + walk_dir)

    # If your current working directory may change during script execution, it's recommended to
    # immediately convert program arguments to an absolute path. Then the variable root below will
    # be an absolute path as well. Example:
    # walk_dir = os.path.abspath(walk_dir)
    print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

    for root, subdirs, files in os.walk(walk_dir):
        print('--\nroot = ' + root)
        list_file_path = os.path.join(root, 'my-directory-list.txt')
        print('list_file_path = ' + list_file_path)

        with open(list_file_path, 'wb') as list_file:
            for subdir in subdirs:
                print('\t- subdirectory ' + subdir)

            for filename in files:
                file_path = os.path.join(root, filename)

                print('\t- file %s (full path: %s)' % (filename, file_path))

                with open(file_path, 'rb') as f:
                    f_content = f.read()
                    list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
                    list_file.write(f_content)
                    list_file.write(b'\n')

    print ("Scanning root directory:")
    for i in root_dir:
        if i != file_name:
            for j in i:
                if j != file_name:
                    for k in j:
                        if k!=file_name:
                            for n in k:
                                if n!= file_name:
                                    print ("there in no config file at 5 level!!!", os.path.join())


    pass

def create_vobs_list (dest_file):
    print ("Open config_spec file")
    print ("Extract lines with =")
    print ("Split by =, then second part split by ], then first part split by /")
    print ("Add extracted information to list")
    pass

def unique_list (list_vobs):
    print ("Get a list")
    # Not order preserving
    keys = {}
    for e in list_vobs:
        keys[e] = 1
    return keys.keys()

